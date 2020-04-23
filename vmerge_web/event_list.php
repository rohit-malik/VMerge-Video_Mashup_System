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
						<a href="#" class="logo">VMERGE</a>
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
									<h2>EVENT LIST</h2>
								</header>

						<?php
						//database constants
						include('session.php');


						$sql = "SELECT event_ID, event_name, event_info FROM event";
						$result = $conn->query($sql);

						echo "<table>
						<tr>
						<th>Event ID</th>
						<th>Event Name</th>
						<th>Event Description</th>
						</tr>";

						if ($result->num_rows > 0) {
						    // output data of each row
						    while($row = $result->fetch_assoc()) {
						    	echo "<tr>";
						    	echo "<td>" . $row['event_ID'] . "</td>";
						    	echo "<td><a href=\"video_list.php?event_ID=" . $row['event_ID'] . "&event_name=" . $row['event_name'] . "\">" .  $row['event_name'] . "</a></td>";
						    	echo "<td>" . $row['event_info'] . "</td>";
						  		echo "</tr>";    
						    }
						} else {
						    echo "0 results";
						}

						echo "</table>";

						$conn->close();

						?>

						<br><br>
						<h3>Add a new Event:</h3>
						<form action="AddEvent.php" method="post">
						<label for="event_name">Event Name:</label><input type="text" name="event_name"><br>
						<label for="event_desc">Event Description:</label> 	<input type="text" name="event_desc"><br>
						<input type="submit">
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