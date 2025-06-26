--
-- MySQL dump for 'countries' table
--

--
-- Table structure for table `countries`
--

-- Drop table if it already exists to ensure a clean slate
DROP TABLE IF EXISTS `countries`;

-- Create the countries table
CREATE TABLE `countries` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(100) NOT NULL UNIQUE,
  `capital` VARCHAR(100) NOT NULL,
  `currency` VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`name`, `capital`, `currency`) VALUES
('United States', 'Washington D.C.', 'US Dollar'),
('Canada', 'Ottawa', 'Canadian Dollar'),
('Mexico', 'Mexico City', 'Mexican Peso'),
('Brazil', 'Brasília', 'Brazilian Real'),
('United Kingdom', 'London', 'Pound Sterling'),
('France', 'Paris', 'Euro'),
('Germany', 'Berlin', 'Euro'),
('Italy', 'Rome', 'Euro'),
('Spain', 'Madrid', 'Euro'),
('China', 'Beijing', 'Chinese Yuan'),
('India', 'New Delhi', 'Indian Rupee'),
('Japan', 'Tokyo', 'Japanese Yen'),
('Australia', 'Canberra', 'Australian Dollar'),
('South Africa', 'Pretoria', 'South African Rand'),
('Egypt', 'Cairo', 'Egyptian Pound'),
('Saudi Arabia', 'Riyadh', 'Saudi Riyal'),
('Russia', 'Moscow', 'Russian Ruble'),
('Argentina', 'Buenos Aires', 'Argentine Peso'),
('South Korea', 'Seoul', 'South Korean Won'),
('Indonesia', 'Jakarta', 'Indonesian Rupiah');

-- End of dump
