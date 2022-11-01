-- MySQL dump 10.13  Distrib 5.7.39, for Linux (x86_64)
--
-- Host: localhost    Database: PHI
-- ------------------------------------------------------
-- Server version	5.7.39-0ubuntu0.18.04.2-log

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
-- Table structure for table `acx_answer`
--

DROP TABLE IF EXISTS `acx_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acx_answer` (
  `answerID` int(11) NOT NULL AUTO_INCREMENT,
  `answerType` varchar(255) NOT NULL,
  `answerSetDate` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL,
  `questionSurvey_id` int(11) NOT NULL,
  `answerAdditional` varchar(255) NOT NULL,
  `answerMain` varchar(255) NOT NULL,
  PRIMARY KEY (`answerID`),
  UNIQUE KEY `acx_answer_questionSurvey_id_author_id_597e6bcc_uniq` (`questionSurvey_id`,`author_id`),
  KEY `acx_answer_author_id_2680ffcc_fk_auth_user_id` (`author_id`),
  CONSTRAINT `acx_answer_author_id_2680ffcc_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `acx_answer_questionSurvey_id_91267e47_fk_acx_surve` FOREIGN KEY (`questionSurvey_id`) REFERENCES `acx_surveyquestion` (`surveyQuestionID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acx_answer`
--

LOCK TABLES `acx_answer` WRITE;
/*!40000 ALTER TABLE `acx_answer` DISABLE KEYS */;
INSERT INTO `acx_answer` VALUES (1,'none','2022-06-15 18:52:37.057337',3,3,'Additional Info','YES'),(2,'none1','2022-06-15 19:00:31.416341',3,4,'Additional Info','YES'),(5,'1','2022-06-15 19:45:31.667030',3,7,'--','YES'),(7,'1','2022-06-15 19:57:35.070172',3,9,'--','10'),(8,'1','2022-06-15 20:32:58.292753',5,3,'--','YES'),(9,'1','2022-06-16 11:39:07.526069',3,10,'immediate','1'),(10,'none','2022-06-16 11:47:11.847001',3,11,'--','YES'),(11,'1','2022-06-21 20:02:06.654770',3,26,'--','YES'),(12,'1','2022-06-21 20:03:30.338622',3,27,'--','YES'),(13,'1','2022-06-21 20:03:47.854479',3,28,'--','YES'),(14,'1','2022-06-21 20:04:45.997353',3,29,'--','YES'),(16,'1','2022-06-21 20:05:56.101994',5,29,'--','YES'),(17,'1','2022-06-21 20:10:19.422764',3,31,'--','YES'),(18,'1','2022-06-21 20:10:49.405860',5,32,'--','YES'),(19,'1','2022-06-21 20:12:04.307800',7,31,'--','YES'),(20,'1','2022-06-24 04:24:09.183370',3,32,'--','YES'),(21,'1','2022-06-24 04:24:39.207920',3,35,'--','10'),(22,'1','2022-06-24 04:25:06.548529',3,36,'--','10');
/*!40000 ALTER TABLE `acx_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `acx_client`
--

DROP TABLE IF EXISTS `acx_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acx_client` (
  `clientID` int(11) NOT NULL AUTO_INCREMENT,
  `clientName` varchar(200) NOT NULL,
  `joinDate` datetime(6) NOT NULL,
  `streamSize` int(11) NOT NULL,
  `projectStatus` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `officialEmail` varchar(254) NOT NULL,
  `lastModified` datetime(6) NOT NULL,
  PRIMARY KEY (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acx_client`
--

LOCK TABLES `acx_client` WRITE;
/*!40000 ALTER TABLE `acx_client` DISABLE KEYS */;
INSERT INTO `acx_client` VALUES (2,'Solidere','2022-09-05 06:02:37.000000',1,5,'Alzorah developement client','Raadr@si.ae','2022-09-05 06:05:44.056444'),(3,'Roof Technology','2022-09-05 06:07:43.000000',1,4,'not materialized for project','joanne@reeftechnology.com','2022-09-05 06:08:19.133016'),(4,'HuffPuff Burger','2022-09-05 14:21:57.000000',1,0,'burgert place','ahmed@huffpuffburger.com','2022-09-05 14:22:32.481194'),(5,'Dubai Racing Club','2022-09-10 16:47:30.000000',3,0,'Mystery guest service for the DRC (Dubai Racing Club)','Omnia.Abdelgalil@dubairacingclub.com','2022-09-10 16:48:18.217192');
/*!40000 ALTER TABLE `acx_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `acx_question`
--

DROP TABLE IF EXISTS `acx_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acx_question` (
  `questionID` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `questionSetDate` datetime(6) NOT NULL,
  `section_id` int(11) NOT NULL,
  PRIMARY KEY (`questionID`),
  UNIQUE KEY `acx_question_question_section_id_e5224dcb_uniq` (`question`,`section_id`),
  KEY `acx_question_section_id_b958721a_fk_acx_section_sectionID` (`section_id`),
  CONSTRAINT `acx_question_section_id_b958721a_fk_acx_section_sectionID` FOREIGN KEY (`section_id`) REFERENCES `acx_section` (`sectionID`)
) ENGINE=InnoDB AUTO_INCREMENT=144 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acx_question`
--

LOCK TABLES `acx_question` WRITE;
/*!40000 ALTER TABLE `acx_question` DISABLE KEYS */;
INSERT INTO `acx_question` VALUES (1,'Valet Parking : Greeted properly ?','YES/NO','2022-06-15 13:09:00.773432',1),(2,'Valet Parking: Car doors opened','YES/NO','2022-06-15 13:13:52.291060',1),(4,'Valet Parking:  Were you offered assistance with your luggage?','YES/NO','2022-06-15 19:22:59.365490',1),(5,'Valet Parking:Hygiene of the valet parking','(1 to 10, 1 being the lowest expectation)','2022-06-15 19:23:29.778049',1),(6,'Valet Parking: Presentation of the Valet parking ticket','(1 to 10, 1 being the lowest expectation)','2022-06-15 19:33:40.229488',1),(7,'Valet Parking: Waiting Time','Waiting time in minutes','2022-06-16 11:06:39.745799',1),(8,'Valet Parking: Availability of Self-Park','YES/NO','2022-06-16 11:42:03.331937',1),(9,'Valet Parking: Parking Condition','provide condition (good/clean/spacious)','2022-06-16 19:19:21.236574',1),(10,'Check-in: Were the doors of the property opened by the bell boy','YES/NO','2022-06-16 19:19:58.143657',1),(11,'Check-in: Warm check in and welcoming','YES/NO','2022-06-16 19:20:24.264144',1),(12,'Check-in :Waiting time before being attended','(In minutes)','2022-06-16 19:21:03.495596',1),(13,'Check-in: Complimentary drink upon arrival','YES/NO','2022-06-16 19:21:31.575881',1),(14,'Check-in: Warm towel','YES/NO','2022-06-16 19:21:56.741850',1),(15,'Check-in: Explaining the hotel facility','(1 to 10, 1 being the lowest expectation)','2022-06-16 19:22:32.463281',1),(16,'Check-in: Payment handling if any at Check-in','YES/NO - but also provide additional info if any','2022-06-16 19:23:45.425854',1),(17,'Check-in: Presentation of Keys','(1 to 10, 1 being the lowest expectation)','2022-06-16 19:24:11.339039',1),(18,'Check-in: Number of keys','Number of keys given','2022-06-16 19:24:47.034237',1),(19,'check-in: Time-check till check-in is done','(In minutes)','2022-06-16 19:25:15.224988',1),(20,'Check-in: Assistance towards the elevator','YES/NO','2022-06-16 19:25:37.731050',1),(21,'CHeck-in: Accompany to room and explaining the room','YES/NO','2022-06-16 19:25:59.661802',1),(22,'Check-in: Luggage transfer to the room','YES/NO','2022-06-16 19:26:17.500910',1),(23,'Check-in: Luggage rack in clean condition','YES/NO','2022-06-16 19:26:40.358626',1),(24,'Check-out: Warm welcome','YES/NO','2022-06-16 19:28:02.367791',6),(25,'Check-out: Easy of checking-out','YES/NO','2022-06-16 19:28:27.757882',6),(26,'Check-out: Explaining the Bill','YES/NO','2022-06-16 19:28:51.118024',6),(27,'Check-out: Ease of Payment and proof of payemt','YES/NO','2022-06-16 19:29:14.712575',6),(28,'Check-out: Collection luggage','YES/NO','2022-06-16 19:29:33.012456',6),(29,'Check-out: Assistance towards the car','YES/NO','2022-06-16 19:29:51.795986',6),(30,'Check-out: Valet parking  (time stamp)','YES/NO','2022-06-16 19:30:14.131463',6),(32,'Rate The unveiling effect','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:25:44.048646',4),(33,'Rate The general aspect of the room','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:26:02.125259',4),(34,'Did the room feel clean when entering the room?','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:26:22.687009',4),(35,'Rate the general condition of the furniture','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:26:47.232028',4),(36,'Pictures and mirrors straight and dust free','YES/NO','2022-06-17 19:27:04.950982',4),(37,'Describe the smell of the room','(Written brief description)','2022-06-17 19:27:40.896426',4),(38,'Safe box ease of use and availability','YES/NO','2022-06-17 19:28:01.859477',4),(39,'Was the room dust free?','YES/NO','2022-06-17 19:28:18.042182',4),(40,'Was the room free from hair','YES/NO','2022-06-17 19:28:32.717658',4),(41,'Lamp Shades clean and straight','YES/NO','2022-06-17 19:29:16.201888',4),(42,'All Light bulbs functioning?','YES/NO','2022-06-17 19:29:32.137170',4),(43,'Curtains clean and straight','YES/NO','2022-06-17 19:29:46.298603',4),(44,'Furniture clean and upholstery in good condition','YES/NO','2022-06-17 19:30:05.975117',4),(45,'Furniture free from scratches','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:30:24.843973',4),(46,'Furniture drawers slide out easily?','YES/NO','2022-06-17 19:30:38.295661',4),(47,'Rate and describe the room amenities','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:31:01.508932',4),(48,'Size of the TV screen and working?','(brief description)','2022-06-17 19:31:26.935983',4),(49,'Bluetooth Sound system','YES/NO','2022-06-17 19:31:45.702019',4),(50,'Telephone clean and working','YES/NO','2022-06-17 19:32:01.788589',4),(51,'Rate the Availability of channels','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:32:15.084266',4),(52,'Walls clean and free from cobwebs in corners','YES/NO','2022-06-17 19:32:29.421746',4),(53,'Walls free from nicks and scratches','YES/NO','2022-06-17 19:32:45.899721',4),(54,'Room service Menu condition','YES/NO','2022-06-17 19:33:01.538900',4),(55,'Marketing collateral / Special events / up selling technique','YES/NO','2022-06-17 19:33:18.477599',4),(56,'Selection in Mini BAR','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:33:34.260382',4),(57,'Description Free condiments (Coffee, Tea, Espresso pods, water, Sugar, Sweet n Low, Brown sugar)','(Brief description)','2022-06-17 19:33:58.985118',4),(58,'Boiler status and espresso machine','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:35:48.191785',4),(59,'Rate the ease of use of central lighting system','(Brief description)','2022-06-17 19:36:11.253914',4),(60,'Doors working properly and sound?','YES/NO','2022-06-17 19:36:32.508466',4),(61,'Clean ashtrays','YES/NO','2022-06-17 19:36:46.457003',4),(62,'Controls of air-conditioning working properly','YES/NO','2022-06-17 19:37:00.860601',4),(63,'WIFI User friendliness level','(Brief description)','2022-06-17 19:37:25.313478',4),(64,'Everything in the room working perfectly / Comments','YES/NO','2022-06-17 19:37:39.999378',4),(65,'Soundproofing','YES/NO','2022-06-17 19:37:57.400658',4),(66,'Linen Clean and free from air and Hair','YES/NO','2022-06-17 19:38:12.078365',4),(67,'Fluffed and even pillows','YES/NO','2022-06-17 19:38:25.180384',4),(68,'Bed Status: Bed frame','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:39:00.794444',4),(69,'Bed Status: Bed base','(1 to 10, 1 being the lowest expectation)','2022-06-17 19:39:33.124356',4),(70,'Bed Status: Mattress','(Extra Firm, Firm, Plush, ultra-plush)','2022-06-17 19:40:02.653457',4),(71,'Bed Status: Mattress pad','YES/NO','2022-06-17 19:41:28.218154',4),(72,'Bed Status: Availability of different types of Pillows','YES/NO','2022-06-17 19:41:48.528960',4),(73,'Cabinet sanitization seal?','YES/NO','2022-06-17 19:44:51.789136',3),(74,'Clean Toilet seat','YES/NO','2022-06-17 19:45:05.826344',3),(75,'Underside of lavatory clean?','YES/NO','2022-06-17 19:45:22.000087',3),(76,'Shower rod in good condition','YES/NO','2022-06-17 19:45:35.716989',3),(77,'Toilet flushes correctly','YES/NO','2022-06-17 19:45:56.695405',3),(78,'Bathroom free of odors and noises','YES/NO','2022-06-17 19:46:15.894330',3),(79,'Shower curtain or glass curtain condition','YES/NO','2022-06-17 19:46:31.407414',3),(80,'Shower head description and option of rain shower','YES/NO','2022-06-17 19:46:51.342033',3),(81,'Water spots in tiles','YES/NO','2022-06-17 19:47:04.083119',3),(82,'Shower or tub free of grout','YES/NO','2022-06-17 19:47:18.978551',3),(83,'General condition of the bathroom','YES/NO','2022-06-17 19:47:30.983599',3),(84,'Floors hair free?','YES/NO','2022-06-17 19:47:44.822642',3),(85,'Fresh supply of towels','YES/NO','2022-06-17 19:47:58.399809',3),(86,'Smell of towers and number of towels (Hand, Shower)','(Brief Description)','2022-06-17 19:48:26.571171',3),(87,'Shower mat','YES/NO','2022-06-17 19:48:47.680581',3),(88,'Softeness and description of towels','(Brief description)','2022-06-17 19:49:37.146414',3),(89,'Amenities availability and description','(Brief description)','2022-06-17 19:50:05.586692',3),(90,'Shampoos, soap, conditioner, Creams, Sunscreen, Mosquito Repellent. White Label or branded','(Brief Description)','2022-06-17 19:50:26.036796',3),(91,'Website status of the property','(Brief description)','2022-06-17 19:51:45.175909',5),(92,'Distance from a major airport','(Brief description)','2022-06-17 19:52:28.085926',5),(93,'Number of rooms, size of the room, number of elevators, number of buggies','(Brief Description)','2022-06-17 19:52:52.621778',5),(94,'Online reservation process (where applicable)','YES/NO','2022-06-17 19:53:08.464334',5),(95,'Staff greeting throughout the property','(Brief Deescription)','2022-06-17 19:53:32.248387',5),(96,'Staff apparel throughout the property','(Brief Description)','2022-06-17 19:53:49.964167',5),(97,'Restroom in general areas: Proximity','(brief description)','2022-06-17 19:54:51.884249',5),(98,'Restroom in general areas: Cleanliness','(Brief Description)','2022-06-17 19:55:18.318765',5),(99,'Restroom in general areas: Amenities','(Brief Description)','2022-06-17 19:55:57.909107',5),(100,'Concierge: Greeting','(Brief description)','2022-06-17 19:56:33.082681',5),(101,'Concierge: Helpfulness','(Brief description)','2022-06-17 19:57:07.715454',5),(102,'Concierge: Guidance','(Brief Description)','2022-06-17 19:57:37.157373',5),(103,'Concierge: Time-check for assistance','(Brief Description)','2022-06-17 19:57:58.102444',5),(104,'Room service: Time to pick up the phone','(in seconds)','2022-06-18 12:46:27.239995',5),(105,'Room service: Time-check for order to arrive','(In minutes)','2022-06-18 12:46:57.804268',5),(106,'Room service: Status of the order (check dining Checklist)','(Brief description)','2022-06-18 12:47:39.879251',5),(107,'Housekeeping:  Time to pick up the phone','(In seconds)','2022-06-18 12:48:20.583543',5),(108,'Housekeeping: Time-check for request to arrive','(In minutes)','2022-06-18 12:48:55.520256',5),(109,'Laundry service: Time to pick up the phone','(In seconds)','2022-06-18 12:50:09.668330',5),(110,'Laundry service: Time-check for pick up and drop off','(In minutes)','2022-06-18 12:51:01.031653',5),(111,'Laundry service:  Cleanliness','(1 to 10, 1 being the lowest expectation)','2022-06-18 12:51:43.472056',5),(112,'SPA:  Massage menu','(1 to 10, 1 being the lowest expectation)','2022-06-18 12:53:26.986229',5),(113,'SPA: Smell of the spa, Scent diffusion','(1 to 10, 1 being the lowest expectation)','2022-06-18 12:55:43.015544',5),(114,'SPA: Look and feel','(1 to 10, 1 being the lowest expectation)','2022-06-18 12:59:34.570906',5),(115,'SPA: Cleanliness of the massage rooms and treatment rooms','(1 to 10, 1 being the lowest expectation)','2022-06-18 13:01:41.855314',5),(116,'SPA: Lighting','(1 to 10, 1 being the lowest expectation)','2022-06-18 13:04:05.346305',5),(117,'SPA: Music','(1 to 10, 1 being the lowest expectation)','2022-06-18 13:04:28.819125',5),(118,'SPA:  The use of essential oils','(1 to 10, 1 being the lowest expectation)','2022-06-18 13:04:57.782961',5),(119,'SPA:  Satisfaction and comfort level','(1 to 10, 1 being the lowest expectation)','2022-06-18 13:06:12.208978',5),(120,'Pool: General condition of the pool','(1-10)','2022-06-18 13:10:08.661595',5),(121,'Pool: Pool side cleanliness','(1-10)','2022-06-18 13:10:31.691683',5),(122,'Pool: Towels at poolside','(1-10)','2022-06-18 13:11:41.938857',5),(123,'Pool: Pool side slippers','(1-10)','2022-06-18 13:12:06.242135',5),(124,'Pool:  Color of the water','(1-10)','2022-06-18 13:12:26.045074',5),(125,'Pool:  Smell level of Chlorine','1-10','2022-06-18 13:12:41.967926',5),(126,'Pool: Beach side','(1-10)','2022-06-18 13:13:03.262296',5),(127,'Pool: Beach side: Status of sand','(Brief Description)','2022-06-18 13:13:43.282644',5),(128,'Pool: Beach side: Debris free','YES/NO','2022-06-18 13:14:07.702707',5),(129,'Pool: Pool lounge chairs: Working properly','YES/NO','2022-06-18 13:16:17.422111',5),(130,'Pool: Pool lounge chairs: Stains','YES/NO','2022-06-18 13:16:47.199150',5),(131,'Pool: Pool lounge chairs: Upholstery - if available','(Brief Description)','2022-06-22 10:52:47.989279',5),(132,'Pool: Pool lounge chairs: Comfort Level','(Brief Description)','2022-06-22 10:54:35.004422',5),(133,'Hallways, Elevator and Lobby: Lobby Decor','(Brief Description)','2022-06-22 10:55:51.514928',5),(134,'Hallways, Elevator and Lobby: Lobby seating area','(1 to 10, 1 being the lowest expectation)','2022-06-22 10:56:27.011465',5),(135,'Hallways, Elevator and Lobby: Smell','(1 to 10, 1 being the lowest expectation)','2022-06-22 10:57:34.915669',5),(136,'Hallways, Elevator and Lobby: Availability of business center: Printing services','YES/NO','2022-06-22 11:03:04.747471',5),(137,'Hallways, Elevator and Lobby: Furniture: Stains','YES/NO','2022-06-22 11:03:49.406138',5),(138,'Hallways, Elevator and Lobby: Furniture: Dust','YES/NO','2022-06-22 11:04:15.586343',5),(139,'Hallways, Elevator and Lobby: Furniture: Scratches','YES/NO','2022-06-22 11:04:42.436017',5),(140,'Hallways, Elevator and Lobby: Furniture: Upholstery condition','(1 to 10, 1 being the lowest expectation)','2022-06-22 11:05:26.587335',5),(141,'Cash integrity test','(Brief Description)','2022-06-22 11:05:54.101454',5),(142,'Left behind Belongings','(Brief Description)','2022-06-22 11:06:15.719868',5),(143,'Problem solving case and attending a special need','(Brief Description)','2022-06-22 11:06:31.859285',5);
/*!40000 ALTER TABLE `acx_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `acx_section`
--

DROP TABLE IF EXISTS `acx_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acx_section` (
  `sectionID` int(11) NOT NULL AUTO_INCREMENT,
  `sectionName` varchar(200) NOT NULL,
  `sectionDescription` longtext NOT NULL,
  `sectionSetDate` datetime(6) NOT NULL,
  `survey` varchar(200) NOT NULL,
  PRIMARY KEY (`sectionID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acx_section`
--

LOCK TABLES `acx_section` WRITE;
/*!40000 ALTER TABLE `acx_section` DISABLE KEYS */;
INSERT INTO `acx_section` VALUES (1,'Arrival','Arrival section of evaluation','2022-06-15 13:08:16.449376','1'),(2,'Shop floor','describes the shop floor','2022-06-15 19:02:54.063504','1'),(3,'Bathroom','Bathroom Area of hotel','2022-06-16 11:03:29.066091','1'),(4,'Room','hotel room area','2022-06-16 11:37:30.353183','1'),(5,'General areas and services','The hotel general areas and common places indoor and outdoor','2022-06-16 11:43:23.084114','1'),(6,'Departure','Departure section of the hotel','2022-06-16 19:27:37.640816','1'),(7,'Restaurant','restaurant section of survey','2022-06-24 08:06:56.206179','2');
/*!40000 ALTER TABLE `acx_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `acx_survey`
--

DROP TABLE IF EXISTS `acx_survey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acx_survey` (
  `surveyID` int(11) NOT NULL AUTO_INCREMENT,
  `surveyName` varchar(200) NOT NULL,
  `surveyDescription` longtext NOT NULL,
  `surveySetDate` datetime(6) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`surveyID`),
  KEY `acx_survey_client_id_2564b783_fk_acx_client_clientID` (`client_id`),
  CONSTRAINT `acx_survey_client_id_2564b783_fk_acx_client_clientID` FOREIGN KEY (`client_id`) REFERENCES `acx_client` (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acx_survey`
--

LOCK TABLES `acx_survey` WRITE;
/*!40000 ALTER TABLE `acx_survey` DISABLE KEYS */;
INSERT INTO `acx_survey` VALUES (1,'Mystery Guest Survey','Mystery guest survey for hotels and properties','2022-06-15 13:05:57.771418',2),(2,'Mystery Shopper Survey','Survey Sppecific to a mystery shopper','2022-06-15 19:01:58.924186',3),(3,'mystery Shopper','survey for burger place huff puff','2022-09-05 14:23:59.335177',4);
/*!40000 ALTER TABLE `acx_survey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `acx_surveyquestion`
--

DROP TABLE IF EXISTS `acx_surveyquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `acx_surveyquestion` (
  `surveyQuestionID` int(11) NOT NULL AUTO_INCREMENT,
  `surveyQuestionAttribute` varchar(255) NOT NULL,
  `question_id` int(11) NOT NULL,
  `survey_id` int(11) NOT NULL,
  `rank` decimal(20,2) NOT NULL,
  PRIMARY KEY (`surveyQuestionID`),
  KEY `acx_surveyquestion_question_id_988a0dd6_fk_acx_quest` (`question_id`),
  KEY `acx_surveyquestion_survey_id_656d3070_fk_acx_survey_surveyID` (`survey_id`),
  CONSTRAINT `acx_surveyquestion_question_id_988a0dd6_fk_acx_quest` FOREIGN KEY (`question_id`) REFERENCES `acx_question` (`questionID`),
  CONSTRAINT `acx_surveyquestion_survey_id_656d3070_fk_acx_survey_surveyID` FOREIGN KEY (`survey_id`) REFERENCES `acx_survey` (`surveyID`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acx_surveyquestion`
--

LOCK TABLES `acx_surveyquestion` WRITE;
/*!40000 ALTER TABLE `acx_surveyquestion` DISABLE KEYS */;
INSERT INTO `acx_surveyquestion` VALUES (3,'1',1,1,100.00),(4,'1',2,1,100.00),(7,'1',4,1,100.00),(8,'1',5,1,100.00),(9,'1',6,1,100.00),(10,'2',7,1,100.00),(11,'2',8,1,100.00),(12,'1',10,1,100.00),(13,'1',11,1,100.00),(14,'1',12,1,100.00),(15,'1',13,1,100.00),(16,'1',14,1,100.00),(17,'1',15,1,100.00),(18,'1',16,1,100.00),(19,'1',17,1,100.00),(20,'1',18,1,100.00),(21,'1',19,1,100.00),(22,'1',20,1,100.00),(23,'1',21,1,100.00),(24,'1',22,1,100.00),(25,'1',23,1,100.00),(26,'1',24,1,100.00),(27,'1',25,1,100.00),(28,'1',26,1,100.00),(29,'1',27,1,100.00),(30,'1',28,1,100.00),(31,'1',29,1,100.00),(32,'1',30,1,100.00),(35,'1',32,1,100.00),(36,'1',33,1,100.00),(37,'1',34,1,100.00),(38,'1',35,1,100.00),(39,'1',36,1,100.00),(40,'1',37,1,100.00),(41,'1',38,1,100.00),(42,'1',39,1,100.00),(43,'1',40,1,100.00),(44,'1',41,1,100.00),(45,'1',42,1,100.00),(46,'1',43,1,100.00),(47,'1',44,1,100.00),(48,'1',45,1,100.00),(49,'1',46,1,100.00),(50,'1',47,1,100.00),(51,'1',48,1,100.00),(52,'1',49,1,100.00),(54,'1',50,1,100.00),(55,'1',51,1,100.00),(56,'1',52,1,100.00),(57,'1',53,1,100.00),(58,'1',54,1,100.00),(59,'1',55,1,100.00),(60,'1',56,1,100.00),(61,'1',56,1,100.00),(62,'1',57,1,100.00),(63,'1',58,1,100.00),(64,'1',59,1,100.00),(65,'1',60,1,100.00),(66,'1',61,1,100.00),(67,'1',62,1,100.00),(68,'1',63,1,100.00),(69,'1',64,1,100.00),(70,'1',65,1,100.00),(71,'1',66,1,100.00),(72,'1',67,1,100.00),(73,'1',68,1,100.00),(74,'1',69,1,100.00),(75,'1',70,1,100.00),(76,'1',71,1,100.00),(77,'1',72,1,100.00),(78,'1',1,3,100.00),(79,'1',2,3,100.00);
/*!40000 ALTER TABLE `acx_surveyquestion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-23  8:46:03
