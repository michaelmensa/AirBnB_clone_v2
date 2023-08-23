-- script that prepares a MySQL server for the AirBnB project
-- db hbnb_dev_db
-- user hbnb_dev in localhost passwd hbnb_dev_pwd
-- hbnb_dev should have all priveleges on hbnb_dev_db
-- hbnb_dev has SELECT privilege on performance_schema db

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
