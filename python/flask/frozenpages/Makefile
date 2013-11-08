clean:
	rm -rf build

test:
	python sitebuilder.py

freeze_and_test:
	python sitebuilder.py build
	twistd.py -n web --port=8000 --path="build"
