import os
import sys
import argparse
import subprocess
import json
from datetime import datetime, timedelta
import psycopg2

# 10 internal Intel DC S3700 SATA SSDs
#
STORSYS_INTERNAL_SSD_DEV = [
    #'sda', # boot/system disk!! do NOT touch!
    'sdb',
    'sdc',
    #'sdd', # boot/system disk!! do NOT touch!
    'sde',
    'sdf',
    'sdg',
    'sdh',
    'sdi',
    'sdj',
    'sdk',
    'sdl',
]

# 8 internal Intel P3700 NVMe SSDs
#
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

# 24 external Seagate Constellation ES.3 disks
#
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


# 7 tests
#
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


# 60 test variants
#
TEST_VARIANTS = [
    # 11 test variants
    {
        'ioengine': 'sync',
        'numjobs': [1, 2, 4, 8, 16, 32, 48, 64, 128, 256, 512],
        'iodepth': [1]
    },
    # 49 test variants
    {
        'ioengine': 'aio',
        'numjobs': [1, 2, 4, 8, 16, 32, 64],
        'iodepth': [1, 2, 4, 8, 16, 32, 64]
    },
]


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

    cmd = ' '.join(args)

    print("Running FIO: {}".format(cmd))

    res = subprocess.check_output(args)

    return (cmd, res)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # target database
    #
    parser.add_argument("--pghost", type=str, required=True, help='PostgreSQL database server.')
    parser.add_argument("--pgport", type=int, default=5432, help='PostgreSQL database server listening port.')
    parser.add_argument("--pgdb", type=str, required=True, help='PostgreSQL database name.')
    parser.add_argument("--pguser", type=str, required=True, help='PostgreSQL database user.')
    parser.add_argument("--pgpassword", type=str, default=os.environ.get('PGPASSWORD', None), help='PostgreSQL database user password.')
    
    # test setup
    #
    parser.add_argument("--description", type=str, required=True, help='Test setup description')
    parser.add_argument("--filename", type=str, required=True, help='Filename or device to run tests on, e.g. /dev/sdl')
    parser.add_argument("--filesize", type=str, default=None, help='Size of test data, e.g. 10g.')
    parser.add_argument("--runtime", type=int, default=10, help='Run-time in seconds, default is 10.')
    parser.add_argument("--ramptime", type=int, default=0, help='Rampup-time in seconds, default is 0.')

    # limit number of tests run
    #
    parser.add_argument("--limit", type=int, default=None, help='Limit number of tests run.')

    # parse cmd line args
    #
    args = parser.parse_args()

    # connect to DB
    #
    conn = psycopg2.connect(host=args.pghost, port=args.pgport, database=args.pgdb, user=args.pguser, password=args.pgpassword)
    conn.autocommit = True
    cur = conn.cursor()

    # give user last chance to exit
    #
    test_count = 0
    for test in TESTS:
        for variant in TEST_VARIANTS:
            for numjobs in variant['numjobs']:
                for iodepth in variant['iodepth']:
                    test_count += 1

    if args.limit is not None:
        test_count = args.limit

    estimated_duration = test_count * (args.ramptime + args.runtime)

    started = datetime.now()

    estimated_end = started + timedelta(seconds=estimated_duration)

    print("Ok, I will run {} tests, which will take {} seconds and end at (estimated) {}".format(test_count, estimated_duration, estimated_end))

    while True:
        ok = raw_input("Continue? (y/n)").lower()
        if ok in ['y', 'n']:
            break

    if ok == 'n':
        sys.exit(0)

    cur.execute("SELECT nextval('perf.seq_storage_test')")
    test_id = cur.fetchone()[0]

    cur.execute("INSERT INTO perf.tbl_storage_test (id, descr, filename, filesize, runtime, ramptime, started, test_count, estimated_end, estimated_duration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (test_id, args.description, args.filename, args.filesize, args.runtime, args.ramptime, started, test_count, estimated_end, estimated_duration))

    cnt_tests = 0

    for test in TESTS:

        for variant in TEST_VARIANTS:

            ioengine = variant['ioengine']

            for numjobs in variant['numjobs']:

                for iodepth in variant['iodepth']:

                    if args.limit is None or cnt_tests < args.limit:

                        cur.execute("SELECT nextval('perf.seq_storage_test_result')")
                        test_result_id = cur.fetchone()[0]

                        test_started = datetime.now()

                        (cmd, result) = fio(test, filename=args.filename, size=args.filesize,
                            ioengine=ioengine, iodepth=iodepth, numjobs=numjobs)

                        test_ended = datetime.now()

                        cur.execute("INSERT INTO perf.tbl_storage_test_result (id, test_id, name, command, ioengine, iomode, blocksize, iodepth, numjobs, started, ended, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (test_result_id, test_id, test.get('name', 'fio-test'), cmd, ioengine, test.get('rw', 'read'), int(test.get('bs', 4)), iodepth, numjobs, test_started, test_ended, result))

                        cnt_tests += 1

    ended = datetime.now()

    cur.execute("UPDATE perf.tbl_storage_test SET ended = %s", (ended,))
