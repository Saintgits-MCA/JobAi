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
  `ats_score` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `JobAi_App_jobapplication_jobseeker_id_job_id_00de0ef9_uniq` (`jobseeker_id`,`company_joblist_id`),
  KEY `JobAi_App_jobapplica_company_joblist_id_680959ed_fk_JobAi_App` (`company_joblist_id`),
  CONSTRAINT `JobAi_App_jobapplica_company_joblist_id_680959ed_fk_JobAi_App` FOREIGN KEY (`company_joblist_id`) REFERENCES `jobai_app_company_joblist` (`id`),
  CONSTRAINT `JobAi_App_jobapplica_jobseeker_id_06490689_fk_JobAi_App` FOREIGN KEY (`jobseeker_id`) REFERENCES `jobai_app_jobseeker_profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_jobapplication`
--

LOCK TABLES `jobai_app_jobapplication` WRITE;
/*!40000 ALTER TABLE `jobai_app_jobapplication` DISABLE KEYS */;
INSERT INTO `jobai_app_jobapplication` VALUES (1,'2025-03-17 06:17:49.120463',2,2,'Accepted',62),(2,'2025-03-17 06:17:49.130604',14,2,'Applied',NULL),(3,'2025-03-17 06:17:49.148733',3,2,'Rejected',NULL),(4,'2025-03-17 06:17:49.154236',12,2,'Rejected',NULL),(5,'2025-03-17 06:18:13.015994',1,2,'Rejected',NULL),(7,'2025-03-17 06:18:13.048463',9,2,'Rejected',NULL),(10,'2025-03-17 10:07:18.712750',3,4,'Rejected',NULL),(11,'2025-03-17 10:07:18.719446',12,4,'Applied',NULL),(12,'2025-03-17 10:07:18.727209',2,4,'Rejected',1),(13,'2025-03-17 10:07:18.736057',14,4,'Applied',NULL),(21,'2025-03-20 10:52:00.926407',22,2,'Accepted',NULL),(22,'2025-03-21 02:26:08.066529',22,4,'Applied',NULL),(23,'2025-03-21 02:26:08.095149',1,4,'Applied',NULL),(25,'2025-03-21 02:26:08.110274',9,4,'Applied',NULL),(26,'2025-03-21 04:55:13.021709',5,2,'Rejected',38),(27,'2025-03-21 05:01:54.574742',23,2,'Rejected',38),(28,'2025-03-21 05:03:56.956286',5,4,'Accepted',55),(29,'2025-03-21 05:03:56.973750',23,4,'Rejected',35),(43,'2025-03-21 05:13:59.002433',22,1,'Applied',NULL),(44,'2025-03-21 05:13:59.008606',12,1,'Applied',NULL),(45,'2025-03-21 05:13:59.016642',3,1,'Applied',NULL),(46,'2025-03-21 05:13:59.021896',5,1,'Accepted',55),(47,'2025-03-21 05:15:43.982362',2,1,'Rejected',1),(48,'2025-03-21 05:15:43.992671',14,1,'Applied',NULL),(49,'2025-03-21 05:15:43.999232',23,1,'Accepted',55),(50,'2025-03-21 05:15:44.005813',1,1,'Applied',NULL);
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

-- Dump completed on 2025-03-23  8:27:08
