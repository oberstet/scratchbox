Git
===

Git is great, but I forget the more obscure spells all the time.


Freshing up submodules - recursively
------------------------------------

git submodule update --init --recursive


Forwarding a submodule
----------------------

cd SOMEREPO/SUBMODULE
git checkout master
git pull
cd ..
git add .
git commit -m "forward submodule SUBMODULE"
git push
git submodule update --init --recursive
