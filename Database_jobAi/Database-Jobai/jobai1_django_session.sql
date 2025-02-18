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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('48dk64ju6ahlbg3nw7chae0skb2sz5c8','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiEOU:fxg233xPAWthmW7cWtbxs7gXC8E2G4hutm0aYo-A4KQ','2025-02-26 15:11:18.163174'),('5mr6igumt46d03eapcuva56q6ssgrkhe','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiEkZ:DdSuGD79kUjBv3D-E80LmG2Y3_Y4dMv5N-FGC2lmTU0','2025-02-26 15:34:07.547801'),('63981l066c12ihcqdjpucnu0m504m6as','eyJjb21wYW55X2lkIjoxLCJjb21wYW55X25hbWUiOiJJbmZvc3lzIn0:1tirci:x2RD97HEYQA2o2fZNjidG-S-Ss24zxVTExhto8ZG2Z8','2025-02-28 09:04:36.538895'),('7kzhasyaee9lo4iqtlfuuilgbg49k6ld','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiFUr:geLqK5mmRCimz3sqqQyMfgMZXLawlnGZAJXm3hA9ysY','2025-02-26 16:21:57.013405'),('7om0mnfyb0j7m4yb02pq0ho1pq4i4495','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tjKsI:a7a9DDHnkBLQk-CtFaYYiXWv2TBokmV3tWKf-W6AGRk','2025-03-01 16:18:38.957131'),('an3va2akmuonmhb98s2cs8xuidnm4pgi','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tjHyi:ZuuPfJ_thWfHwRhm0V5LUkxSS7hVvlfk01lrF3dvOb4','2025-03-01 13:13:04.385625'),('ce1nv2epeg8c5purkph5s5cndfcw4yj3','eyJjb21wYW55X2lkIjoxLCJjb21wYW55X25hbWUiOiJJbmZvc3lzIn0:1tiDvr:f7U72RT-vL-TloKPnZpNLQakXdbnmijPfPh3SJYbbMA','2025-02-26 14:41:43.914720'),('i2yw4j5dlcsk30qmpw20svo999ruarcv','eyJjb21wYW55X2lkIjoxLCJjb21wYW55X25hbWUiOiJJbmZvc3lzIn0:1tiqYQ:cF34MD7AdIka2R0C5sV1Xz-JtwE1tJgXuvo-qqU_uGk','2025-02-28 07:56:06.649883'),('jpsta7egvvede53wewea7xfz8tvmh71v','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiEtZ:GY78pfipi6-GfcPOHTcVR3ZcDxygGN6ELS-Y9IZhl7g','2025-02-26 15:43:25.567034'),('jvzcjag4spls4fq6wz64wxeycj2uzdor','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiF6M:UkQWWtap3gzs6WYdSyNKtbG6ri0yRRI3CmAcCUnvawk','2025-02-26 15:56:38.891638'),('nflno6zfb9bf1x34d96vsphtclwakpcf','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tjZwv:gxq6T6zWJ1INEVoHjKZQqxsd_RXAWAJGQCSievwaCjc','2025-03-02 08:24:25.920611'),('ojosbp4b0egudqmea07mqnqmgck5g9dj','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tj7mL:AE2ndkzhul9zb9y1NBpKRKUZESa9jHXbmp09te0N0VU','2025-03-01 02:19:37.855881'),('oufknuh4bdle5jgeuiotbnuxspf7azeq','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tjZrl:T8vjKsaQteuzXDQ9Wq3kuLYf9o6wtS5zGMYHQF4nJWs','2025-03-02 08:19:05.428921'),('pj0pj5v56ffrhckzt700ay3e50wsl309','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tjI7m:5rEXdtlEqVAzRlQFWGjz8fpNf8qJ5ohaLw8rp5z75gY','2025-03-01 13:22:26.243709'),('pmxanexhvms9q6auwal7eh0m331huw1d','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiFDV:yQI_uHbd1VCm8mNmT9B6z9o_kEMg2a4zNeOvxVpUtVc','2025-02-26 16:04:01.903686'),('q87tfq2gw8bxli66xzo7nof04czes997','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiETo:hUXcZ_UI_W7_tRafwKlqTUIf7LnkswauuuiUSYrHEYA','2025-02-26 15:16:48.905052'),('xbipu7ep7ysd367uoqbc0z204bo00z8p','eyJjb21wYW55X2lkIjoyLCJjb21wYW55X25hbWUiOiJUQVRBIENPTlNVTFRJTkcgU0VSVklDRVMifQ:1tj6RB:te2VcxxlvmGTOuZZSJq62oREUOErjgUnF5Tutimi4CY','2025-03-01 00:53:41.628149'),('yp6eajqi2zdgmor0ne0pol0lgx0ne4io','.eJxVjc0OgjAQhF-F7LmYUqgaTnoULr6BWexGt_aHFDwQ47tbbnicmW9mPmDjMBG9KN0CeoIWOlwwoS264srOIYPYMGyg1VuDPLLLLYvLu1L16bHq3T36v9r4jGHdPujjvm6UrmSO0ZhE05TtPs5zfvWip4QOxSUYxkyYOORUNeV5TOxKJaWC7w9dBTpq:1tjzHF:NXiJcsOdhgA0JUb7WIbHuw8N_8w4DWZ7-VF-7I9_bE4','2025-03-03 11:27:05.387651'),('yvfdngdxe1r8ywzg2ec8v87ikf2owscv','.eJyrVsrKTypOTc1OLYrPS8xNVbJSCigqTckoz1QISsxS0kGSzkxRsjJEFkjNTczMAWoogGgoSszKdkgHiekl5-cq1QIA2UYgxw:1tiFLp:EMLjPa1Di8A596qmX9meVDlMIdGutX9TXk0f4-d0T0E','2025-02-26 16:12:37.005413');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-17 19:20:13
