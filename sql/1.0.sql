---------------------------------------------------------------------------------------- 
-- Create a table
---------------------------------------------------------------------------------------- 
USE dev_employee_portal;
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    gender VARCHAR(10),
    phoneNo VARCHAR(15),
    addressDetails JSON,
        -- hno VARCHAR(20),
        -- street VARCHAR(255),
        -- city VARCHAR(255),
        -- state VARCHAR(255),
    workExperience JSON,
        -- companyName VARCHAR(255),
        -- fromDate VARCHAR(255),
        -- toDate VARCHAR(255),
        -- address VARCHAR(255),
    qualifications JSON, 
        -- qualificationName VARCHAR(255),
        -- fromDate VARCHAR(255),
        -- toDate VARCHAR(255),
        -- percentage DOUBLE,
    projects JSON, 
        -- title VARCHAR(255),
        -- description VARCHAR(255),
    photo MEDIUMBLOB
);
