<?php 
 
	
	//database constants
	define('DB_HOST', 'localhost');
	define('DB_USER', 'root');
	define('DB_PASS', '');
	define('DB_NAME', 'vmerge');
	
	//connecting to database and getting the connection object
	$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
	
	//Checking if any error occured while connecting
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
		die();
	}
	
	$event_name = $_POST['event_name'];
	$event_desc = $_POST['event_desc'];

	//creating a query
	$stmt = $conn->prepare("INSERT into event(event_name, event_info) values('$event_name', '$event_desc');");
	
	//executing the query 
	$stmt->execute();
	$target_path ='/opt/lampp/htdocs/AndroidUploadImage/' . $event_name;
	
	if (!is_dir($target_path)) {
		mkdir($target_path, 0777);
		chmod($target_path, 0777);
		mkdir($target_path . "/mashup", 0777);
		chmod($target_path . "/mashup", 0777);
		echo json_encode(array('status'=>'success', 'message'=>'Event Successfully Added'));
	}
	else{
		echo "Event already Exists";
	}
	$conn->close();
	
?>
