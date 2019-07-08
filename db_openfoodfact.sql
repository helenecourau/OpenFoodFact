CREATE DATABASE healthy_food CHARACTER SET 'utf8';
USE healthy_food; 

CREATE TABLE Category (
	id INT UNSIGNED AUTO_INCREMENT,
	name VARCHAR(150) NOT NULL UNIQUE,
	PRIMARY KEY(id)
)
ENGINE=INNODB;

CREATE TABLE Product (
	id INT UNSIGNED AUTO_INCREMENT,
	name VARCHAR(150) NOT NULL UNIQUE,
	description TEXT(255),
	grade VARCHAR(10) NOT NULL,
	url VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=INNODB;

CREATE TABLE Category_product (
	id_category INT UNSIGNED,
	id_product INT UNSIGNED,
	PRIMARY KEY(id_category, id_product)
)
ENGINE=INNODB;

CREATE TABLE Store (
	id INT UNSIGNED AUTO_INCREMENT,
	name VARCHAR(150) NOT NULL UNIQUE,
	PRIMARY KEY(id)
)
ENGINE=INNODB;

CREATE TABLE Store_product (
	id_store INT UNSIGNED,
	id_product INT UNSIGNED,
	PRIMARY KEY(id_store, id_product)
)
ENGINE=INNODB;

CREATE TABLE Fav_product (
	id_bad_product INT UNSIGNED,
	id_good_product INT UNSIGNED,
	PRIMARY KEY(id_bad_product, id_good_product)
)
ENGINE=INNODB;

ALTER TABLE Category_product
ADD CONSTRAINT fk_id_category FOREIGN KEY (id_category) REFERENCES Category(id),
ADD CONSTRAINT fk_id_product FOREIGN KEY (id_product) REFERENCES Product(id);

ALTER TABLE Store_product
ADD CONSTRAINT fk_id_store FOREIGN KEY (id_store) REFERENCES Store(id),
ADD CONSTRAINT fk_id_product_for_store FOREIGN KEY (id_product) REFERENCES Product(id);

ALTER TABLE Fav_product
ADD CONSTRAINT fk_id_bad_product FOREIGN KEY (id_bad_product) REFERENCES Product(id),
ADD CONSTRAINT fk_id_good_product FOREIGN KEY (id_good_product) REFERENCES Product(id);