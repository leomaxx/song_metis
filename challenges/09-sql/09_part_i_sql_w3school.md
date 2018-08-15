# Challenge Set 9
## Part I: W3Schools SQL Lab

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?
Around the Horn
B's Beverages
Consolidated Holdings
Eastern Connection
Island Trading
North/South
Seven Seas Imports

2. What is the name of the customer who has the most orders?
CustomerName	OrderCount
Ernst Handel	10

SELECT CustomerName, count(OrderID) AS OrderCount
FROM Customers LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerName
ORDER BY count(OrderID) DESC;

3. Which supplier has the highest average product price?
SupplierName	AvgPrice
Aux joyeux ecclésiastiques	140.75

SELECT SupplierName, AVG(Price) AS AvgPrice
FROM Suppliers LEFT JOIN Products
ON Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
ORDER BY AVG(Price) DESC;

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

21

SELECT COUNT(DISTINCT Country)
FROM Customers;


5. What category appears in the most orders?

CategoryName	COUNT(DISTINCT OrderID)
Produce	196

SELECT CategoryName, COUNT(DISTINCT OrderID)
FROM Categories, Products, OrderDetails
WHERE Categories.CategoryID = Products.CategoryID
AND Products.ProductID = OrderDetails.ProductID

6. What was the total cost for each order?

SELECT OrderID, sum(Price*Quantity) AS TotalCost
FROM Products, OrderDetails
WHERE Products.ProductID = OrderDetails.ProductID
GROUP BY OrderID

7. Which employee made the most sales (by total price)?

SELECT LastName, FirstName, sum(Price*Quantity) AS TotalSales
FROM Employees, Products, Orders, OrderDetails
WHERE Employees.EmployeeID = Orders.EmployeeID
AND Products.ProductID = OrderDetails.ProductID
AND Orders.OrderID = OrderDetails.OrderID
GROUP BY Employees.EmployeeID

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
FirstName	LastName
Janet	Leverling
Steven	Buchanan

SELECT FirstName, LastName
FROM Employees
WHERE Notes LIKE '%BS%';

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

SupplierName	ProductCount	AveragePrice
Tokyo Traders	3	46

SELECT SupplierName, COUNT(DISTINCT ProductID) AS ProductCount, AVG(Price) AS AveragePrice
FROM Suppliers, Products
WHERE Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
HAVING COUNT(DISTINCT ProductID) > 2
ORDER BY AVG(Price) DESC
LIMIT 1;
