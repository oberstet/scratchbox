# Git

Git is great, but I forget the more obscure spells all the time.

## Create a Twisted Patch

Create issue/feature branch:

	git checkout -b fix_9999

Do stuff, add, commit .. lets say `615d4a` is last commit before patch

	git log -n 2

then

	git diff 615d4a > fix_9999.patch

To check that the patch applies

	git checkout trunk
	patch -p1 < fix_9999.patch

	
## Changing Repo Origin

	git remote remove goeddea
	
	git config remote.origin.url git@bitbucket.org:oberstet/sixtdemo.git
	git push -u origin --all
	git push -u origin --tags
	
	git remote add goeddea git@bitbucket.org:goeddea/sixtdemo.git
	git fetch --all
	git merge goeddea


## Freshing up submodules - recursively

git submodule update --init --recursive


## Forwarding a submodule

cd SOMEREPO/SUBMODULE
git checkout master
git pull
cd ..
git add .
git commit -m "forward submodule SUBMODULE"
git push
git submodule update --init --recursive


## History of a file

Show history of a file following file renames:

	git log --follow -p crossbar/adminwebmodule/oraconnects.py

## Cleaning up history

### Removing files from history

The following will remove all files matching the given patterns from the repo history by rewriting history:

Clone the repo

	git clone --no-hardlinks WebMQ __WebMQ
    cd __WebMQ

Remove all tags

	git tag -d <TAG>

Filter

	git filter-branch -f --prune-empty --index-filter "git rm -rf --cached --ignore-unmatch '*.js' '*.jgz' '*.html' '*.css' '*.svg' '*.png' '*.jpg' '*.ttf' '*.woff' '*.eot' '*.md' '*.vsd' '*.pdf' '*.xlsx' '*.cpp' '*.h' '*.ino' '*.exe' '*.json' '*.ico' '*.pyc' 'LICENSE.txt' 'README' 'dropin.cache' 'appliance' 'webmqlas' 'test' 'demo' 'docs'" -- --all

	git filter-branch -f --prune-empty --index-filter "git rm -rf --cached --ignore-unmatch '*.js' '*.html' '*.css'"  -- --all

Cleanup

	git gc --prune
    rm -rf .git/refs/original/

### Removing branches from history



