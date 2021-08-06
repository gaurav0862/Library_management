-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2021 at 01:04 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `addmembership`
--

CREATE TABLE `addmembership` (
  `mId` int(11) NOT NULL,
  `memberName` varchar(255) NOT NULL,
  `fatherName` varchar(255) NOT NULL,
  `mobileNo` int(11) NOT NULL,
  `emailId` varchar(255) NOT NULL,
  `membershipType` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `booksalloted` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addmembership`
--

INSERT INTO `addmembership` (`mId`, `memberName`, `fatherName`, `mobileNo`, `emailId`, `membershipType`, `status`, `password`, `booksalloted`) VALUES
(1, 'Admin', 'Super Admin', 2147483647, 'admin@123', 'Scholar', 'Active', '12345', 3),
(5, 'new', 'new', 123456789, 'gauravsharma', 'Scholar', 'Active', ',bX*ZeTuKU[s', 1),
(9, 'demo', 'demo', 2147483647, 'aryankhanna1939@gmail.com', 'Scholar', 'Active', 'du4VGv0&*2s%', 1);

-- --------------------------------------------------------

--
-- Table structure for table `adminmember`
--

CREATE TABLE `adminmember` (
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `lastLogin` varchar(255) DEFAULT NULL,
  `adminType` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminmember`
--

INSERT INTO `adminmember` (`email`, `password`, `lastLogin`, `adminType`) VALUES
('Admin2@gmail.com', '45612', NULL, 'SuperAdmin');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bookingId` int(11) NOT NULL,
  `memberId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  `dateOfBooking` varchar(255) NOT NULL,
  `dateOfRelease` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bookingId`, `memberId`, `bookId`, `dateOfBooking`, `dateOfRelease`) VALUES
(7, 1, 20, '2021-08-06 14:32:52.944365', '2021-08-21 14:32:52.944365'),
(8, 1, 20, '2021-08-06 14:33:20.736130', '2021-08-21 14:33:20.736130'),
(9, 1, 20, '2021-08-06 14:33:58.055526', '2021-08-21 14:33:58.055526');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bookId` int(100) NOT NULL,
  `bookName` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `editor` varchar(255) NOT NULL,
  `numberOfTopics` int(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `ISBN` varchar(255) NOT NULL,
  `SectionName` varchar(255) NOT NULL,
  `subSectionname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bookId`, `bookName`, `author`, `editor`, `numberOfTopics`, `description`, `ISBN`, `SectionName`, `subSectionname`) VALUES
(20, '2 States', 'Chetan Bhagat', 'BBD', 5, 'love and fight.\n', 'ags52dt', 'science', 'Fiction');

-- --------------------------------------------------------

--
-- Table structure for table `membershiptype`
--

CREATE TABLE `membershiptype` (
  `typeName` varchar(255) NOT NULL,
  `booksAllowed` int(11) NOT NULL,
  `duration` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membershiptype`
--

INSERT INTO `membershiptype` (`typeName`, `booksAllowed`, `duration`) VALUES
('Scholar', 8, 25),
('Student', 3, 15),
('Teacher', 10, 30);

-- --------------------------------------------------------

--
-- Table structure for table `section`
--

CREATE TABLE `section` (
  `SectionName` varchar(255) NOT NULL,
  `description` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `section`
--

INSERT INTO `section` (`SectionName`, `description`) VALUES
('Love', 'Love Storie'),
('science', 'science\n');

-- --------------------------------------------------------

--
-- Table structure for table `subsection`
--

CREATE TABLE `subsection` (
  `subSectionname` varchar(255) NOT NULL,
  `SectionName` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subsection`
--

INSERT INTO `subsection` (`subSectionname`, `SectionName`) VALUES
('Romance', 'Love'),
('Fiction', 'science');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addmembership`
--
ALTER TABLE `addmembership`
  ADD PRIMARY KEY (`mId`),
  ADD KEY `membershipType` (`membershipType`);

--
-- Indexes for table `adminmember`
--
ALTER TABLE `adminmember`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bookingId`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bookId`),
  ADD KEY `books_ibfk_1` (`SectionName`),
  ADD KEY `subSectionname` (`subSectionname`);

--
-- Indexes for table `membershiptype`
--
ALTER TABLE `membershiptype`
  ADD PRIMARY KEY (`typeName`);

--
-- Indexes for table `section`
--
ALTER TABLE `section`
  ADD PRIMARY KEY (`SectionName`);

--
-- Indexes for table `subsection`
--
ALTER TABLE `subsection`
  ADD PRIMARY KEY (`subSectionname`),
  ADD KEY `subsection_ibfk_1` (`SectionName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addmembership`
--
ALTER TABLE `addmembership`
  MODIFY `mId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bookingId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `bookId` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `addmembership`
--
ALTER TABLE `addmembership`
  ADD CONSTRAINT `addmembership_ibfk_1` FOREIGN KEY (`membershipType`) REFERENCES `membershiptype` (`typeName`);

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`SectionName`) REFERENCES `section` (`SectionName`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `books_ibfk_2` FOREIGN KEY (`subSectionname`) REFERENCES `subsection` (`subSectionname`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subsection`
--
ALTER TABLE `subsection`
  ADD CONSTRAINT `subsection_ibfk_1` FOREIGN KEY (`SectionName`) REFERENCES `section` (`SectionName`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
