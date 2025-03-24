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
  `job_description` varchar(12000) DEFAULT NULL,
  `job_type` varchar(255) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `highest_qualification` varchar(255) DEFAULT NULL,
  `percent_criteria` longtext,
  `skills_required` longtext,
  `dateofpublish` date DEFAULT NULL,
  `Lastdate` date DEFAULT NULL,
  `company_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `JobAi_App_company_jo_company_id_5afbe075_fk_JobAi_App` (`company_id`),
  KEY `JobAi_App_company_joblist_job_title_id_5b3f377e` (`job_title_id`),
  CONSTRAINT `JobAi_App_company_jo_company_id_5afbe075_fk_JobAi_App` FOREIGN KEY (`company_id`) REFERENCES `jobai_app_company` (`id`),
  CONSTRAINT `JobAi_App_company_jo_job_title_id_5b3f377e_fk_JobAi_App` FOREIGN KEY (`job_title_id`) REFERENCES `jobai_app_job_title` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobai_app_company_joblist`
--

LOCK TABLES `jobai_app_company_joblist` WRITE;
/*!40000 ALTER TABLE `jobai_app_company_joblist` DISABLE KEYS */;
INSERT INTO `jobai_app_company_joblist` VALUES (1,3,'Job opening for .NET, Visual Basic, and SQL developers with a strong academic background. Suitable for candidates with BTech CSE, MCA, or Integrated MCA.','Part Time','Hyderabad,Bangalore','Btech CSE,MCA,Integrated MCA','70%','.NET, Visual Basic ,SQL','2025-03-12','2025-07-01',6),(2,1,'Django Developer – Infosys\n\nInfosys is looking for a skilled Django Developer to join our dynamic team. The ideal candidate is an Integrated MCA Graduate with strong proficiency in Python, HTML, CSS, and GitHub, along with excellent communication skills.\n\nResponsibilities:\nDevelop and maintain web applications using Django and Python.\nCollaborate with cross-functional teams to integrate front-end and back-end systems.\nWork with databases and APIs for efficient data management.\nEnsure application security and performance optimization.\nRequirements:\nStrong programming skills in Python and Java.\nExperience with HTML, CSS, and GitHub for version control.\nKnowledge of databases and SQL (IBM certified).\nExposure to object detection, automation projects (Raspberry Pi, Arduino) is a plus.\nEnthusiastic about problem-solving, web development, and cybersecurity.\nInfosys provides a growth-oriented environment where innovation is encouraged. Apply now and be a part of our cutting-edge technology team!','Full Time','Kochi,Thiruvananthapuram,Kozhikode','Integrated MCA,MCA','70%','Python,HTML,CSS','2025-03-14','2025-05-29',1),(3,3,'Job opportunity for .NET, Visual Basic, and SQL developers. Seeking candidates with MCA or Integrated MCA qualifications.','Full Time','Thiruvananthapuram,Kochi','MCA,Integrated MCA','60%','.NET, Visual Basic ,SQL','2025-02-28','2025-04-29',3),(4,3,'Hiring .NET, Visual Basic, and SQL developers for a full-time role. Candidates with BE/BTech CSE qualification preferred.','Full Time','Bangalore,Kochi','BE/Btech CSE','70%','.NET, Visual Basic ,SQL','2025-03-06','2025-06-26',1),(5,7,'Job opening for Python and ML professionals. Candidates with experience in Python, Jupyter/Anaconda, MySQL, and Machine Learning preferred.','Full Time','Hyderabad','BE/Btech CSE, Integrated MCA,MCA','60%','Python ,MySQL, or Any other Databases,ML','2025-03-21','2025-05-28',1),(8,5,'Hiring Java developers with a strong academic background. Seeking candidates with a BTech CSE degree.','Full Time','Bangalore','Btech CSE','80%','Java','2025-02-24','2025-04-25',7),(9,7,'Opportunity for full-stack developers proficient in multiple web and scripting languages, including HTML, CSS, JavaScript, Node.js, React, Python, and Angular.js.','Full Time','Kochi,Bangalore,Trivandrum','Btech CSE,MCA,Integrated MCA','60%','HTML,CSS,JavaScript,Nodejs,React,Python,Angularjs','2025-03-20','2025-11-28',2),(12,2,'Full-time role for front-end and back-end developers with expertise in HTML, CSS, JavaScript, Node.js, React, Python, and Angular.js.','Full Time','Delhi,Bangalore','Btech CSE,MCA,Integrated MCA','70%','HTML,CSS,JavaScript,Nodejs,React,Python,Angularjs','2025-03-12','2025-05-27',6),(13,6,'Part-time opportunity for web developers proficient in front-end technologies such as HTML, CSS, JavaScript, Node.js, and React.js.','Part Time','Delhi,Bangalore,Kolkata ','Btech CSE,MCA,Integrated MCA','70%','HTML,CSS,JavaScript,Nodejs,React','2025-03-12','2025-03-11',2),(14,1,'Full-time hiring for developers with expertise in HTML, CSS, JavaScript, Node.js, React, Python, and Angular.js. Open positions available in Hyderabad and Bangalore.','Full Time','Hyderabad,Bangalore','Btech CSE,MCA,Integrated MCA','70%','HTML,CSS,JavaScript,Nodejs,React,Python,Angularjs','2025-03-13','2025-05-30',9),(22,2,'-','Full Time','Kottayam ','MCA,Integrated MCA','70%','HTML,CSS,JavaScript,Nodejs,React,Python,Angularjs','2025-03-20','2025-03-31',2),(23,8,'Job Title: MERN Stack Developer\r\nCompany: Nfosys\r\n\r\nJob Description:\r\nWe are seeking a skilled MERN Stack Developer to join our dynamic team at Nfosys. You will be responsible for designing, developing, and maintaining full-stack web applications using MongoDB, Express.js, React.js, and Node.js. Your role includes writing clean, scalable code, implementing RESTful APIs, optimizing database performance, and ensuring responsive UI/UX.\r\n\r\nResponsibilities:\r\n\r\nDevelop and maintain scalable web applications using MERN Stack.\r\nImplement RESTful APIs and integrate third-party services.\r\nOptimize front-end performance and ensure cross-browser compatibility.\r\nCollaborate with designers and backend teams for seamless development.\r\nTroubleshoot, debug, and enhance application performance.\r\nRequirements:\r\n\r\nProficiency in MongoDB, Express.js, React.js, Node.js, Python.\r\nExperience with REST APIs, Git, and cloud platforms.\r\nStrong problem-solving skills and attention to detail.','Full Time','Delhi,Bangalore,Kolkata ','Integrated MCA,MCA','80%','HTML,CSS,JavaScript,Nodejs,Reactjs,SQL','2025-03-21','2025-06-30',1);
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

-- Dump completed on 2025-03-23  8:27:04
