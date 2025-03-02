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
  PRIMARY KEY (`id`),
  UNIQUE KEY `JobAi_App_jobapplication_jobseeker_id_job_id_00de0ef9_uniq` (`jobseeker_id`,`company_joblist_id`),
  KEY `JobAi_App_jobapplica_company_joblist_id_680959ed_fk_JobAi_App` (`company_joblist_id`),
  CONSTRAINT `JobAi_App_jobapplica_company_joblist_id_680959ed_fk_JobAi_App` FOREIGN KEY (`company_joblist_id`) REFERENCES `jobai_app_company_joblist` (`id`),
  CONSTRAINT `JobAi_App_jobapplica_jobseeker_id_06490689_fk_JobAi_App` FOREIGN KEY (`jobseeker_id`) REFERENCES `jobai_app_jobseeker_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_jobapplication`
--

LOCK TABLES `jobai_app_jobapplication` WRITE;
/*!40000 ALTER TABLE `jobai_app_jobapplication` DISABLE KEYS */;
INSERT INTO `jobai_app_jobapplication` VALUES (5,'2025-02-28 06:15:35.140829',2,1),(6,'2025-02-28 06:15:35.147701',3,1),(7,'2025-02-28 06:15:35.150823',10,1),(8,'2025-02-28 06:15:35.155158',8,1),(9,'2025-02-28 06:16:05.439463',7,1),(10,'2025-03-01 00:52:55.928023',2,5),(11,'2025-03-01 00:52:55.933818',3,5),(12,'2025-03-01 00:52:55.942062',10,5);
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

-- Dump completed on 2025-03-01  7:24:24
