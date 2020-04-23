-- MySQL dump 10.16  Distrib 10.1.30-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: vmerge
-- ------------------------------------------------------
-- Server version	10.1.30-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `event_ID` int(11) NOT NULL AUTO_INCREMENT,
  `event_name` varchar(200) NOT NULL,
  `event_info` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`event_ID`),
  UNIQUE KEY `UNIQUE` (`event_name`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (23,'Sugar','This event contains video clips of Song \"Sugar\" by Maroon 5'),(24,'River','This event contains video clips of Song \"River\" by Ed Sheeran and Eminem.'),(25,'bhangra','bhrigu lake'),(26,'suit','bhangra\n'),(27,'Zeitgeist','cultural event'),(28,'Sitar Metal Band','Performance clips of Sitar Metal Band Performance, Day 2 Zeitgeist');
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `user_type` varchar(20) NOT NULL DEFAULT 'user',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_id` (`email_id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,'ROHIT KUMAR','2016csb1055@iitrpr.ac.in','admin'),(7,'Sahil Gupta','2016csb1056@iitrpr.ac.in','admin'),(24,'AMIT KUMAR','2016eeb1070@iitrpr.ac.in','user'),(26,'Sahil Gupta','gupta.sahil436@gmail.com','admin'),(29,'ANUBHAV SAINI','anubhav.saini0@gmail.com','user'),(30,'MATTELA NITHISH','2016csb1042@iitrpr.ac.in','user'),(32,'YASH RANJAN','2016ceb1025@iitrpr.ac.in','user'),(33,'Ashish Dubey','2019eem1019@iitrpr.ac.in','user'),(34,'Shreyanshu Shekhar','shreyanshushekhar007@gmail.com','user'),(35,'piyush kumar','piyushkumar17101999@gmail.com','user'),(36,'DEVENDRA RAJ','2017eeb1136@iitrpr.ac.in','user'),(37,'Saurabh Jaiswal','saurabh.19csz0009@iitrpr.ac.in','user'),(41,'ANSHU KUMAR','2019csb1074@iitrpr.ac.in','user'),(47,'AVINASH KUMAR GUPTA','2016eeb1071@iitrpr.ac.in','user'),(48,'Shreyans Soni','2016csb1146@iitrpr.ac.in','user'),(52,'Yogita Saini','yogita@iitrpr.ac.in','user'),(53,'Saroj kumar','saroj.19mez0005@iitrpr.ac.in','user'),(55,'GURJOT SINGH','2019eeb1160@iitrpr.ac.in','user'),(56,'Nikhil Mahla','mahlanikhil007@gmail.com','user'),(57,'DARSHIT SULIYA','2019ceb1032@iitrpr.ac.in','user'),(58,'KULDEEP _','2018csm1014@iitrpr.ac.in','user'),(60,'Harshpreet Singh','harshpreetnishu096@gmail.com','user'),(61,'Jatin Gaur','2018eez0016@iitrpr.ac.in','user'),(62,'ANURAG MEENA','2019ceb1004@iitrpr.ac.in','user'),(63,'RAHUL KUMAR MEENA','2018meb1246@iitrpr.ac.in','user'),(64,'GURKIRPAL SINGH','2019csb1087@iitrpr.ac.in','user'),(66,'Anubhav Dogra','2016mez0019@iitrpr.ac.in','user'),(68,'Vusirikala Abhishek','abhishekvusirikala01052001@gmail.com','user'),(69,'Sangram Jagadale','sangramjagadale2017@gmail.com','user'),(70,'KAPIL DEV','2017csb1085@iitrpr.ac.in','user'),(71,'Shobhit Gupta','shobhitgupta907@gmail.com','user'),(72,'SURAJ BHAN MUNDOTIYA','2018mmb1296@iitrpr.ac.in','user'),(73,'Pvp Jerry','hellopvp17@gmail.com','user'),(74,'Abhishek Gupta','abhiigupta9934@gmail.com','user'),(75,'Mayank Singh','mayank.s090301@gmail.com','user'),(76,'Soumya Ranjan Panigrahi','2018eem1024@iitrpr.ac.in','user'),(77,'Md Danish Quamar','danishq.dakshana16@gmail.com','user'),(79,'JATIN GEHLOT','2018meb1231@iitrpr.ac.in','user'),(80,'Jaideep Singh','803jaideep@gmail.com','user'),(82,'LOVISH GARG','2019meb1273@iitrpr.ac.in','user'),(88,'','2019meb1260@iitrpr.ac.in','user'),(90,'chetan kumar','chetankumar20177@gmail.com','user'),(91,'2019eeb1137@iitrpr.ac.in','2019eeb1137@iitrpr.ac.in','user'),(92,'Amritpal S','amrit6928@gmail.com','user'),(95,'MD. ATHAR HASSAN','2019meb1278@iitrpr.ac.in','user'),(96,'Kajal Madaan','iamkajalmadaan@gmail.com','user'),(97,'NEMA RAM MEGHWAL','2019csb1101@iitrpr.ac.in','user'),(98,'Munish Garg','munishkumgarg@gmail.com','user'),(99,'Jatin Sachan','sachanjatin976@gmail.com','user'),(101,'Rohan Kumar','rohananindian@gmail.com','user');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `video` (
  `video_ID` int(11) NOT NULL AUTO_INCREMENT,
  `video_name` varchar(200) NOT NULL,
  `event_ID` int(11) NOT NULL,
  `video_desc` varchar(400) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`video_ID`) USING BTREE,
  UNIQUE KEY `video_name` (`video_name`,`video_desc`),
  KEY `event_ID` (`event_ID`),
  KEY `video_ibfk_2` (`user_id`),
  CONSTRAINT `video_ibfk_1` FOREIGN KEY (`event_ID`) REFERENCES `event` (`event_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `video_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_info` (`user_id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video`
--

LOCK TABLES `video` WRITE;
/*!40000 ALTER TABLE `video` DISABLE KEYS */;
INSERT INTO `video` VALUES (41,'VID_20191005_143955727.mp4',23,NULL,1),(42,'VID_20191005_143927020.mp4',23,NULL,1),(43,'V_20191005_143909_OC0.mp4',23,NULL,1),(44,'V_20191005_143944_OC0.mp4',23,NULL,1),(45,'VID_20191005_171219681.mp4',24,NULL,1),(46,'V_20191005_171140_OC0.mp4',24,NULL,1),(47,'V_20191005_171207_OC0.mp4',24,NULL,1),(48,'V_20191005_171234_OC0.mp4',24,NULL,1),(49,'VID_20191005_171149434.mp4',24,NULL,1),(50,'VID_20191006_150408254.mp4',25,NULL,1),(51,'V_20191006_150403_OC0.mp4',25,NULL,1),(52,'VID_20191006_150444229.mp4',25,NULL,1),(53,'V_20191006_150432_OC0.mp4',25,NULL,1),(54,'VID_20191006_150444229.mp4',25,NULL,1),(55,'V_20191006_153428_OC0.mp4',26,NULL,1),(56,'V_20191006_153352_OC0.mp4',26,NULL,1),(57,'VID_20191006_153410215.mp4',26,NULL,1),(58,'VID_20191006_153348876.mp4',26,NULL,1),(60,'20191010_211357.mp4',27,NULL,37),(61,'VID_20191012_185302.mp4',27,NULL,57),(62,'video_20191012_214035.mp4',27,NULL,60),(63,'video_20191012_222517.mp4',27,NULL,60),(64,'VID_20191012_140201.mp4',27,NULL,80);
/*!40000 ALTER TABLE `video` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-02 23:13:10
