<?php
class QueryDatabase
{
	protected $_db;
	protected $_result;
	public $results;

	public function __construct()
	{
		error_log("Connecting to Oracle ..");
		//$_db = oci_connect('test1', 'test1', '192.168.1.118/orcl');
		$_db = oci_connect('test1', 'test1', '192.168.56.102/orcl');

		if (!$_db) {
			$e = oci_error();
			die("Unable to connect: $_db" . $e['message']);
		} else {
			error_log("Connected to Oracle!");
		}
		return $_db;
	}

	public function getResults(stdClass $params)
	{
		$_db = $this->__construct();

		$stid = oci_parse($_db, 'SELECT id, name, address, state FROM owners');
		oci_execute($stid);

		$results = array();

		while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS)) {
			array_push($results, $row);
		}

		return $results;
	}

	public function __destruct()
	{
		$_db = $this->__construct();
		//$_db->close();

		return $this;
	}
}
