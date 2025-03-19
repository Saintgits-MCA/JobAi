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
-- Table structure for table `jobai_app_jobapplication`
--

DROP TABLE IF EXISTS `jobai_app_jobapplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobai_app_jobapplication` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `applied_at` datetime(6) NOT NULL,
  `company_joblist_id` bigint NOT NULL,
  `jobseeker_id` bigint NOT NULL,
  `status` longtext NOT NULL DEFAULT (_utf8mb3'Applied'),
  PRIMARY KEY (`id`),
  UNIQUE KEY `JobAi_App_jobapplication_jobseeker_id_job_id_00de0ef9_uniq` (`jobseeker_id`,`company_joblist_id`),
  KEY `JobAi_App_jobapplica_company_joblist_id_680959ed_fk_JobAi_App` (`company_joblist_id`),
  CONSTRAINT `JobAi_App_jobapplica_company_joblist_id_680959ed_fk_JobAi_App` FOREIGN KEY (`company_joblist_id`) REFERENCES `jobai_app_company_joblist` (`id`),
  CONSTRAINT `JobAi_App_jobapplica_jobseeker_id_06490689_fk_JobAi_App` FOREIGN KEY (`jobseeker_id`) REFERENCES `jobai_app_jobseeker_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_jobapplication`
--

LOCK TABLES `jobai_app_jobapplication` WRITE;
/*!40000 ALTER TABLE `jobai_app_jobapplication` DISABLE KEYS */;
INSERT INTO `jobai_app_jobapplication` VALUES (1,'2025-03-17 06:17:49.120463',2,2,'Applied'),(2,'2025-03-17 06:17:49.130604',14,2,'Applied'),(3,'2025-03-17 06:17:49.148733',3,2,'Applied'),(4,'2025-03-17 06:17:49.154236',12,2,'Applied'),(5,'2025-03-17 06:18:13.015994',1,2,'Applied'),(6,'2025-03-17 06:18:13.031990',6,2,'Applied'),(7,'2025-03-17 06:18:13.048463',9,2,'Applied'),(10,'2025-03-17 10:07:18.712750',3,4,'Applied'),(11,'2025-03-17 10:07:18.719446',12,4,'Applied'),(12,'2025-03-17 10:07:18.727209',2,4,'Applied'),(13,'2025-03-17 10:07:18.736057',14,4,'Applied');
/*!40000 ALTER TABLE `jobai_app_jobapplication` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-18  8:17:25
