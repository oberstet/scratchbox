# Git

Git is great, but I forget the more obscure spells all the time.


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



