-- MySQL dump 10.13  Distrib 5.6.26, for osx10.8 (x86_64)
--
-- Host: localhost    Database: twss
-- ------------------------------------------------------
-- Server version	5.6.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `TWSS_Class`
--

DROP TABLE IF EXISTS `TWSS_Class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_Class` (
  `id` varchar(8) NOT NULL,
  `name` varchar(16) NOT NULL,
  `grade` int(11) NOT NULL,
  `sum` int(11) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TWSS_Class_teacher_id_84f509db_fk_TWSS_User_id` (`teacher_id`),
  KEY `TWSS_Class_department_id_f09db38c_fk_TWSS_Department_id` (`department_id`),
  CONSTRAINT `TWSS_Class_department_id_f09db38c_fk_TWSS_Department_id` FOREIGN KEY (`department_id`) REFERENCES `TWSS_Department` (`id`),
  CONSTRAINT `TWSS_Class_teacher_id_84f509db_fk_TWSS_User_id` FOREIGN KEY (`teacher_id`) REFERENCES `TWSS_User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_Class`
--

LOCK TABLES `TWSS_Class` WRITE;
/*!40000 ALTER TABLE `TWSS_Class` DISABLE KEYS */;
INSERT INTO `TWSS_Class` VALUES ('20160101','2016生物工程1班',2016,50,'20160000004',1),('20160102','2016生物工程2班',2016,50,'20160000001',1),('20160104','2016生物工程3班',2016,50,'20160000004',1),('20160201','2016生物技术1班',2016,50,'20160000004',2),('20160202','2016生物技术2班',2016,50,'20160000004',2),('20160203','2016生物技术3班',2016,50,'20160000004',2),('20160301','2016生物信息1班',2016,50,'20160000004',3),('20160302','2016生物信息2班',2016,50,'20160000004',3);
/*!40000 ALTER TABLE `TWSS_Class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_CompetitionGuide`
--

DROP TABLE IF EXISTS `TWSS_CompetitionGuide`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_CompetitionGuide` (
  `id` varchar(16) NOT NULL,
  `students` varchar(32) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `level` varchar(64) NOT NULL,
  `name` varchar(128) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `type` varchar(16) NOT NULL,
  `rank` varchar(4),
  `department_id` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TWSS_CompetitionGuide_teacher_id_2692248f_fk_TWSS_User_id` (`teacher_id`),
  CONSTRAINT `TWSS_CompetitionGuide_teacher_id_2692248f_fk_TWSS_User_id` FOREIGN KEY (`teacher_id`) REFERENCES `TWSS_User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_CompetitionGuide`
--

LOCK TABLES `TWSS_CompetitionGuide` WRITE;
/*!40000 ALTER TABLE `TWSS_CompetitionGuide` DISABLE KEYS */;
INSERT INTO `TWSS_CompetitionGuide` VALUES ('000000001','学生A,学生C,学生F,学生G',0,'特等','XXXXX竞赛','20160000001','全国性大学生学科竞赛',' ',1,1,2017,NULL),('000000002','学生B',0,'一等','XXXXX竞赛','20160000001','省部级大学生竞赛',' ',1,2,2017,NULL),('1504997985','学生B',2,'特等','新增竞赛','20160000001','全国性大学生学科竞赛',' ',1,2,2017,NULL),('1504997999','学生H',0,'二等','新增竞赛','20160000001','省部级大学生竞赛',' ',1,2,2017,NULL);
/*!40000 ALTER TABLE `TWSS_CompetitionGuide` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_Department`
--

DROP TABLE IF EXISTS `TWSS_Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_Department` (
  `id` int(11) NOT NULL,
  `name` varchar(8) NOT NULL,
  `head_of_department` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_Department`
--

LOCK TABLES `TWSS_Department` WRITE;
/*!40000 ALTER TABLE `TWSS_Department` DISABLE KEYS */;
INSERT INTO `TWSS_Department` VALUES (1,'生物工程','20160000001'),(2,'生物技术','20160000002'),(3,'生物信息','20160000003');
/*!40000 ALTER TABLE `TWSS_Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_ExperimentCourse`
--

DROP TABLE IF EXISTS `TWSS_ExperimentCourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_ExperimentCourse` (
  `id` varchar(16) NOT NULL,
  `name` varchar(32) NOT NULL,
  `year` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `classes` varchar(128) NOT NULL,
  `student_sum` int(11) NOT NULL,
  `period` int(11) NOT NULL,
  `credit` int(11) NOT NULL,
  `attribute` int(11) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  KEY `TWSS_ExperimentCours_department_id_5d72a899_fk_TWSS_Depa` (`department_id`),
  KEY `TWSS_ExperimentCourse_teacher_id_3f8acd88` (`teacher_id`),
  CONSTRAINT `TWSS_ExperimentCours_department_id_5d72a899_fk_TWSS_Depa` FOREIGN KEY (`department_id`) REFERENCES `TWSS_Department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_ExperimentCourse`
--

LOCK TABLES `TWSS_ExperimentCourse` WRITE;
/*!40000 ALTER TABLE `TWSS_ExperimentCourse` DISABLE KEYS */;
INSERT INTO `TWSS_ExperimentCourse` VALUES ('474399','解剖小白鼠',2017,1,'20160201,20160202,20160203,',150,6,2,1,0,1,'20160000001',NULL),('463839','发酵啤酒',2017,1,'20160101,20160102,',100,4,1,1,0,1,'20160000001',NULL);
/*!40000 ALTER TABLE `TWSS_ExperimentCourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_GlobalValue`
--

DROP TABLE IF EXISTS `TWSS_GlobalValue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_GlobalValue` (
  `key` varchar(32) NOT NULL,
  `value` varchar(32) DEFAULT NULL,
  `comment` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_GlobalValue`
--

LOCK TABLES `TWSS_GlobalValue` WRITE;
/*!40000 ALTER TABLE `TWSS_GlobalValue` DISABLE KEYS */;
INSERT INTO `TWSS_GlobalValue` VALUES ('current_semester','1','当前学期'),('current_year','2017','当前学年');
/*!40000 ALTER TABLE `TWSS_GlobalValue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_PaperGuide`
--

DROP TABLE IF EXISTS `TWSS_PaperGuide`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_PaperGuide` (
  `id` varchar(16) NOT NULL,
  `author` varchar(16) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `level` varchar(64) NOT NULL,
  `name` varchar(128) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `type` varchar(16) NOT NULL,
  `rank` varchar(4),
  `department_id` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TWSS_PaperGuide_teacher_id_895e3807_fk_TWSS_User_id` (`teacher_id`),
  CONSTRAINT `TWSS_PaperGuide_teacher_id_895e3807_fk_TWSS_User_id` FOREIGN KEY (`teacher_id`) REFERENCES `TWSS_User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_PaperGuide`
--

LOCK TABLES `TWSS_PaperGuide` WRITE;
/*!40000 ALTER TABLE `TWSS_PaperGuide` DISABLE KEYS */;
INSERT INTO `TWSS_PaperGuide` VALUES ('000001','学生A',0,'SCI','关于XXXXXX的论文','20160000001','未记录',' ',1,2,2017,NULL),('1504998017','学生Z',0,'一般期刊','新增论文','20160000001','未记录',' ',1,1,2017,NULL);
/*!40000 ALTER TABLE `TWSS_PaperGuide` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_PraticeCourse`
--

DROP TABLE IF EXISTS `TWSS_PraticeCourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_PraticeCourse` (
  `id` varchar(16) NOT NULL,
  `name` varchar(32) NOT NULL,
  `year` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `classes` varchar(128) NOT NULL,
  `student_sum` int(11) NOT NULL,
  `period` int(11) NOT NULL,
  `credit` int(11) NOT NULL,
  `attribute` int(11) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `department_id` int(11) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  KEY `TWSS_PraticeCourse_department_id_5d52e473_fk_TWSS_Department_id` (`department_id`),
  KEY `TWSS_PraticeCourse_teacher_id_4a42fd85` (`teacher_id`),
  CONSTRAINT `TWSS_PraticeCourse_department_id_5d52e473_fk_TWSS_Department_id` FOREIGN KEY (`department_id`) REFERENCES `TWSS_Department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_PraticeCourse`
--

LOCK TABLES `TWSS_PraticeCourse` WRITE;
/*!40000 ALTER TABLE `TWSS_PraticeCourse` DISABLE KEYS */;
INSERT INTO `TWSS_PraticeCourse` VALUES ('476666','生信华农实习',2017,1,'20160301,20160302,',100,24,3,1,2,'20160000001',1,NULL),('476667','生技野外实习',2017,1,'20160201,20160202,20160203,',150,6,1,1,0,'20160000001',1,NULL);
/*!40000 ALTER TABLE `TWSS_PraticeCourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_TeachingAchievement`
--

DROP TABLE IF EXISTS `TWSS_TeachingAchievement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_TeachingAchievement` (
  `id` varchar(16) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `name` varchar(128) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `level` varchar(64) NOT NULL,
  `type` varchar(16) NOT NULL,
  `rank` varchar(4),
  `department_id` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TWSS_TeachingAchievement_teacher_id_8c25eecf_fk_TWSS_User_id` (`teacher_id`),
  CONSTRAINT `TWSS_TeachingAchievement_teacher_id_8c25eecf_fk_TWSS_User_id` FOREIGN KEY (`teacher_id`) REFERENCES `TWSS_User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_TeachingAchievement`
--

LOCK TABLES `TWSS_TeachingAchievement` WRITE;
/*!40000 ALTER TABLE `TWSS_TeachingAchievement` DISABLE KEYS */;
INSERT INTO `TWSS_TeachingAchievement` VALUES ('00000000',0,'基于Web的教师工作量统计系统的设计与实现','20160000001','核心期刊','教研论文',' ',1,1,2017,NULL),('00000001',2,'基于Web的教师工作量统计系统的设计与实现','20160000001','国家级','教改项目结项',' ',1,1,2017,NULL),('00000002',0,'基于Web的教师工作量统计系统的设计与实现','20160000001','国家级','教学成果','一等',1,2,2017,NULL),('00000004',0,'基于Web的教师工作量统计系统的设计与实现','20160000001','全国统编教材、国家级规划教材、全国教学专业指导委员会指定教材、全国优秀教材','教材',' ',1,2,2017,NULL),('00000005',1,'基于Web的教师工作量统计系统的设计与实现','20160000001','其他正式出版教材','教材',' ',1,1,2016,NULL),('00000006',0,'基于Web的教师工作量统计系统的设计与实现','20160000001','其他正式出版教材','教材',' ',1,2,2017,NULL),('00000007',0,'基于Web的教师工作量统计系统的设计与实现','20160000001','国家级','教学成果',' ',1,2,2017,NULL),('00000008',2,'基于Web的教师工作量统计系统的设计与实现','20160000001','国家级','教学成果','一等',1,2,2017,NULL),('1504987803',2,'新增教研论文1','20160000001','核心期刊','教研论文',' ',1,1,2017,NULL),('1504988167',1,'新增教改项目2','20160000001','国家级','教改项目结项',' ',1,2,2016,NULL),('1504988189',0,'新增教学成果','20160000001','省部级','教学成果',' ',1,1,2017,NULL),('1504989230',1,'新增教研论文0','20160000001','一般期刊','教研论文',' ',1,2,2017,NULL),('1504989319',0,'新增教改项目','20160000002','核心期刊','教改项目结项',' ',1,1,2017,NULL),('1504989331',2,'新增教改项目','20160000001','核心期刊','教改项目结项',' ',1,2,2016,NULL),('1505137434',0,'新增教研论文666','20160000001','一般期刊','教研论文',' ',1,2,2017,NULL);
/*!40000 ALTER TABLE `TWSS_TeachingAchievement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_TeachingProject`
--

DROP TABLE IF EXISTS `TWSS_TeachingProject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_TeachingProject` (
  `id` varchar(16) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `level` varchar(64) NOT NULL,
  `name` varchar(128) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `type` varchar(16) NOT NULL,
  `rank` varchar(4),
  `department_id` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TWSS_TeachingProject_teacher_id_224b4a49_fk_TWSS_User_id` (`teacher_id`),
  CONSTRAINT `TWSS_TeachingProject_teacher_id_224b4a49_fk_TWSS_User_id` FOREIGN KEY (`teacher_id`) REFERENCES `TWSS_User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_TeachingProject`
--

LOCK TABLES `TWSS_TeachingProject` WRITE;
/*!40000 ALTER TABLE `TWSS_TeachingProject` DISABLE KEYS */;
INSERT INTO `TWSS_TeachingProject` VALUES ('00000001',2,'省部级','基于Web的教师工作量统计系统的设计与实现','20160000001','专业、团队及实验中心类',' ',1,1,2017,NULL),('00000002',1,'省部级','基于Web的教师工作量统计系统的设计与实现','20160000001','课程类',' ',1,2,2017,NULL),('00000003',2,'国家级','基于Web的教师工作量统计系统的设计与实现','20160000001','工程实践教育类',' ',1,1,2017,NULL),('00000004',0,'省部级','基于Web的教师工作量统计系统的设计与实现','20160000001','教学名师',' ',1,2,2017,NULL),('00000005',1,'省部级','基于Web的教师工作量统计系统的设计与实现','20160000001','大学生创新创业训练',' ',1,2,2016,NULL),('1504991012',2,'国家级','新增专业、团队及实验中心类','20160000001','专业、团队及实验中心类',' ',1,1,2017,NULL),('1504991044',0,'国家级','新增教学名师','20160000001','教学名师',' ',1,1,2017,NULL),('1505137636',0,'校级','新增教学项目666','20160000001','课程类',' ',1,2,2017,NULL);
/*!40000 ALTER TABLE `TWSS_TeachingProject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_TheoryCourse`
--

DROP TABLE IF EXISTS `TWSS_TheoryCourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_TheoryCourse` (
  `id` varchar(16) NOT NULL,
  `name` varchar(32) NOT NULL,
  `year` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `classes` varchar(128) NOT NULL,
  `student_sum` int(11) NOT NULL,
  `period` int(11) NOT NULL,
  `credit` int(11) NOT NULL,
  `attribute` int(11) NOT NULL,
  `audit_status` int(11) NOT NULL,
  `teacher_id` varchar(16) NOT NULL,
  `department_id` int(11) NOT NULL,
  `reject_reason` varchar(128) DEFAULT NULL,
  KEY `TWSS_TheoryCourse_department_id_78769f56_fk_TWSS_Department_id` (`department_id`),
  KEY `TWSS_TheoryCourse_teacher_id_33b2fabe` (`teacher_id`),
  CONSTRAINT `TWSS_TheoryCourse_department_id_78769f56_fk_TWSS_Department_id` FOREIGN KEY (`department_id`) REFERENCES `TWSS_Department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_TheoryCourse`
--

LOCK TABLES `TWSS_TheoryCourse` WRITE;
/*!40000 ALTER TABLE `TWSS_TheoryCourse` DISABLE KEYS */;
INSERT INTO `TWSS_TheoryCourse` VALUES ('470001','微积分A',2017,1,'20160301,20160302,',100,36,5,1,2,'20160000001',1,NULL),('470002','微积分B',2017,2,'20160201,20160202,20160203,',150,32,5,1,2,'20160000001',1,NULL),('470003','微积分B',2016,1,'20160101,20160102,',100,34,5,1,0,'20160000001',1,NULL),('463728','生物化学',2017,1,'20160301,20160302,',100,30,4,1,0,'20160000001',1,NULL);
/*!40000 ALTER TABLE `TWSS_TheoryCourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TWSS_User`
--

DROP TABLE IF EXISTS `TWSS_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TWSS_User` (
  `id` varchar(16) NOT NULL,
  `name` varchar(16) NOT NULL,
  `title` varchar(16) NOT NULL,
  `status` varchar(16) NOT NULL,
  `password` varchar(32) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `email` varchar(32) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TWSS_User_department_id_53b6c127_fk_TWSS_Department_id` (`department_id`),
  CONSTRAINT `TWSS_User_department_id_53b6c127_fk_TWSS_Department_id` FOREIGN KEY (`department_id`) REFERENCES `TWSS_Department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TWSS_User`
--

LOCK TABLES `TWSS_User` WRITE;
/*!40000 ALTER TABLE `TWSS_User` DISABLE KEYS */;
INSERT INTO `TWSS_User` VALUES ('20160000001','教师A','教授','教师,系主任,教务员','d820e68d6feed0eeb70dfe0873083c98','18012345678','18012345678@zzu.edu',1),('20160000002','教师B','教授','教师,系主任','3fb53bee6b17ea134ea174c8f6c03316','18012345678','18012345678@zzu.edu',2),('20160000003','教师C','教授','教师,系主任','bc45ba006918401167376632a8ab115e','18012345678','18012345678@zzu.edu',3),('20160000004','教师D','教授','教师','c7f4a8c56b9c57cc921eec3572763dd9','18012345678','18012345678@zzu.edu',1);
/*!40000 ALTER TABLE `TWSS_User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add class',7,'add_class'),(20,'Can change class',7,'change_class'),(21,'Can delete class',7,'delete_class'),(22,'Can add competition guide',8,'add_competitionguide'),(23,'Can change competition guide',8,'change_competitionguide'),(24,'Can delete competition guide',8,'delete_competitionguide'),(25,'Can add department',9,'add_department'),(26,'Can change department',9,'change_department'),(27,'Can delete department',9,'delete_department'),(28,'Can add paper guide',10,'add_paperguide'),(29,'Can change paper guide',10,'change_paperguide'),(30,'Can delete paper guide',10,'delete_paperguide'),(31,'Can add pratice course',11,'add_praticecourse'),(32,'Can change pratice course',11,'change_praticecourse'),(33,'Can delete pratice course',11,'delete_praticecourse'),(34,'Can add teaching achievement',12,'add_teachingachievement'),(35,'Can change teaching achievement',12,'change_teachingachievement'),(36,'Can delete teaching achievement',12,'delete_teachingachievement'),(37,'Can add teaching project',13,'add_teachingproject'),(38,'Can change teaching project',13,'change_teachingproject'),(39,'Can delete teaching project',13,'delete_teachingproject'),(40,'Can add theory course',14,'add_theorycourse'),(41,'Can change theory course',14,'change_theorycourse'),(42,'Can delete theory course',14,'delete_theorycourse'),(43,'Can add user',15,'add_user'),(44,'Can change user',15,'change_user'),(45,'Can delete user',15,'delete_user'),(46,'Can add experiment course',16,'add_experimentcourse'),(47,'Can change experiment course',16,'change_experimentcourse'),(48,'Can delete experiment course',16,'delete_experimentcourse'),(49,'Can add global value',17,'add_globalvalue'),(50,'Can change global value',17,'change_globalvalue'),(51,'Can delete global value',17,'delete_globalvalue');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'project','class'),(8,'project','competitionguide'),(9,'project','department'),(16,'project','experimentcourse'),(17,'project','globalvalue'),(10,'project','paperguide'),(11,'project','praticecourse'),(12,'project','teachingachievement'),(13,'project','teachingproject'),(14,'project','theorycourse'),(15,'project','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-09-08 10:51:01.060187'),(2,'auth','0001_initial','2017-09-08 10:51:01.468752'),(3,'admin','0001_initial','2017-09-08 10:51:01.559493'),(4,'admin','0002_logentry_remove_auto_add','2017-09-08 10:51:01.595985'),(5,'contenttypes','0002_remove_content_type_name','2017-09-08 10:51:01.707275'),(6,'auth','0002_alter_permission_name_max_length','2017-09-08 10:51:01.750269'),(7,'auth','0003_alter_user_email_max_length','2017-09-08 10:51:01.791041'),(8,'auth','0004_alter_user_username_opts','2017-09-08 10:51:01.811111'),(9,'auth','0005_alter_user_last_login_null','2017-09-08 10:51:01.853162'),(10,'auth','0006_require_contenttypes_0002','2017-09-08 10:51:01.857145'),(11,'auth','0007_alter_validators_add_error_messages','2017-09-08 10:51:01.879481'),(12,'auth','0008_alter_user_username_max_length','2017-09-08 10:51:01.927919'),(13,'project','0001_initial','2017-09-08 10:51:02.611376'),(14,'sessions','0001_initial','2017-09-08 10:51:02.649967'),(15,'project','0002_auto_20170908_1919','2017-09-08 11:19:49.482753'),(16,'project','0003_auto_20170908_1932','2017-09-08 11:32:31.693065'),(17,'project','0004_auto_20170908_1932','2017-09-08 11:32:31.730234'),(18,'project','0002_class_department','2017-09-08 14:03:57.092760'),(19,'project','0003_auto_20170909_0123','2017-09-08 17:23:20.296478'),(20,'project','0004_experimentcourse','2017-09-08 17:36:59.577016'),(21,'project','0005_auto_20170909_0320','2017-09-08 19:23:20.465299'),(22,'project','0002_praticecourse_other_teacher_num','2017-09-08 19:25:18.691391'),(23,'project','0003_auto_20170909_0326','2017-09-08 19:26:54.585316'),(24,'project','0004_auto_20170909_0331','2017-09-08 19:32:01.287542'),(25,'project','0005_remove_praticecourse_other_teacher_num','2017-09-08 19:33:48.314769'),(26,'project','0002_auto_20170909_0448','2017-09-08 20:48:59.787685'),(27,'project','0002_auto_20170909_1629','2017-09-09 08:29:11.436508'),(28,'project','0003_auto_20170909_1633','2017-09-09 08:33:02.486707'),(29,'project','0004_auto_20170909_1637','2017-09-09 08:37:45.508816'),(30,'project','0005_auto_20170909_1643','2017-09-09 08:43:38.880340'),(31,'project','0006_auto_20170909_1645','2017-09-09 08:45:23.902247'),(32,'project','0007_auto_20170909_1645','2017-09-09 08:45:49.904122'),(33,'project','0008_auto_20170909_1647','2017-09-09 08:47:04.788982'),(34,'project','0009_auto_20170909_1647','2017-09-09 08:47:20.447476'),(35,'project','0002_auto_20170909_1702','2017-09-09 09:02:26.392582'),(36,'project','0003_auto_20170909_1702','2017-09-09 09:03:00.520957'),(37,'project','0002_auto_20170909_1724','2017-09-09 09:24:20.391542'),(38,'project','0002_auto_20170909_2222','2017-09-09 14:22:59.147414'),(39,'project','0003_auto_20170909_2253','2017-09-09 14:53:57.100134'),(40,'project','0004_auto_20170909_2255','2017-09-09 14:55:45.594882'),(41,'project','0005_auto_20170909_2256','2017-09-09 14:56:20.996226'),(42,'project','0006_auto_20170909_2256','2017-09-09 14:56:30.417655'),(43,'project','0002_auto_20170910_0906','2017-09-10 01:06:54.939164'),(44,'project','0003_auto_20170910_0907','2017-09-10 01:07:36.612324'),(45,'project','0002_globalvalue','2017-09-11 02:12:35.500911'),(46,'project','0003_auto_20170911_1029','2017-09-11 02:32:53.248004'),(47,'project','0004_auto_20170911_1029','2017-09-11 02:32:53.270421'),(48,'project','0002_globalvalue_comment','2017-09-11 04:33:05.175601'),(49,'project','0002_auto_20170911_2045','2017-09-11 12:46:24.155389'),(50,'project','0003_auto_20170912_0349','2017-09-11 19:49:33.271701');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
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

-- Dump completed on 2017-09-14 19:44:48
