-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 27, 2023 at 07:36 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `korpus`
--

-- --------------------------------------------------------

--
-- Table structure for table `anotasi`
--

CREATE TABLE `anotasi` (
  `id_anotasi` int(11) NOT NULL,
  `id_korpus` int(11) NOT NULL,
  `kelas_kata` varchar(60) NOT NULL,
  `sintaksi` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `daftar_kata`
--

CREATE TABLE `daftar_kata` (
  `id_daftar_kata` int(11) NOT NULL,
  `nama_kata` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `daftar_kata`
--

INSERT INTO `daftar_kata` (`id_daftar_kata`, `nama_kata`) VALUES
(1138, 'Awang.'),
(1139, 'Dempo'),
(1140, 'kadetengnganna'),
(1141, 'Dempo'),
(1142, 'kadetengnganna'),
(1143, 'Awang.');

-- --------------------------------------------------------

--
-- Table structure for table `korpus`
--

CREATE TABLE `korpus` (
  `id_korpus` int(11) NOT NULL,
  `konten` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `korpus`
--

INSERT INTO `korpus` (`id_korpus`, `konten`) VALUES
(70, 'kadetengnganna Dempo Awang.'),
(71, 'kadetengnganna Dempo Awang.');

-- --------------------------------------------------------

--
-- Table structure for table `meta_data`
--

CREATE TABLE `meta_data` (
  `id_meta_data` int(11) NOT NULL,
  `id_korpus` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `sumber` varchar(255) NOT NULL,
  `penerbit` varchar(60) NOT NULL,
  `jumlah_kata` int(11) NOT NULL,
  `jumlah_kalimat` int(11) NOT NULL,
  `judul` varchar(60) NOT NULL,
  `penulis` varchar(60) NOT NULL,
  `kategori` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meta_data`
--

INSERT INTO `meta_data` (`id_meta_data`, `id_korpus`, `tanggal`, `sumber`, `penerbit`, `jumlah_kata`, `jumlah_kalimat`, `judul`, `penulis`, `kategori`) VALUES
(64, 70, '2000-01-01', 'dari jonggol', 'Niqay Barbelong 96', 3, 1, 'My Only Love', 'ya gue siapa lagi', 'Pilih Kategori'),
(65, 71, '2000-01-01', '', '', 3, 1, 'My Only One', '', 'Pilih Kategori');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anotasi`
--
ALTER TABLE `anotasi`
  ADD PRIMARY KEY (`id_anotasi`),
  ADD KEY `id_korpus` (`id_korpus`);

--
-- Indexes for table `daftar_kata`
--
ALTER TABLE `daftar_kata`
  ADD PRIMARY KEY (`id_daftar_kata`);

--
-- Indexes for table `korpus`
--
ALTER TABLE `korpus`
  ADD PRIMARY KEY (`id_korpus`);

--
-- Indexes for table `meta_data`
--
ALTER TABLE `meta_data`
  ADD PRIMARY KEY (`id_meta_data`),
  ADD KEY `meta_data` (`id_korpus`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anotasi`
--
ALTER TABLE `anotasi`
  MODIFY `id_anotasi` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `daftar_kata`
--
ALTER TABLE `daftar_kata`
  MODIFY `id_daftar_kata` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1144;

--
-- AUTO_INCREMENT for table `korpus`
--
ALTER TABLE `korpus`
  MODIFY `id_korpus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT for table `meta_data`
--
ALTER TABLE `meta_data`
  MODIFY `id_meta_data` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `anotasi`
--
ALTER TABLE `anotasi`
  ADD CONSTRAINT `anotasi_ibfk_1` FOREIGN KEY (`id_korpus`) REFERENCES `korpus` (`id_korpus`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `meta_data`
--
ALTER TABLE `meta_data`
  ADD CONSTRAINT `meta_data` FOREIGN KEY (`id_korpus`) REFERENCES `korpus` (`id_korpus`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
