-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 16, 2020 at 03:01 PM
-- Server version: 5.6.47-log
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `yundonghui`
--

-- --------------------------------------------------------

--
-- Table structure for table `chengji`
--

CREATE TABLE `chengji` (
  `YID` char(12) NOT NULL,
  `XID` char(12) NOT NULL,
  `Score` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chengji`
--

INSERT INTO `chengji` (`YID`, `XID`, `Score`) VALUES
('00', '00', 100),
('01', '01', 96),
('03', '00', 77),
('04', '01', 99),
('06', '01', 99);

-- --------------------------------------------------------

--
-- Table structure for table `gongzuogongwei`
--

CREATE TABLE `gongzuogongwei` (
  `g_name` char(12) NOT NULL,
  `g_ID` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gongzuogongwei`
--

INSERT INTO `gongzuogongwei` (`g_name`, `g_ID`) VALUES
('管理员', '00'),
('普通工作人员', '01');

-- --------------------------------------------------------

--
-- Table structure for table `gongzuorenyuan`
--

CREATE TABLE `gongzuorenyuan` (
  `Gname` char(12) NOT NULL,
  `GID` char(12) NOT NULL,
  `g_ID` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gongzuorenyuan`
--

INSERT INTO `gongzuorenyuan` (`Gname`, `GID`, `g_ID`) VALUES
('hulin', '00', '00'),
('ceshi', '01', '01');

-- --------------------------------------------------------

--
-- Table structure for table `xiangmu`
--

CREATE TABLE `xiangmu` (
  `Xname` char(12) NOT NULL,
  `XID` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `xiangmu`
--

INSERT INTO `xiangmu` (`Xname`, `XID`) VALUES
('跑步', '00'),
('跳远', '01'),
('游泳', '02');

-- --------------------------------------------------------

--
-- Table structure for table `yundongyuan`
--

CREATE TABLE `yundongyuan` (
  `Yname` char(12) NOT NULL,
  `YID` char(12) NOT NULL,
  `XID` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `yundongyuan`
--

INSERT INTO `yundongyuan` (`Yname`, `YID`, `XID`) VALUES
('tom', '00', '00'),
('张三', '01', '01'),
('李四', '03', '00'),
('万无', '04', '01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chengji`
--
ALTER TABLE `chengji`
  ADD PRIMARY KEY (`YID`);

--
-- Indexes for table `gongzuogongwei`
--
ALTER TABLE `gongzuogongwei`
  ADD PRIMARY KEY (`g_ID`);

--
-- Indexes for table `gongzuorenyuan`
--
ALTER TABLE `gongzuorenyuan`
  ADD PRIMARY KEY (`GID`);

--
-- Indexes for table `xiangmu`
--
ALTER TABLE `xiangmu`
  ADD PRIMARY KEY (`XID`);

--
-- Indexes for table `yundongyuan`
--
ALTER TABLE `yundongyuan`
  ADD PRIMARY KEY (`YID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
