
#Add Upstream

	$ cat .hg/hgrc
	[paths]
	default = ssh://hg@bitbucket.org/oberstet/pypy
	upstream = ssh://hg@bitbucket.org/pypy/pypy
	
	$ hg pull upstream
	$ hg update
	
# List last N commits

	$ hg log -l 5

# Get help

	$ hg help log
