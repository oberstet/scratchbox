import os
import subprocess

outfile_name = 'tavendo_to_crossbario_ip_git_reporefs_fingerprints.csv'

repo_basedir = os.path.expanduser('~/scm/')

repo_names = [
    'crossbario/autobahn-c',
    'crossbario/autobahn-cpp',
    'crossbario/autobahn-java',
    'crossbario/autobahn-js',
    'crossbario/autobahn-python',
    'crossbario/autobahn-testsuite',
    'crossbario/autobahn-www',
    'crossbario/crossbar',
#    'crossbario/crossbar-cloud',
    'crossbario/crossbar-docker',
    'crossbario/crossbar-examples',
    'crossbario/crossbar-fabric',
    'crossbario/crossbar-fabric-center',
    'crossbario/crossbar-fabric-center-web',
    'crossbario/crossbar-fabric-hangouts',
    'crossbario/crossbar-fabric-package',
    'crossbario/crossbar-fabric-shell',
    'crossbario/crossbar-fabric-testrig',
    'crossbario/crossbar-www',
    'crossbario/crossbario-organize',
    'crossbario/crossbario-www',
#    'crossbario/organize',
    'crossbario/txaio',
    'crossbario/wsperf',
    'wamp-proto/wamp-proto',
    'wamp-proto/wamp-web',
]

with open(outfile_name, 'w') as outfile:
    outfile.write('"repo_name","ref_name","ref_sha1"\n')
    for repo_name in repo_names:
        repo_path = os.path.join(repo_basedir, repo_name)
        res = subprocess.check_output(['git', 'show-ref', '--head', '--dereference'],
                                      cwd=repo_path)
        res = res.splitlines()

        for l in res:
            ref_sha1, ref_name = l.decode().split()
            outfile.write('"{repo_name}","{ref_name}","{ref_sha1}"\n'.format(repo_name=repo_name,
                                                                             ref_name=ref_name,
                                                                             ref_sha1=ref_sha1))
