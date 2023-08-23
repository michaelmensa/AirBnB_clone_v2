-- script that prepares a MySQL server for the AirBnB project
-- db hbnb_test_db
-- user hbnb_test in localhost passwd hbnb_test_pwd
-- hbnb_test should have all priveleges on hbnb_test_db
-- hbnb_test has SELECT privilege on performance_schema db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
