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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add uploaded file',7,'add_uploadedfile'),(26,'Can change uploaded file',7,'change_uploadedfile'),(27,'Can delete uploaded file',7,'delete_uploadedfile'),(28,'Can view uploaded file',7,'view_uploadedfile'),(29,'Can add resume details',8,'add_resumedetails'),(30,'Can change resume details',8,'change_resumedetails'),(31,'Can delete resume details',8,'delete_resumedetails'),(32,'Can view resume details',8,'view_resumedetails'),(33,'Can add company',9,'add_company'),(34,'Can change company',9,'change_company'),(35,'Can delete company',9,'delete_company'),(36,'Can view company',9,'view_company'),(37,'Can add jobseeker_ registration',10,'add_jobseeker_registration'),(38,'Can change jobseeker_ registration',10,'change_jobseeker_registration'),(39,'Can delete jobseeker_ registration',10,'delete_jobseeker_registration'),(40,'Can view jobseeker_ registration',10,'view_jobseeker_registration'),(41,'Can add jobseeker_profile',11,'add_jobseeker_profile'),(42,'Can change jobseeker_profile',11,'change_jobseeker_profile'),(43,'Can delete jobseeker_profile',11,'delete_jobseeker_profile'),(44,'Can view jobseeker_profile',11,'view_jobseeker_profile'),(45,'Can add company_ type_ master',12,'add_company_type_master'),(46,'Can change company_ type_ master',12,'change_company_type_master'),(47,'Can delete company_ type_ master',12,'delete_company_type_master'),(48,'Can view company_ type_ master',12,'view_company_type_master'),(49,'Can add jobseeker_resume',13,'add_jobseeker_resume'),(50,'Can change jobseeker_resume',13,'change_jobseeker_resume'),(51,'Can delete jobseeker_resume',13,'delete_jobseeker_resume'),(52,'Can view jobseeker_resume',13,'view_jobseeker_resume'),(53,'Can add company_jobs',14,'add_company_jobs'),(54,'Can change company_jobs',14,'change_company_jobs'),(55,'Can delete company_jobs',14,'delete_company_jobs'),(56,'Can view company_jobs',14,'view_company_jobs'),(57,'Can add company_joblist',15,'add_company_joblist'),(58,'Can change company_joblist',15,'change_company_joblist'),(59,'Can delete company_joblist',15,'delete_company_joblist'),(60,'Can view company_joblist',15,'view_company_joblist'),(61,'Can add job_title',16,'add_job_title'),(62,'Can change job_title',16,'change_job_title'),(63,'Can delete job_title',16,'delete_job_title'),(64,'Can view job_title',16,'view_job_title'),(65,'Can add job application',17,'add_jobapplication'),(66,'Can change job application',17,'change_jobapplication'),(67,'Can delete job application',17,'delete_jobapplication'),(68,'Can view job application',17,'view_jobapplication'),(69,'Can add job notification',18,'add_jobnotification'),(70,'Can change job notification',18,'change_jobnotification'),(71,'Can delete job notification',18,'delete_jobnotification'),(72,'Can view job notification',18,'view_jobnotification'),(73,'Can add company notification',19,'add_companynotification'),(74,'Can change company notification',19,'change_companynotification'),(75,'Can delete company notification',19,'delete_companynotification'),(76,'Can view company notification',19,'view_companynotification');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-23  8:26:59
