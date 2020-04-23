<?php
include('session.php');

    if(isset($_POST['event_name'])){
	$event_name = $_POST['event_name'];
    }
    if(isset($_POST['event_id'])){
    $event_id = $_POST['event_id'];
    }     

    // Path to move uploaded files
    $target_path = '/opt/lampp/htdocs/AndroidUploadImage/' . $event_name .'/';
    if (isset($_FILES['image']['name'])) {
        $target_path = $target_path . basename($_FILES['image']['name']);
	
        try {
            // Throws exception incase file is not being moved
            if (!move_uploaded_file($_FILES['image']['tmp_name'], $target_path)) {
                // make error flag true
                echo json_encode(array('status'=>'fail', 'message'=>'could not move file'));
            }

            // File successfully uploaded
            echo json_encode(array('status'=>'success', 'message'=>'File Uploaded'));
        } catch (Exception $e) {
            // Exception occurred. Make error flag true
            echo json_encode(array('status'=>'fail', 'message'=>$e->getMessage()));
        }
    
        $video_name = basename($_FILES['image']['name']);
        $email = $_SESSION['email'];

        $sql = "SELECT user_id FROM user_info WHERE user_info.email_id = '$email'";
        $result = $conn->query($sql);

        while($row = $result->fetch_assoc()) {
            $user_id = $row['user_id'];
        }

        $sql = "INSERT into video (video_name, event_ID, user_id) values('$video_name', '$event_id', '$user_id')";

            if ($conn->query($sql) === TRUE) {
                echo "Video added in the database";
                // header("Location: video_list.php");

            } else {
                echo "Video could not be added in the database";
                echo "Error: " . $sql . "<br>" . $conn->error;
            }
            
            $conn->close();

    } else {
        // File parameter is missing
        echo json_encode(array('status'=>'fail', 'message'=>'Not received any file'));
    }
    
?>
