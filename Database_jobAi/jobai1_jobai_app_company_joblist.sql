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
-- Table structure for table `jobai_app_company_joblist`
--

DROP TABLE IF EXISTS `jobai_app_company_joblist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobai_app_company_joblist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `job_title_id` bigint NOT NULL,
  `job_number` varchar(100) NOT NULL,
  `job_description` varchar(5000) DEFAULT NULL,
  `job_type` varchar(255) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `highest_qualification` varchar(255) DEFAULT NULL,
  `skills_required` longtext,
  `dateofpublish` date DEFAULT NULL,
  `Lastdate` date DEFAULT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `JobAi_App_company_jo_company_id_5afbe075_fk_JobAi_App` (`company_id`),
  KEY `JobAi_App_company_joblist_job_title_id_5b3f377e` (`job_title_id`),
  CONSTRAINT `JobAi_App_company_jo_company_id_5afbe075_fk_JobAi_App` FOREIGN KEY (`company_id`) REFERENCES `jobai_app_company` (`id`),
  CONSTRAINT `JobAi_App_company_jo_job_title_id_5b3f377e_fk_JobAi_App` FOREIGN KEY (`job_title_id`) REFERENCES `jobai_app_job_title` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_company_joblist`
--

LOCK TABLES `jobai_app_company_joblist` WRITE;
/*!40000 ALTER TABLE `jobai_app_company_joblist` DISABLE KEYS */;
INSERT INTO `jobai_app_company_joblist` VALUES (1,2,'1000220','-','Full Time','Bangalore,Karnataka','BE/Btech CSE ,MCA,Mtech CSE','Python,HTML,CSS,JavaScript,Django','2025-02-18','2025-05-15',6),(2,5,'1000227','-','Part Time','Kochi,Kerala,India','BE/Btech CSE ,MCA,Mtech CSE','Python,Redhat Course Certification','2025-02-19','2025-05-15',1),(4,5,'1000224','-','Full Time','Kochi,Kerala,India','MCA, Btech CSE','Java,MySQL/Any other Databases','2025-02-18','2025-04-23',2),(5,1,'1000229','-','Full Time','Bangalore,Karnataka','BE/Btech CSE , MCA, Mtech CSE','Python,HTML,CSS,JavaScript,Django','2025-02-19','2025-06-26',1),(6,7,'123456','-','Full Time','Hyderabad,Andhra Pradesh,India','BE/Btech CSE ,MCA,Mtech CSE','Python Jupyter/Anaconda,MySQL/Any other Databases,Knowledge in ML','2025-02-19','2025-05-28',1);
/*!40000 ALTER TABLE `jobai_app_company_joblist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-19 21:53:26
