import subprocess

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

#
# --filename
# --size
# --ioengine
# --iodepth
# --numjobs
# --runtime
# --ramp_time


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
        'name': 'random-read70write30-8k',
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


def fio(spec, filename, size=None, runtime=30, ramptime=0, ioengine='sync', iodepth=1, numjobs=1):
    args = [
        '/usr/bin/fio',
        '--filename="{}"'.format(filename),
        '--ioengine={}'.format(ioengine),
        '--rw={}'.format(spec.get('rw', 'read')),
        '--bs={}k'.format(int(spec.get('bs', 4))),
        '--output-format=json',
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
    ]

    if 'rwmixread' in spec:
        args.append('--rwmixread={}'.format(int(spec['rwmixread'])
    if size:
        args.append('--size={}'.format(int(size))

    res = subprocess.check_output()

    return res


print fio(TESTS[0], "/dev/sdl")
