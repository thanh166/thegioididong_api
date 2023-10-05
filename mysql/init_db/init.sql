CREATE DATABASE thegioididong_db;
USE thegioididong_db;
CREATE TABLE product (
id int(10) NOT NULL AUTO_INCREMENT,
title varchar(500) NOT NULL DEFAULT '',
price varchar(30) NOT NULL,
images varchar(1000),
PRIMARY KEY (id)
);