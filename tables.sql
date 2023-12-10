-- Firstly, create DB called grocery_store

-- Create inventory table
CREATE TABLE `inventory` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `quantity_id` int NOT NULL,
  `price_per_quantity` decimal(13,2) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `fk_quantity_id_idx` (`quantity_id`),
  CONSTRAINT `fk_quantity_id` FOREIGN KEY (`quantity_id`) REFERENCES `quantity` (`quantity_id`) ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create orderInfo table
CREATE TABLE `orderInfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` decimal(13,2) NOT NULL,
  `total` decimal(13,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_order_id_idx` (`order_id`),
  KEY `fk_product_id_idx` (`product_id`),
  CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON UPDATE RESTRICT,
  CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `inventory` (`product_id`) ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create orders table
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(45) NOT NULL,
  `total_price` decimal(13,2) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create quantity table
CREATE TABLE `quantity` (
  `quantity_id` int NOT NULL AUTO_INCREMENT,
  `quantity_name` varchar(45) NOT NULL,
  PRIMARY KEY (`quantity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
