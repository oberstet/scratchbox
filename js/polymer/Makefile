run:
	twistd --nodaemon web --port=8080 --path=.

install:
	npm install bower
	./node_modules/bower/bin/bower init
	./node_modules/bower/bin/bower install --save Polymer/polymer
	./node_modules/bower/bin/bower install --save autobahn
