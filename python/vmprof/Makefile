test:
	python test_serializer.py
	vmprofshow vmprof_json.dat --indent=2 --prune_percent=5
	vmprofshow vmprof_msgpack.dat --indent=2 --prune_percent=5

clean:
	rm -f *.dat
