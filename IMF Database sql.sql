-- International Net Position from IMF website

-- Project by Group 5
-- Data Analysts
-- "Ifeka Odira Hillary"
-- "Deborah Abosede"
-- "Convenenant Lenu"
-- "Dr Isaac Israel"

-- Developers
-- "Melvind-P"
-- "Kenechukwu"

-- CREATE DATABASE imf_data;
CREATE TABLE annual_data (
  Annual_ID INT PRIMARY KEY,
  Country_ID INT,
  Country VARCHAR(100),
  Metric VARCHAR(500),
  Year INT,
  Value DECIMAL(15,2)
);

-- SELECT COUNT (*) FROM quarterly_data

CREATE TABLE quarterly_data (
  Quarter_ID INT PRIMARY KEY,
  Country_ID INT,
  Country VARCHAR(100),
  Metric VARCHAR(500),
  Quarter VARCHAR(10),
  Value DECIMAL(15,2)
);

-- Countries Table creation and Population
CREATE TABLE countries (
  Country_ID INT PRIMARY KEY,
  Country VARCHAR(100) UNIQUE
);

SELECT * FROM annual_data


INSERT INTO countries (Country_ID, Country)
VALUES (4, 'Austria'), (1, 'Germany'), (3, 'Luxembourg'), (2, 'Switzerland'), (5, 'Spain');

SELECT * FROM annual_data LIMIT 10;
SELECT * FROM quarterly_data LIMIT 10;
SELECT * FROM countries;

-- Setting up foreign Key Relationship
ALTER TABLE annual_data
ADD CONSTRAINT fk_country
FOREIGN KEY (Country_ID) REFERENCES countries(Country_ID);

ALTER TABLE quarterly_data
ADD CONSTRAINT fk_country_quarterly
FOREIGN KEY (Country_ID) REFERENCES countries(Country_ID);

-- ANALYSIS (the total value of each metric by country for each year)
SELECT Country, Metric, Year, SUM(Value) AS Total_Value
FROM annual_data
GROUP BY Country, Metric, Year
ORDER BY Year DESC;

-- Trends over Time for NIIP
SELECT Country, Year, SUM(Value) AS Total_NIIP
FROM annual_data
WHERE Metric = 'Net international investment position'
GROUP BY Country, Year
ORDER BY Country, Year;

 -- Total Assets and Liabilities Comparison
SELECT Country,
       SUM(CASE WHEN Metric LIKE 'Assets%' THEN Value ELSE 0 END) AS Total_Assets,
       SUM(CASE WHEN Metric LIKE 'Liabilities%' THEN Value ELSE 0 END) AS Total_Liabilities
FROM annual_data
GROUP BY Country
ORDER BY Total_Assets DESC;

 -- Investment Breakdown by Sector
SELECT Country, 
       SUM(CASE WHEN Metric LIKE 'Direct investment%' THEN Value ELSE 0 END) AS Direct_Investment,
       SUM(CASE WHEN Metric LIKE 'Portfolio investment%' THEN Value ELSE 0 END) AS Portfolio_Investment
FROM annual_data
GROUP BY Country
ORDER BY Direct_Investment DESC;

-- Growth of Total Assets over Time
SELECT Country, Year, SUM(Value) AS Total_Assets
FROM annual_data
WHERE Metric LIKE 'Assets%'
GROUP BY Country, Year
ORDER BY Country, Year;








 