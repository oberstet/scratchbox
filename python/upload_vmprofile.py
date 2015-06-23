import sys
import argparse
from collections import namedtuple

import vmprof

parser = argparse.ArgumentParser(
    description='VMprof',
    prog="vmprof"
)

parser.add_argument(
    'profile',
    help='Profile file'
)

parser.add_argument(
    '--program',
    default='Crossbar.io Router Worker',
    help='program'
)

parser.add_argument(
    '--web-auth',
    help='Authtoken for your acount on the server, works only when --web is used'
)

parser.add_argument(
    '--web',
    metavar='url',
    default='vmprof.baroquesoftware.com',
    help='Upload profiling stats to a remote server'
)

args = parser.parse_args()
args.args = []

stats = vmprof.read_profile(args.profile, virtual_only=True)

vmprof.cli.show(stats)

vmprof.com.send(stats, args)
