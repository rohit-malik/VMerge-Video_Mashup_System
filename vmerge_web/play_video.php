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
									<h2>Mashup Video</h2>
								</header>

						
						<?php
							include('session.php');

							$event_name = $_GET['event_name'];
							$video_name = $_GET['video_name'];
						?>

						<h2>Playing Video:<h2>
							<div class="fit">
						<video width="100%" height="auto" controls>
						  	<source src="http://172.26.1.221/AndroidUploadImage/<?php echo $event_name; echo '/'; echo $video_name?>" type="video/mp4">
						  	Your browser does not support the video tag.
						</video>
						</div>

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
