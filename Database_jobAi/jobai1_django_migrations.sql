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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-02-10 09:09:15.661686'),(2,'auth','0001_initial','2025-02-10 09:09:17.185697'),(3,'JobAi_App','0001_initial','2025-02-10 09:09:17.249680'),(4,'JobAi_App','0002_resumedetails_usersettings','2025-02-10 09:09:17.590735'),(5,'JobAi_App','0003_company','2025-02-10 09:09:17.849444'),(6,'JobAi_App','0004_remove_company_created_at_remove_company_user','2025-02-10 09:09:18.176324'),(7,'JobAi_App','0005_jobseeker_registration_delete_usersettings','2025-02-10 09:09:18.313798'),(8,'JobAi_App','0006_jobseeker_registration_name','2025-02-10 09:09:18.409740'),(9,'JobAi_App','0007_jobseeker_profile','2025-02-10 09:09:18.446215'),(10,'JobAi_App','0008_company_type_master_jobseeker_resume_and_more','2025-02-10 09:09:18.550742'),(11,'JobAi_App','0009_company_company_type','2025-02-10 09:09:18.643279'),(12,'admin','0001_initial','2025-02-10 09:09:18.913119'),(13,'admin','0002_logentry_remove_auto_add','2025-02-10 09:09:18.943112'),(14,'admin','0003_logentry_add_action_flag_choices','2025-02-10 09:09:18.985033'),(15,'contenttypes','0002_remove_content_type_name','2025-02-10 09:09:19.255078'),(16,'auth','0002_alter_permission_name_max_length','2025-02-10 09:09:19.410636'),(17,'auth','0003_alter_user_email_max_length','2025-02-10 09:09:19.488407'),(18,'auth','0004_alter_user_username_opts','2025-02-10 09:09:19.510201'),(19,'auth','0005_alter_user_last_login_null','2025-02-10 09:09:19.634723'),(20,'auth','0006_require_contenttypes_0002','2025-02-10 09:09:19.639825'),(21,'auth','0007_alter_validators_add_error_messages','2025-02-10 09:09:19.664475'),(22,'auth','0008_alter_user_username_max_length','2025-02-10 09:09:19.795139'),(23,'auth','0009_alter_user_last_name_max_length','2025-02-10 09:09:19.980830'),(24,'auth','0010_alter_group_name_max_length','2025-02-10 09:09:20.079591'),(25,'auth','0011_update_proxy_permissions','2025-02-10 09:09:20.130223'),(26,'auth','0012_alter_user_first_name_max_length','2025-02-10 09:09:20.315824'),(27,'sessions','0001_initial','2025-02-10 09:09:20.394752'),(28,'JobAi_App','0010_company_jobs','2025-02-12 09:19:17.398403'),(29,'JobAi_App','0011_company_jobs_company_id','2025-02-12 09:35:02.856958'),(30,'JobAi_App','0012_company_jobs_job_type_and_more','2025-02-12 10:03:09.425685'),(31,'JobAi_App','0013_company_joblist_delete_company_jobs','2025-02-12 10:12:44.092911'),(32,'JobAi_App','0014_remove_company_joblist_salary_and_more','2025-02-12 10:25:43.806550'),(33,'JobAi_App','0015_alter_company_joblist_job_number_and_more','2025-02-14 02:37:57.750552'),(34,'JobAi_App','0016_rename_company_id_company_joblist_company','2025-02-14 06:27:34.651494'),(35,'JobAi_App','0017_jobseeker_profile_user','2025-02-14 10:34:24.914569'),(36,'JobAi_App','0018_jobseeker_registration_phone','2025-02-17 05:07:12.550055'),(37,'JobAi_App','0019_jobseeker_resume_user','2025-02-17 11:35:31.505079'),(38,'JobAi_App','0020_alter_jobseeker_resume_user','2025-02-17 11:42:11.647698'),(39,'JobAi_App','0021_job_title','2025-02-18 01:39:18.567586'),(40,'JobAi_App','0022_alter_company_joblist_job_title','2025-02-18 01:43:54.283568'),(41,'JobAi_App','0023_jobseeker_profile_profile_img','2025-02-19 07:17:55.092553'),(42,'JobAi_App','0024_company_profile_img','2025-02-19 07:49:09.555990'),(43,'JobAi_App','0025_remove_company_profile_img','2025-02-19 11:45:22.288569'),(44,'JobAi_App','0026_company_profile_img','2025-02-19 11:45:40.505358'),(45,'JobAi_App','0027_jobseeker_registration_last_login','2025-02-22 07:57:31.220265'),(46,'JobAi_App','0028_jobapplication','2025-02-25 05:14:03.568707'),(47,'JobAi_App','0029_rename_job_jobapplication_company_joblist_and_more','2025-02-25 07:24:28.799109'),(48,'JobAi_App','0030_company_joblist_percent_criteria_and_more','2025-03-07 01:30:03.980932'),(49,'JobAi_App','0031_jobseeker_profile_passoutyear','2025-03-07 02:54:20.454497'),(50,'JobAi_App','0032_alter_jobseeker_profile_dob','2025-03-07 03:59:08.463534'),(51,'JobAi_App','0033_alter_jobseeker_profile_dob','2025-03-07 03:59:08.478705'),(52,'JobAi_App','0034_jobnotification','2025-03-09 04:53:08.014007'),(53,'JobAi_App','0035_delete_resumedetails','2025-03-10 09:52:53.119198'),(54,'JobAi_App','0036_rename_jobseeker_jobnotification_jobseeker_profile','2025-03-12 06:31:13.783894'),(55,'JobAi_App','0037_jobapplication_status','2025-03-13 10:25:37.536325'),(56,'JobAi_App','0038_alter_jobapplication_status','2025-03-13 10:28:19.901872'),(57,'JobAi_App','0038_remove_jobapplication_status','2025-03-13 10:32:45.445747'),(58,'JobAi_App','0039_jobapplication_status','2025-03-13 10:33:00.239856'),(59,'JobAi_App','0040_remove_company_joblist_job_number','2025-03-17 06:47:17.224207');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
