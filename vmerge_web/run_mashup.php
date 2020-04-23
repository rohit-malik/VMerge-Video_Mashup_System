<?php
//database constants
include('session.php');
error_reporting(E_ALL);
ini_set('display_errors', 1);

$event_ID = $_GET["event_ID"];	
$event_name = $_GET["event_name"];	

#$python_cmd = '/home/vmash/VMERGE/run_python_script.sh ' . $event_name;
$python_cmd = 'python2 /home/vmash/VMERGE/Audio_Smoothing/smooth.py';
echo $python_cmd;

$command = escapeshellcmd($python_cmd);
$output = shell_exec($command);

echo $output;
var_dump($output);

$conn->close();

?>
