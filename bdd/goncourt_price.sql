-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt_price`
--

CREATE DATABASE IF NOT EXISTS goncourt_price;
USE goncourt_price;

-- --------------------------------------------------------

DROP TABLE IF EXISTS `vote`;
DROP TABLE IF EXISTS `book`;
DROP TABLE IF EXISTS `jury`;
DROP TABLE IF EXISTS `author`;
DROP TABLE IF EXISTS `person`;
DROP TABLE IF EXISTS `editor`;

--
-- Structure de la table `editor`
--

CREATE TABLE IF NOT EXISTS `editor` (
  `ed_id_editor` int NOT NULL AUTO_INCREMENT,
  `ed_name` varchar(50) NOT NULL,
  PRIMARY KEY (`ed_id_editor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `editor`
--


-- --------------------------------------------------------

--
-- Structure de la table `book`
--

CREATE TABLE IF NOT EXISTS `book` (
  `bo_id_book` int NOT NULL AUTO_INCREMENT,
  `bo_title` varchar(50) NOT NULL,
  `bo_isbn` CHAR(13) NOT NULL UNIQUE,
  `bo_resume` TEXT NOT NULL,
  `bo_main_people` TEXT,
  `bo_publication_date` DATE NOT NULL,
  `bo_editor_price` DECIMAL(3,2) NOT NULL,
  `bo_id_editor` INT NOT NULL,
  `bo_id_author` INT NOT NULL,
  PRIMARY KEY (`bo_id_book`),
  KEY `bo_id_editor` (`bo_id_editor`),
  KEY `bo_id_author` (`bo_id_author`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `book`
--


-- --------------------------------------------------------

--
-- Structure de la table `person`
--

CREATE TABLE IF NOT EXISTS `person` (
  `pe_id_person` int NOT NULL AUTO_INCREMENT,
  `pe_first_name` varchar(50) NOT NULL,
  `pe_last_name` varchar(50) NOT NULL,
  PRIMARY KEY (`pe_id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=10 CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `person`
--


-- --------------------------------------------------------

--
-- Structure de la table `author`
--

CREATE TABLE IF NOT EXISTS `author` (
  `au_id_author` int NOT NULL,
  `au_biography` TEXT,
  `au_id_person` int NOT NULL,
  PRIMARY KEY (`au_id_author`),
  KEY `au_id_person` (`au_id_person`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `author`
--


-- --------------------------------------------------------

--
-- Structure de la table `vote`
--

CREATE TABLE IF NOT EXISTS `vote` (
  `bo_id_book` int NOT NULL,
  `ju_id_jury` int NOT NULL,
  PRIMARY KEY (`bo_id_book`,`ju_id_jury`),
  KEY `bo_id_book` (`bo_id_book`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

CREATE TABLE IF NOT EXISTS `jury` (
  `ju_id_jury` int NOT NULL AUTO_INCREMENT,
  `ju_is_chairman` BOOLEAN NOT NULL DEFAULT FALSE,
  `ju_id_person` int NOT NULL,
  `ju_id_book` int,
  PRIMARY KEY (`ju_id_jury`),
  UNIQUE KEY `ju_id_person` (`ju_id_person`),
  KEY `ju_id_book` (`ju_id_book`)
) ENGINE=InnoDB CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `jury`
--


--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `author`
--
ALTER TABLE `author`
  ADD CONSTRAINT `author_ibfk_1` FOREIGN KEY (`au_id_person`) REFERENCES `person` (`pe_id_person`);

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `bo_ibfk_1` FOREIGN KEY (`bo_id_author`) REFERENCES `author` (`au_id_author`),
  ADD CONSTRAINT `bo_ibfk_2` FOREIGN KEY (`bo_id_editor`) REFERENCES `editor` (`ed_id_editor`);

--
-- Contraintes pour la table `vote`
--
ALTER TABLE `vote`
  ADD CONSTRAINT `vote_ibfk_1` FOREIGN KEY (`ju_id_jury`) REFERENCES `jury` (`ju_id_jury`),
  ADD CONSTRAINT `vote_ibfk_2` FOREIGN KEY (`bo_id_book`) REFERENCES `book` (`bo_id_book`);

--
-- Contraintes pour la table `jury`
--
ALTER TABLE `jury`
  ADD CONSTRAINT `jury_ibfk_1` FOREIGN KEY (`ju_id_person`) REFERENCES `person` (`pe_id_person`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
