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
-- Table structure for table `jobai_app_jobnotification`
--

DROP TABLE IF EXISTS `jobai_app_jobnotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobai_app_jobnotification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `company_job_id` bigint NOT NULL,
  `jobseeker_profile_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `JobAi_App_jobnotific_company_job_id_4e386625_fk_JobAi_App` (`company_job_id`),
  KEY `JobAi_App_jobnotific_jobseeker_profile_id_3d5a7004_fk_JobAi_App` (`jobseeker_profile_id`),
  CONSTRAINT `JobAi_App_jobnotific_company_job_id_4e386625_fk_JobAi_App` FOREIGN KEY (`company_job_id`) REFERENCES `jobai_app_company_joblist` (`id`),
  CONSTRAINT `JobAi_App_jobnotific_jobseeker_profile_id_3d5a7004_fk_JobAi_App` FOREIGN KEY (`jobseeker_profile_id`) REFERENCES `jobai_app_jobseeker_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_jobnotification`
--

LOCK TABLES `jobai_app_jobnotification` WRITE;
/*!40000 ALTER TABLE `jobai_app_jobnotification` DISABLE KEYS */;
INSERT INTO `jobai_app_jobnotification` VALUES (1,'New job posted: Django Developer at Amazon India Pvt Ltd.',0,'2025-03-13 05:46:03.906596',14,1),(2,'New job posted: Django Developer at Amazon India Pvt Ltd.',0,'2025-03-13 05:46:03.919396',14,2),(3,'New job posted: Django Developer at Amazon India Pvt Ltd.',0,'2025-03-13 05:46:03.929337',14,3),(4,'New job posted: Django Developer at Amazon India Pvt Ltd.',0,'2025-03-13 05:46:03.929337',14,4);
/*!40000 ALTER TABLE `jobai_app_jobnotification` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-18  8:17:26
