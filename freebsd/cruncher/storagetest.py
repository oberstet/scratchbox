import argparse
import subprocess
import json
from datetime import datetime
import psycopg2


STORSYS_INTERNAL_SSD_DEV = [
    #'sda',
    'sdb',
    'sdc',
    #'sdd',
    'sde',
    'sdf',
    'sdg',
    'sdh',
    'sdi',
    'sdj',
    'sdk',
    'sdl',
]

STORSYS_INTERNAL_NVME_DEV = [
    'nvme0n1',
    'nvme1n1',
    'nvme2n1',
    'nvme3n1',
    'nvme4n1',
    'nvme5n1',
    'nvme6n1',
    'nvme7n1',
]

STORSYS_EXTERNAL_HDD_DEV = [
    'sdm',
    'sdn',
    'sdo',
    'sdp',
    'sdq',
    'sdr',
    'sds',
    'sdt',
    'sdu',
    'sdv',
    'sdw',
    'sdx',
    'sdy',
    'sdz',
    'sdaa',
    'sdab',
    'sdac',
    'sdad',
    'sdae',
    'sdaf',
    'sdag',
    'sdah',
    'sdai',
    'sdaj',
]

TESTS = [
    {
        'name': 'random-read-4k',
        'bs': 4,
        'rw': 'randread'
    },
    {
        'name': 'random-write-4k',
        'bs': 4,
        'rw': 'randwrite'
    },
    {
        'name': 'random-read-8k',
        'bs': 8,
        'rw': 'randread'
    },
    {
        'name': 'random-write-8k',
        'bs': 8,
        'rw': 'randwrite'
    },
    {
        'name': 'random-readwrite7030-8k',
        'bs': 8,
        'rw': 'randrw',
        'rwmixread': 70
    },
    {
        'name': 'sequential-read-128k',
        'bs': 128,
        'rw': 'read'
    },
    {
        'name': 'sequential-write-128k',
        'bs': 128,
        'rw': 'write'
    },
]

TEST_VARIANTS = [
    {
        'ioengine': 'sync',
        'numjobs': [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],
        'iodepth': [1]
    },
    {
        'ioengine': 'aio',
        'numjobs': [1, 2, 4, 8, 16, 32, 64],
        'iodepth': [1, 2, 4, 8, 16, 32, 64]
    },
]



def utcnow():
    now = datetime.utcnow()
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def fio(spec, filename, size=None, runtime=10, ramptime=0, ioengine='sync', iodepth=1, numjobs=1, json=True):
    args = [
        '/usr/bin/fio',
        '--name={}'.format(spec.get('name', 'fio-test')),
        '--filename={}'.format(filename),
        '--ioengine={}'.format(ioengine),
        '--rw={}'.format(spec.get('rw', 'read')),
        '--bs={}k'.format(int(spec.get('bs', 4))),
        '--runtime={}'.format(int(runtime)),
        '--ramp_time={}'.format(int(ramptime)),
        '--iodepth={}'.format(int(iodepth)),
        '--numjobs={}'.format(int(numjobs)),
        '--thread=1',
        '--direct=1',
        '--time_based=1',
        '--randrepeat=0',
        '--norandommap',
        '--refill_buffers=1',
        '--end_fsync=1',
        '--group_reporting', 
    ]

    if 'rwmixread' in spec:
        args.append('--rwmixread={}'.format(int(spec['rwmixread'])))
    if size:
        args.append('--size={}'.format(int(size)))
    if json:
        args.append('--output-format=json')

    print("Running FIO: {}".format(' '.join(args)))

    res = subprocess.check_output(args)

    return res


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument("--description", type=str, required=True, help='Test setup description')
    parser.add_argument("--filename", type=str, required=True, help='Filename or device to run tests on, e.g. /dev/sdl')
    parser.add_argument("--filesize", type=str, default=None, help='Size of test data, e.g. 10g.')
    parser.add_argument("--runtime", type=int, default=10, help='Run-time in seconds, default is 10.')
    parser.add_argument("--ramptime", type=int, default=0, help='Rampup-time in seconds, default is 0.')

    args = parser.parse_args()

    conn = psycopg2.connect(host="192.168.9.1", port=5432, database="adr", user="oberstet", password="123456")
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT nextval('perf.seq_storage_test')")
    test_id = cur.fetchone()[0]

    started = datetime.datetime.now()

    cur.execute("INSERT INTO perf.tbl_storage_test (id, descr, filename, filesize, runtime, ramptime, started) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (test_id, args.description, args.filename, args.filesize, args.runtime, args.ramptime, started))

    with open(args.output, 'a') as out:
        for variant in TEST_VARIANTS:
            for numjobs in variant['numjobs']:
                for iodepth in variant['iodepth']:

                    cur.execute("SELECT nextval('perf.seq_storage_test_result')")
                    test_result_id = cur.fetchone()[0]

                    test_started = datetime.datetime.now()

                    result = fio(TESTS[0], filename=args.filename, size=args.filesize,
                        ioengine=variant['ioengine'], iodepth=iodepth, numjobs=numjobs)

                    test_ended = datetime.datetime.now()

                    #output = json.dumps(res, separators=(',', ':'), ensure_ascii=False)
                    print res

                    cur.execute("INSERT INTO perf.tbl_storage_test_result (id, test_id, started, ended, result) VALUES (%s, %s, %s, %s, %s)",
                        (test_result_id, test_id, test_started, test_ended, result))

    ended = datetime.datetime.now()

    cur.execute("UPDATE perf.tbl_storage_test SET ended = %s", (ended,))
