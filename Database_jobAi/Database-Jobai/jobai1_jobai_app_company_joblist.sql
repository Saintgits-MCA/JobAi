CREATE DATABASE  IF NOT EXISTS `jobai1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `jobai1`;
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
  `job_title` varchar(100) DEFAULT NULL,
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
  CONSTRAINT `JobAi_App_company_jo_company_id_5afbe075_fk_JobAi_App` FOREIGN KEY (`company_id`) REFERENCES `jobai_app_company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_company_joblist`
--

LOCK TABLES `jobai_app_company_joblist` WRITE;
/*!40000 ALTER TABLE `jobai_app_company_joblist` DISABLE KEYS */;
INSERT INTO `jobai_app_company_joblist` VALUES (1,'Django Full Stack','1000229','-','Part Time','Kochi,Kerala,India','[\'BE/Btech CSE , MCA, Mtech CSE\']','[\'Python,HTML,CSS,JavaScript,Django\']','2025-02-17','2025-03-07',1),(2,'FullStack Web Developer','1400226','-','Full time','Remote','[\'BE/Btech CSE , MCA,Msc Computer Science\']','[\'Python,HTML,CSS,JavaScript,Django,Flutter,Reactjs,nodejs,Php\']','2025-02-16','2025-04-25',2),(3,'Android App Developer','1000221','-','Full time','Remote','[\'BE/Btech CSE , MCA\']','[\'Java,Android,MySQL\']','2025-02-16','2025-06-30',2),(5,'Security Analysts','13245663','-','Full Time','Thiruvananthapuram,Kerala,India','[\'BE/Btech CSE ,MCA,Mtech CSE\']','[\'Python,Redhat Course Certification\']','2025-02-17','2025-05-29',1);
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

-- Dump completed on 2025-02-17 19:20:11
