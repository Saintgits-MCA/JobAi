-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: jobai1
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jobai_app_jobseeker_profile`
--

DROP TABLE IF EXISTS `jobai_app_jobseeker_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobai_app_jobseeker_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `highest_qualification` varchar(255) DEFAULT NULL,
  `job_preference` varchar(255) DEFAULT NULL,
  `university` varchar(255) DEFAULT NULL,
  `address` longtext,
  `skills` longtext,
  `resume` varchar(100) DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  `profile_img` varchar(100) DEFAULT NULL,
  `percentage` longtext,
  `passoutyear` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_jobseeker_profile`
--

LOCK TABLES `jobai_app_jobseeker_profile` WRITE;
/*!40000 ALTER TABLE `jobai_app_jobseeker_profile` DISABLE KEYS */;
INSERT INTO `jobai_app_jobseeker_profile` VALUES (1,'Aslam Salam','aslamsalam3491@gmail.com','623508419','2002-01-09','MCA','FullStack Developer','A P J Abdulkalam Technological University','Lakulathu Thazchayil, Kuttapuzha P O Thiruvalla, Kerala, 689103','CSS, Django, Git, HTML, Java, JavaScript, Python, React, SQL','documents/ASLAM-SALAM-FlowCV-Resume-20250112_2.docx',4,'images/aslam_salam.jpeg','84.1%','2025'),(2,'Prudhwi Raj','prudhwirajk@gmail.com','9562766835','2002-04-24','Integrated MCA','Django Developer','Saintgits College Of Engineering(Autonomous),Kottayam, Kerala','Kottayam ,Kerala Pin:686502','CSS, Git, HTML, Java, Python, SQL','documents/Prudhwi_Raj_Krishna_V_CV.docx',1,'images/Prudhwi_Raj.jpg','85.7%','2025'),(3,'Janna Gardner','jannagardner@gmail.com','9576628123','2002-01-18','MCA','Database  Analyst','A P J Abdul Kalam Technological University, Kerala','Ance Villa,Kochi,Kerala,India','CSS, HTML, Python, SQL','documents/Janna_Gardner.docx',6,'images/janna-gardner.jpeg','60%','2025'),(4,'Jayaraj J Pillai','jayaraj.inmca2025@saintgits.org','8586342510','2002-06-24','Integrated MCA','Cyber Security Analyst','Saintgits College of Engineering (Autonomous), Kottayam','Vallamkulam P.O Thiruvalla Pathanamthitta Kerala','C++, CSS, Django, Git, HTML, Java, JavaScript, Python, SQL','documents/Jayaraj_J_Pillai_resume.docx',3,'images/jayaraj.jpeg','80.7%','2025');
/*!40000 ALTER TABLE `jobai_app_jobseeker_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-18  8:17:22
