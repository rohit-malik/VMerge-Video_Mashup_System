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

				<!-- Header -->
					<header id="header">
						<a href="event_list.php" class="logo">VMERGE</a>
					</header>

				<!-- Nav -->
					<nav id="nav">
						<ul class="links">

						</ul>
						<ul class="icons">
							<li><a href = "logout.php">Sign Out</a></li>
						</ul>
					</nav>

				<!-- Main -->
					<div id="main">

						<!-- Post -->
							<section class="post">
								<header class="major">
									<h2>VIDEO LIST</h2>
								</header>

						
						<?php
						//database constants
						include('session.php');

						$event_ID = $_GET["event_ID"];	
						$event_name = $_GET["event_name"];	
						$sql = "SELECT video_ID, video_name, video_desc FROM video where video.event_ID='$event_ID'; ";
						$result = $conn->query($sql);

						echo "<h3>Event \"" . $event_name ."\"<h3>";

						echo "<table border='1'>
						<tr>
						<th>Video Id</th>
						<th>Video Name</th>
						<th>Video Description</th>
						</tr>";

						if ($result->num_rows > 0) {
						// output data of each row
						while($row = $result->fetch_assoc()) {
							echo "<tr>";
							echo "<td>" . $row['video_ID'] . "</td>";
							echo "<td><a href=\"play_video.php?video_name=" . $row['video_name'] . "&event_name=" . $event_name . "\">" . $row['video_name'] . "</a></td>";
							echo "<td>" . $row['video_desc'] . "</td>";
								echo "</tr>";    
						}
						} else {
						echo "0 results";
						}

						echo "</table>";
						echo "<h4><a href=\"http://172.26.1.221/AndroidUploadImage/" . $event_name . "/mashup/mashup.mp4\" download=\"" . $event_name . "_mashup.mp4\" class='button primary'>Download Mashup</a></h4>";

						$conn->close();

						?>

						<br><br>
						<h3>Select video to upload:</h3>
						<form action="upload.php" method="post" enctype="multipart/form-data">
						    
						    <input type="file" name="image" id="image" multiple="multiple" class='button'>
						    <input type="submit" value="Upload Image" name="submit" class='button primary'>
						    <input type='hidden' name='event_name' value='<?=$event_name?>'/> 
						    <input type='hidden' name='event_id' value='<?=$event_ID?>'/> 

						</form>

					</div>

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
