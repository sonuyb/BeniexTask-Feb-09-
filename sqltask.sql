create database chib;
use chib;
CREATE TABLE SampleTable (
    ID INT PRIMARY KEY,
    Empname VARCHAR(50),
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10, 2),
    JoinDate DATE,
    Gender CHAR(1),
    City VARCHAR(50),
    Education VARCHAR(50),
    ExperienceYears INT
);
INSERT INTO SampleTable values(1,'Joseph',24,'MCA',15000,'2019-11-11','m','thrissur','mca',5),
(2,'Sujith',23,'MBA',15000,'2020-08-11','m','kozhikode','mba',4),
(3,'Dhanu',22,'BTECH',30000,'2023-09-21','m','trivandrum','it',1),
(4,'Aswin',21,'IT',11000,'2022-07-27','m','kollam','cs',2),
(5,'Catherine',25,'MBA',21000,'2024-08-26','f','kottayam','mba',4),
(6,'Shona',23,'BIOCHEM',19500,'2022-01-11','f','ernakulam','chem',2),
(7,'Josly',24,'BIONANO',20000,'2020-11-07','f','alppuzha','bionano',4),
(8,'Sreejith',20,'BIOFOOD',21000,'2022-05-06','M','thrissur','foodtechno',2),
(9,'Michael',27,'MBA',15000,'2019-03-01','m','pathanamthitta','mba',5),
(10,'Rona',19,'MCOM',24000,'2019-02-07','f','kannur','btech',5);

select * from SampleTable;

-- Scenario 1 Select all records where age is greater than 18 and the gender is 'F':
SELECT * FROM SampleTable WHERE Age > 18 AND Gender = 'F';

-- Scenario 2 - Select distinct categories available in the table:
SELECT DISTINCT Age FROM SampleTable;

-- Scenario 3 - Select records where the Salary is between 15000 and 20000:
SELECT * FROM SampleTable WHERE Salary  BETWEEN 15000  AND 20000;

-- Scenario 4 - Select records where the city is either 'trivandrum' or 'kasargod':
SELECT * FROM SampleTable WHERE City IN ('trivandrum', 'kannur');

-- Scenario 5 - Select records where age is not between 20 and 30:
SELECT * FROM SampleTable WHERE Age NOT BETWEEN 20 AND 30;

-- Scenario 6 - Select records where the country is 'trivandrum' and the Salary is '30000':
SELECT * FROM SampleTable WHERE City= 'trivandrum' AND Salary = '30000';

-- Scenario 7 - Select records where the age is greater than 20 and the grade is 'B+':
SELECT * FROM SampleTable WHERE Age = 22 and Salary = 30000;

-- Scenario 8 - Select records where the name starts with 'A' or 'B' and the age is less than 25:
SELECT * FROM SampleTable WHERE (Empname LIKE 'A%' OR Empname LIKE 'S%') AND Age < 25;

-- Scenario 9 - Select records where the score in both Salary is above 80:
SELECT * FROM SampleTable WHERE Salary> 10000 AND Salary> 20000;

-- Scenario 10 - Select records where the name is 'Dhanu' or 'Aswin' and the city is not 'Alappuzha':
SELECT * FROM SampleTable WHERE (Empname = 'Dhanu' OR Empname = 'Aswin') AND City != 'Alappuzha';

-- Scenario 11 - Select records where the Department is either IT' or 'BTECH':
SELECT * FROM SampleTable WHERE Department IN ('IT', 'MCA');

-- Scenario 12 - Select records where the age is greater than 21 or the city is 'kannur':
SELECT * FROM SampleTable WHERE Age > 23 OR City = 'kannur';

-- Scenario 13 - Select records where the city is not 'pathanamthitta' and the department is not 'IT' or 'MBA':
SELECT * FROM SampleTable WHERE City != 'pathanamthitta' AND Department NOT IN ('IT', 'MBA');

-- Scenario 14 - Select records where the age is between 18 and 25 and the gender is 'm':
SELECT * FROM SampleTable WHERE Age BETWEEN 18 AND 25 AND Gender = 'm';

-- Scenario 15 - Select records where the name starts with 'A' and the score in Age is greater than 20:
SELECT * FROM SampleTable WHERE Empname LIKE 'A%' AND Age > 20;




