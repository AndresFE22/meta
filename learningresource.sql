-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-08-2023 a las 22:28:24
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `climate`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `learningresource`
--

CREATE TABLE `learningresource` (
  `id` int(255) NOT NULL,
  `name` varchar(999) NOT NULL,
  `descripcion` varchar(999) NOT NULL,
  `lvl` varchar(999) NOT NULL,
  `url` varchar(999) NOT NULL,
  `pt` varchar(999) NOT NULL,
  `lc` varchar(999) NOT NULL,
  `goal` varchar(999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `learningresource`
--

INSERT INTO `learningresource` (`id`, `name`, `descripcion`, `lvl`, `url`, `pt`, `lc`, `goal`) VALUES
(1, 't1', 't1', 'low', '/learning_resources/t1.jpg', 'illustration', 'activity', 'ClimateChangeFactors'),
(2, 't1', 't1', 'low', '/learning_resources/t1.mp4', 'demonstration', 'activity', 'ClimateChangeFactors'),
(4, 't1', 't1', 'low', '/learning_resources/t1.txt', 'abstract', 'activity', 'ClimateChangeFactors');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `learningresource`
--
ALTER TABLE `learningresource`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `learningresource`
--
ALTER TABLE `learningresource`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
