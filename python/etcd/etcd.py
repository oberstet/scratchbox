from __future__ import print_function

import json
import binascii

from twisted.internet.defer import Deferred, succeed, inlineCallbacks, returnValue
from twisted.internet import protocol
from twisted.web.client import Agent, HTTPConnectionPool
from twisted.web.iweb import IBodyProducer, UNKNOWN_LENGTH
from twisted.web.http_headers import Headers

import treq

__all__ = (
    'Client',
    'Value',
    'Header',
    'Status'
)


def _increment_last_byte(byte_string):
    s = bytearray(byte_string)
    s[-1] = s[-1] + 1
    return bytes(s)


class _BufferedSender(object):

    length = UNKNOWN_LENGTH

    def __init__(self, body):
        self.body = body
        self.length = len(body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass


class _BufferedReceiver(protocol.Protocol):
    def __init__(self, done):
        self._buf = []
        self._done = done

    def dataReceived(self, data):
        self._buf.append(data)

    def connectionLost(self, reason):
        # TODO: test if reason is twisted.web.client.ResponseDone, if not, do an errback
        if self._done:
            self._done.callback(b''.join(self._buf))
            self._done = None


class _StreamingReceiver(protocol.Protocol):

    def __init__(self, cb, done=None):
        self._buf = ''
        self._cb = cb
        self._done = done

    def dataReceived(self, data):
        self._buf += data
        while True:
            i = self._buf.find('\n')
            if i > 0:
                data = self._buf[:i]
                try:
                    obj = json.loads(data)
                except:
                    pass
                else:
                    for evt in obj['result'].get('events', []):
                        if 'kv' in evt:
                            d = evt['kv']

                            key = binascii.a2b_base64(d['key'])
                            value = binascii.a2b_base64(d['value'])
                            create_revision = d['create_revision']
                            mod_revision = d['mod_revision']
                            version = d['version']

                            try:
                                self._cb(key, value)
                            except Exception as e:
                                print('warning: swallowed exception in watch callback: {}'.format(e))
                self._buf = self._buf[i + 1:]
            else:
                break

    def connectionLost(self, reason):
        # TODO: test if reason is twisted.web.client.ResponseDone, if not, do an errback
        if self._done:
            self._done.callback(reason)
            self._done = None


class Header(object):
    """
    u'header':
    {
        u'raft_term': u'2',
        u'revision': u'285',
        u'cluster_id': u'243774308834426361',
        u'member_id': u'17323375927490080838'
    }
    """
    def __init__(self, raft_term, revision, cluster_id, member_id):
        self.raft_term = raft_term
        self.revision = revision
        self.cluster_id = cluster_id
        self.member_id = member_id

    @staticmethod
    def parse(obj):
        raft_term = int(obj['raft_term']) if 'raft_term' in obj else None
        revision = int(obj['revision']) if 'revision' in obj else None
        cluster_id = int(obj['cluster_id']) if 'cluster_id' in obj else None
        member_id = int(obj['member_id']) if 'member_id' in obj else None
        return Header(raft_term, revision, cluster_id, member_id)

    def __str__(self):
        return u'Header(raft_term={}, revision={}, cluster_id={}, member_id={})'.format(self.raft_term, self.revision, self.cluster_id, self.member_id)


class Status(object):
    """
    {
        u'raftTerm': u'2',
        u'header':
        {
            u'raft_term': u'2',
            u'revision': u'285',
            u'cluster_id': u'243774308834426361',
            u'member_id': u'17323375927490080838'
        },
        u'version': u'3.1.0',
        u'raftIndex': u'288',
        u'dbSize': u'57344',
        u'leader': u'17323375927490080838'
    }
    """
    def __init__(self, version, dbSize, leader, header, raftTerm, raftIndex):
        self.version = version
        self.dbSize = dbSize
        self.leader = leader
        self.header = header
        self.raftTerm = raftTerm
        self.raftIndex = raftIndex

    @staticmethod
    def parse(obj):
        version = obj['version'] if 'version' in obj else None
        dbSize = int(obj['dbSize']) if 'dbSize' in obj else None
        leader = int(obj['leader']) if 'leader' in obj else None
        header = Header.parse(obj['header']) if 'header' in obj else None
        raftTerm = int(obj['raftTerm']) if 'raftTerm' in obj else None
        raftIndex = int(obj['raftIndex']) if 'raftIndex' in obj else None
        return Status(version, dbSize, leader, header, raftTerm, raftIndex)

    def __str__(self):
        return u'Status(version={}, dbSize={}, leader={}, header={}, raftTerm={}, raftIndex={})'.format(self.version, self.dbSize, self.leader, self.header, self.raftTerm, self.raftIndex)


class Deleted(object):
    """
    {
        u'deleted': u'1',
        u'header':
            {
                u'raft_term': u'2',
                u'revision': u'334',
                u'cluster_id': u'243774308834426361',
                u'member_id': u'17323375927490080838'
            }
        }
    """
    def __init__(self, deleted, header):
        self.deleted = deleted
        self.header = header

    @staticmethod
    def parse(obj):
        deleted = int(obj['deleted']) if 'deleted' in obj else None
        header = Header.parse(obj['header']) if 'header' in obj else None
        return Deleted(deleted, header)

    def __str__(self):
        return u'Deleted(deleted={}, header={})'.format(self.deleted, self.header)


class Value(object):
    """
    etcd rich value object.
    """

    def __init__(self, value, version=None, create_revision=None, mod_revision=None):
        """

        :param value: The actual value.
        :type value: bytes
        :param version:
        :type version:
        :param create_revision:
        :type create_revision:
        :param mod_revision:
        :type mod_revision
        """
        self.value = value
        self.version = version
        self.create_revision = create_revision
        self.mod_revision = mod_revision

    def __str__(self):
        return 'Value({}, version={}, create_revision={}, mod_revision{})'.format(self.value, self.version, self.create_revision, self.mod_revision)


class Client(object):
    """
    etcd client that talks to the gRPC endpoint of etcd v3.

    TODO:
        * /v3alpha/kv/deleterange
        * /v3alpha/kv/txn
        * /v3alpha/lease/grant
        * /v3alpha/lease/keepalive
        * /v3alpha/kv/lease/revoke
        * /v3alpha/kv/lease/timetolive

    See: https://coreos.com/etcd/docs/latest/dev-guide/apispec/swagger/rpc.swagger.json
    """

    REQ_HEADERS = {'Content-Type': ['application/json']}
    """
    Default request headers for HTTP/POST requests issued to the
    gRPC endpoint of etcd.
    """

    def __init__(self, reactor, url, pool=None):
        """

        :param rector:
        :type reactor:
        :param url:
        :type url:
        :param pool:
        :type pool:
        """
        self._url = url
        self._pool = pool or HTTPConnectionPool(reactor, persistent=True)
        self._agent = Agent(reactor, connectTimeout=10, pool=self._pool)

    @inlineCallbacks
    def status(self):
        """
        Get etcd status.

        URL:     /v3alpha/maintenance/status
        """
        url = b'{}/v3alpha/maintenance/status'.format(self._url)
        obj = {
        }
        data = json.dumps(obj).encode('utf8')

        response = yield treq.post(url, data, headers=self.REQ_HEADERS)
        obj = yield treq.json_content(response)

        status = Status.parse(obj)

        returnValue(status)

    @inlineCallbacks
    def delete(self, key, range_end=None, prev_kv=False):
        """
        Delete value(s) from etcd.

        URL:     /v3alpha/kv/deleterange

        :param key: key is the first key to delete in the range.
        :type key: bytes
        :param range_end: range_end is the key following the last key to delete
            for the range [key, range_end).\nIf range_end is not given, the range
            is defined to contain only the key argument.\nIf range_end is one bit
            larger than the given key, then the range is all keys with the prefix
            (the given key).\nIf range_end is '\\0', the range is all keys greater
            than or equal to the key argument.
        :key range_end: bytes
        :param prev_kv: If prev_kv is set, etcd gets the previous key-value pairs
            before deleting it.\nThe previous key-value pairs will be returned in the
            delete response.
        :key prev_kv: bool
        """
        url = b'{}/v3alpha/kv/deleterange'.format(self._url)
        obj = {
            'key': binascii.b2a_base64(key),
            'range_end': binascii.b2a_base64(range_end) if range_end else None,
            'prev_kv': prev_kv
        }
        data = json.dumps(obj).encode('utf8')

        response = yield treq.post(url, data, headers=self.REQ_HEADERS)
        obj = yield treq.json_content(response)
        res = Deleted.parse(obj)

        returnValue(res)

    @inlineCallbacks
    def set(self, key, value, lease=None, prev_kv=None):
        """
        Put puts the given key into the key-value store.

        A put request increments the revision of the key-value
        store and generates one event in the event history.

        URL:     /v3alpha/kv/put

        :param key: key is the key, in bytes, to put into the key-value store.
        :type key: bytes
        :param lease: lease is the lease ID to associate with the key in the key-value store. A lease\nvalue of 0 indicates no lease.
        :type lease: int
        :param prev_kv: If prev_kv is set, etcd gets the previous key-value pair before changing it.\nThe previous key-value pair will be returned in the put response.
        :type prev_kv: bool
        :param value: value is the value, in bytes, to associate with the key in the key-value store.
        :key value: bytes
        """
        url = b'{}/v3alpha/kv/put'.format(self._url)
        obj = {
            'key': binascii.b2a_base64(key),
            'value': binascii.b2a_base64(value)
        }
        data = json.dumps(obj).encode('utf8')

        response = yield treq.post(url, data, headers=self.REQ_HEADERS)
        obj = yield treq.json_content(response)

        revision = obj['header']['revision']
        returnValue(revision)

    @inlineCallbacks
    def get(self, key, range_end=None, prefix=None):
        """
        Range gets the keys in the range from the key-value store.

        URL:    /v3alpha/kv/range

        :param key: key is the first key for the range. If range_end is not given, the request only looks up key.
        :type key: bytes

        :param range_end: range_end is the upper bound on the requested range
            [key, range_end).\nIf range_end is '\\0', the range is all keys \u003e= key.
            If the range_end is one bit larger than the given key, then the range requests
            get the all keys with the prefix (the given key).\nIf both key and range_end
            are '\\0', then range requests returns all keys.
        :type range_end: bytes

        :param prefix: If set, and no range_end is given, compute range_end from key prefix.
        :type prefix: bool

        :param count_only: count_only when set returns only the count of the keys in the range.
        :type count_only: bool

        :param keys_only: keys_only when set returns only the keys and not the values.
        :type keys_only: bool

        :param limit: limit is a limit on the number of keys returned for the request.
        :type limit: int

        :param max_create_revision: max_create_revision is the upper bound for returned key create revisions; all keys with\ngreater create revisions will be filtered away.
        :type max_create_revision: int

        :param max_mod_revision: max_mod_revision is the upper bound for returned key mod revisions; all keys with\ngreater mod revisions will be filtered away.
        :type max_mod_revision: int

        :param min_create_revision: min_create_revision is the lower bound for returned key create revisions; all keys with\nlesser create trevisions will be filtered away.
        :type min_create_revision: int

        :param min_mod_revision: min_mod_revision is the lower bound for returned key mod revisions; all keys with\nlesser mod revisions will be filtered away.
        :type min_min_revision: int

        :param revision: revision is the point-in-time of the key-value store to use for the
            range. If revision is less or equal to zero, the range is over the newest
            key-value store. If the revision has been compacted, ErrCompacted is returned as
            a response.
        :type revision: int

        :param serializable: serializable sets the range request to use serializable
            member-local reads. Range requests are linearizable by default; linearizable
            requests have higher latency and lower throughput than serializable requests
            but reflect the current consensus of the cluster. For better performance, in
            exchange for possible stale reads,\na serializable range request is served
            locally without needing to reach consensus\nwith other nodes in the cluster.
        :type serializable: bool

        :param sort_order:
        :type sort_order:

        :param sort_target:
        :type sort_taget:
        """
        url = b'{}/v3alpha/kv/range'.format(self._url)
        obj = {
            'key': binascii.b2a_base64(key)
        }
        if not range_end and prefix is True:
            range_end = _increment_last_byte(key)
        if range_end:
            obj['range_end'] = binascii.b2a_base64(range_end)
        data = json.dumps(obj).encode('utf8')

        response = yield treq.post(url, data, headers=self.REQ_HEADERS)
        obj = yield treq.json_content(response)

        count = int(obj.get('count', 0))
        if count == 0:
            raise Exception('no such key')
        else:
            if count > 1:
                values = {}
                for kv in obj['kvs']:
                    key = binascii.a2b_base64(kv['key'])
                    value = binascii.a2b_base64(kv['value'])
                    mod_revision = int(kv['mod_revision'])
                    create_revision = int(kv['create_revision'])
                    version = int(kv['version'])
                    values[key] = Value(value, version=version, create_revision=create_revision, mod_revision=mod_revision)
                returnValue(values)
            else:
                kv = obj['kvs'][0]
                value = binascii.a2b_base64(kv['value'])
                mod_revision = int(kv['mod_revision'])
                create_revision = int(kv['create_revision'])
                version = int(kv['version'])
                value = Value(value, version=version, create_revision=create_revision, mod_revision=mod_revision)
                returnValue(value)

    def watch(self, prefixes, on_watch, start_revision=None):
        """
        Watch one or more key prefixes and invoke a callback.

        Watch watches for events happening or that have happened. The entire event
        history can be watched starting from the last compaction revision.

        URL:     /v3alpha/watch

        :param prefixes: The prefixes to watch.
        :type prefixes: list of bytes
        :param on_watch: The callback to invoke upon receiving a watch event.
        :type on_watch: callable
        :param start_revision: start_revision is an optional revision to watch
            from (inclusive). No start_revision is \"now\".
        :type start_revision: int
        """
        d = self._start_watching(prefixes, on_watch, start_revision)

        def on_err(err):
            if isinstance(err.value, CancelledError):
                # swallow canceling!
                pass
            else:
                return err
        d.addErrback(on_err)

        return d

    def _start_watching(self, prefixes, on_watch, start_revision):
        data = []
        headers = dict()
        url = b'{}/v3alpha/watch'.format(self._url)

        # create watches for all key prefixes
        for key in prefixes:
            range_end = _increment_last_byte(key)
            obj = {
                'create_request': {
                    'start_revision': start_revision,
                    'key': binascii.b2a_base64(key),

                    # range_end is the end of the range [key, range_end) to watch.
                    # If range_end is not given,\nonly the key argument is watched.
                    # If range_end is equal to '\\0', all keys greater than nor equal
                    # to the key argument are watched. If the range_end is one bit
                    # larger than the given key,\nthen all keys with the prefix (the
                    # given key) will be watched.
                    'range_end': binascii.b2a_base64(range_end),

                    # progress_notify is set so that the etcd server will periodically
                    # send a WatchResponse with\nno events to the new watcher if there
                    # are no recent events. It is useful when clients wish to recover
                    # a disconnected watcher starting from a recent known revision.
                    # The etcd server may decide how often it will send notifications
                    # based on current load.
                    'progress_notify': True,
                }
            }
            data.append(json.dumps(obj).encode('utf8'))

        # HTTP/POST request in one go, but response is streaming ..
        d = self._agent.request('POST',
                                url,
                                Headers(headers),
                                _BufferedSender(b'\n'.join(data)))

        def handle_response(response):
            if response.code == 200:
                done = Deferred()
                response.deliverBody(_StreamingReceiver(on_watch, done))
                return done
            else:
                raise Exception('unexpected response status {}'.format(response.code))

        d.addCallback(handle_response)
        return d

    def submit(self, txn):
        """
        Submit a etcd transaction.
        """
        pass
