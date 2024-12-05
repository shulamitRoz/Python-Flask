CREATE DATABASE car_database;
GO
USE car_database;
GO

-- Create suppliers table
CREATE TABLE suppliers (
    supplier_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100)
);
GO

-- Create car table
CREATE TABLE car (
    car_id INT IDENTITY(1,1) PRIMARY KEY,
    year INT,
    company VARCHAR(50),
    model VARCHAR(50),
    style VARCHAR(50),
    price INT,
    color VARCHAR(50),
    suppliers INT NOT NULL FOREIGN KEY REFERENCES suppliers(supplier_id)
);
GO

-- Create users table
CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    password VARCHAR(10) NOT NULL,
    name VARCHAR(100) NOT NULL,
    age INT,
    country VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);
GO
