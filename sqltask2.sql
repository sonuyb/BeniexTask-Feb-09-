-- 1) Complete full word document with all points from 3 days session.

select * from customer_master;
select * from sales_order;


-- 2) Write a command to display first 10 rows.
  SELECT * FROM customer_master LIMIT 10;
  SELECT * FROM sales_order LIMIT 10;
 
-- 3) Identify unique items?
SELECT DISTINCT Item FROM sales_order;
 
-- 4)Identify any unit cost is negative?
SELECT * FROM sales_order WHERE UnitCost < 0;
 
 
-- 5) Identify minimum and maximum unit price happened for same item.
SELECT Item, MIN(UnitCost) AS min_unit_price, MAX(UnitCost) AS max_unit_price
FROM sales_order
GROUP BY Item;
 
-- 6) Identify the Total sales happened in the year of 2021?
SELECT SUM(Total) AS total_sales_2021
FROM sales_order
WHERE YEAR(STR_TO_DATE(OrderDate, '%d-%m-%Y')) = 2021;
 
-- 7) Which item is sold maximum in the year 2021?
SELECT Item, SUM(Units) AS total_units_sold
FROM sales_order
WHERE YEAR(STR_TO_DATE(OrderDate, '%d-%m-%Y')) = 2021
GROUP BY Item
ORDER BY total_units_sold DESC
LIMIT 1;
 
-- 8) Identify the region with highest and lowest sales.
SELECT cm.Region, SUM(so.Total) AS total_sales
FROM customer_master AS cm
JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region
ORDER BY total_sales DESC
LIMIT 1;
 
SELECT cm.Region, SUM(so.Total) AS total_sales
FROM customer_master AS cm
JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region
ORDER BY total_sales ASC
LIMIT 1;
 
-- 9) Identify the customer name having highest sales for the year 2022.
SELECT cm.Customer, SUM(so.Total) AS total_sales_2022
FROM customer_master AS cm
JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID
WHERE YEAR(STR_TO_DATE(so.OrderDate, '%d-%m-%Y')) = 2022
GROUP BY cm.Customer
ORDER BY total_sales_2022 DESC
LIMIT 1;
 
-- 10) Which item has highest and lowest unit cost?
SELECT Item, `UnitCost` AS max_unit_cost
FROM sales_order
WHERE `UnitCost` = (SELECT MAX(`UnitCost`) FROM sales_order);
 
SELECT Item, `UnitCost` AS min_unit_cost
FROM sales_order
WHERE `UnitCost` = (SELECT MIN(`UnitCost`) FROM sales_order);
 
-- 11) Identify items starts with letter 'P'.
SELECT * FROM sales_order
WHERE Item LIKE 'P%';
 
-- 12) Filter the table having items Pen and Pencil.
SELECT * FROM sales_order
WHERE Item IN ('Pen', 'Pencil');
 
-- 13) Filter the table with unit cost between 1 and 100.
SELECT * FROM sales_order
WHERE `UnitCost` BETWEEN 1 AND 100;
 
-- 14) Identify the customer with more no of transaction(no of entries).
SELECT Customer_ID, COUNT(*) AS transaction_count
FROM sales_order
GROUP BY Customer_ID
ORDER BY transaction_count DESC
LIMIT 1;
 
-- 15) Identify which item has maximum sales in each region.
SELECT cm.Region, so.Item, SUM(so.Units) AS total_units_sold
FROM customer_master AS cm
JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region, so.Item
HAVING SUM(so.Units) = (SELECT MAX(total_units_sold)
                        FROM (SELECT cm.Region, so.Item, SUM(so.Units) AS total_units_sold
                              FROM customer_master AS cm
                              JOIN sales_order AS so ON cm.Customer_ID = so.Customer_ID
                              GROUP BY cm.Region, so.Item) AS max_sales_per_region
                        WHERE max_sales_per_region.Region = cm.Region)
ORDER BY cm.Region;

-- 16)  Create 5 more scenarios using important inbuilt functions of MySQL.

-- 1.Identify the average unit price for each item:

     SELECT  AVG(`UnitCost`) AS AvgUnitPrice
     FROM sales_order;

-- 2.Identify the total number of sales transactions for each customer:

SELECT Customer_ID, COUNT(*) AS TotalTransactions
FROM sales_order
GROUP BY Customer_ID;

-- 3.Identify the month with the highest sales in each region:

SELECT Region, MONTH(OrderDate) AS Month, SUM(Total) AS Total
FROM customer_master as c
JOIN sales_order as s ON c.Customer_ID = s.Customer_ID
GROUP BY Region, MONTH(OrderDate)
ORDER BY Total DESC;


-- 4.Identify the top 5 customers with the highest total sales:

SELECT Customer_ID, SUM(Total) AS TotalSales
FROM Sales_order as s
GROUP BY s.Customer_ID
ORDER BY TotalSales DESC
LIMIT 5;

-- 5.Identify the number of sales transactions per month for the year 2022:

SELECT MONTH(STR_TO_DATE(OrderDate, '%d-%m-%Y')) AS Month, COUNT(*) AS Transactions
FROM sales_order
WHERE YEAR(STR_TO_DATE(OrderDate,'%d-%m-%Y')) = 2021
GROUP BY MONTH(STR_TO_DATE(OrderDate,'%d-%m-%Y'));

