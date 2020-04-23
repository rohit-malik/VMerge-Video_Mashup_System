<!DOCTYPE HTML>
<!--
	Massively by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Generic Page - Massively by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">
				<?php
				require_once 'vendor/autoload.php';
				include("config.php");
				session_start();
				  // $_SESSION['login_user'] = 'genuine_user';


				// init configuration
				$clientID = '515003037690-lhb4o1df38i5e8jg3efamoe2ot67g8lu.apps.googleusercontent.com';
				$clientSecret = 'Yq1mCJTU_aLyQ7h_m4UKXn6X';
				$redirectUri = 'http://172.26.1.221.xip.io/vmerge_web/login.php';
				  
				// create Client Request to access Google API
				$client = new Google_Client();
				$client->setClientId($clientID);
				$client->setClientSecret($clientSecret);
				$client->setRedirectUri($redirectUri);
				$client->addScope("email");
				$client->addScope("profile");

				// $google_oauthV2 = new Google_Service_Oauth2($client);
				// authenticate code from Google OAuth Flow
				if (isset($_GET['code'])) {
				  $token = $client->fetchAccessTokenWithAuthCode($_GET['code']);
				  $client->setAccessToken($token['access_token']);
				  
				  // get profile info
				  $google_oauth = new Google_Service_Oauth2($client);
				  $google_account_info = $google_oauth->userinfo->get();
				  $email =  $google_account_info->email;
				  $name =  $google_account_info->name;


				  $sql = "SELECT email_id FROM user_info WHERE email_id = '$email'";
				      $result = mysqli_query($conn,$sql);
				      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
				      // $active = $row['active'];
				      
				      $count = mysqli_num_rows($result);
				      
				      // If result matched $myusername and $mypassword, table row must be 1 row
				      if($count != 1) {
				         $stmt = $conn->prepare("INSERT into user_info(user_name, email_id, user_type) values('$name', '$email', 'user');");
				         //executing the query 
				         $stmt->execute();
				         echo json_encode(array('status'=>'success', 'message'=>'Successfully Registered'));
				         $conn->close();

				      }

				  $_SESSION['email'] = $email;
				  header("location:event_list.php");
				  // now you can use this profile info to create account in your website and make user logged in.
				} else {
					echo "<header id='header'>";
				  echo "<a href='".$client->createAuthUrl()."' class='logo'>VMERGE Login</a>";
				  echo "</header>";
				}
				?>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
