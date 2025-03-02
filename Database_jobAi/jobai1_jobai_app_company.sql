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
-- Table structure for table `jobai_app_company`
--

DROP TABLE IF EXISTS `jobai_app_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobai_app_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  `company_type_id` bigint NOT NULL,
  `profile_img` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `JobAi_App_company_company_type_id_8745eff7_fk_JobAi_App` (`company_type_id`),
  CONSTRAINT `JobAi_App_company_company_type_id_8745eff7_fk_JobAi_App` FOREIGN KEY (`company_type_id`) REFERENCES `jobai_app_company_type_master` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_company`
--

LOCK TABLES `jobai_app_company` WRITE;
/*!40000 ALTER TABLE `jobai_app_company` DISABLE KEYS */;
INSERT INTO `jobai_app_company` VALUES (1,'admin','Infosys','admin@infosys.org','Thiruvananthapuram,Kerala,India',1,'company_images/infosys.jpg'),(2,'admin','TATA CONSULTING SERVICES','admin@tcs.org','Thiruvananthapuram,Kerala,India',1,'company_images/tcs-logo1.jpg'),(3,'admin@hcl','HCL Technologies','admin@hcl.org','Bangalore,Karnataka,India',2,'company_images/hcl.jpeg'),(6,'admin','Cognizant','admin@cognizant.org','Kochi,Kerala,India',1,'company_images/cognizant.jpg'),(7,'admin','6D Technologies','admin@6d.org','Kochi,Kerala,India',3,'company_images/images.jpeg'),(8,'admin@tecknohow','Tecknohow Solutions','tecknohow.132@gmail.com','Kottayam,Kerala,India',2,'company_images/company_profile.jpg');
/*!40000 ALTER TABLE `jobai_app_company` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-01  7:24:32
