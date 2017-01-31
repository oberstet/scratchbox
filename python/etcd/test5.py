hfrom time import sleep
import etcd3

etcd = etcd3.client()

etcd.get('foo')
etcd.put('foo', 'doot')
#etcd.delete('foo')

#for event in etcd.watch('foo'):
#    r = yield event
#    print(event)

# create a lock that expires after 20 seconds
with etcd.lock('toot', ttl=20) as lock:
    # do something that requires the lock
    print(lock.is_acquired())

    # refresh the timeout on the lease
    lock.refresh()

    sleep(10)
