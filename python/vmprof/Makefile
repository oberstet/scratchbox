all: clean profile show

profile:
	python test_serializer.py

show:
	@echo "JSON Serialization:"
	@echo
	vmprofshow vmprof_test_serialize_json.dat --indent=2 --prune_percent=5
	@echo

	@echo "MsgPack Serialization:"
	@echo
	vmprofshow vmprof_test_serialize_msgpack.dat --indent=2 --prune_percent=5
	@echo

	@echo "JSON Unserialization:"
	@echo
	vmprofshow vmprof_test_unserialize_json.dat --indent=2 --prune_percent=5
	@echo

	@echo "MsgPack UNserialization:"
	@echo
	vmprofshow vmprof_test_unserialize_msgpack.dat --indent=2 --prune_percent=5
	@echo

clean:
	rm -f *.dat
