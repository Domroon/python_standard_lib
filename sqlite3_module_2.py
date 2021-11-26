import sqlite3
from pathlib import Path
import sys
from datetime import datetime as DateTime


PATH = Path()
CURRENT = PATH.cwd()
DATABASES = CURRENT / 'databases'

SQL_COMMANDS = [
                { 'enable_foreign_keys' :
                ['''PRAGMA foreign_keys = ON''', 'enabled foreign keys support']
                },
                { 'create_stocks' :
                ['''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''', 'created stock table']
                },
                { 'create_customers' :
                ['''CREATE TABLE customers (CustomerID INTEGER PRIMARY KEY, CustomerName text UNIQUE, ContactName text UNIQUE, Address text, City text, PostalCode text, Country text)''', 'created customer table']
                },
                { 'create_products' :
                ['''CREATE TABLE products (ProductID INTEGER PRIMARY KEY, ProductName text UNIQUE, SupplierID int, CatergoryID int, Unit text, Price real, FOREIGN KEY(SupplierID) REFERENCES suppliers(SupplierID))''', 'created products table']
                },
                { 'create_orders' :
                ['''CREATE TABLE orders (OrderID INTEGER PRIMARY KEY, CustomerID INTEGER, EmployeeID int, OrderDate text, ShipperID int, FOREIGN KEY(CustomerID) REFERENCES customers(CustomerID))''', 'created orders table']
                },
                { 'create_suppliers' :
                ['''CREATE TABLE suppliers (SupplierID INTEGER PRIMARY KEY, SupplierName Text NOT NULL UNIQUE, ContactName text, Address text, City text NOT NULL, PostalCode text NOT NULL, Country text NOT NULL)''', 'created suppliers table']
                },
                { 'create_shippers' :
                ['''CREATE TABLE shippers (ShipperID INTEGER PRIMARY KEY, ShipperName text UNIQUE NOT NULL)''', 'created shippers table']
                },
                { 'create_employees' :
                ['''CREATE TABLE employees (EmployeeID INTEGER PRIMARY KEY, LastName text, FirstName text, BirthDate text, Photo text UNIQUE, Notes text)''', 'created employees table']
                },
                { 'create_orderDetails' :
                ['''CREATE TABLE orderDetails (OrderDetailID INTEGER PRIMARY KEY, OrderID int NOT NULL, ProductID int NOT NULL, quantity int NOT NULL, FOREIGN KEY(OrderID) REFERENCES orders(OrderID), FOREIGN KEY(ProductID) REFERENCES products(ProductID))''', 'created orderDetails table']
                },
                { 'drop_stocks' :
                ['''DROP TABLE stocks''', 'deleted']
                },
                { 'drop_customers' :
                ['''DROP TABLE customers''', 'deleted']
                },
                { 'drop_orders' :
                ['''DROP TABLE orders''', 'deleted']
                },
                { 'drop_products' :
                ['''DROP TABLE products''', 'deleted']
                },
                { 'drop_suppliers' :
                ['''DROP TABLE suppliers''', 'deleted']
                },
                { 'drop_shippers' :
                ['''DROP TABLE shippers''', 'deleted']
                },
                { 'drop_orderDetails' :
                ['''DROP TABLE orderDetails''', 'deleted']
                },
                { 'insert_stock' :
                ['INSERT INTO stocks VALUES ("2020-11-18" ,"BUY", "IBM", 500, 42.2)', 'inserted']
                },
                { 'insert_customer1' :
                ['INSERT INTO customers VALUES (NULL, "Alfreds Futterkiste", "Maria Anders", "Obere Str. 57", "Berlin", 12209, "Germany")', 'inserted']
                },
                { 'insert_customer2' :
                ['INSERT INTO customers VALUES (NULL, "Ana Trujillo Emparedados y helados", "Ana Trujillo", "Avda. de la Constitución 2222", "México D.F.", 05021, "Mexico")', 'inserted']
                },
                { 'insert_customer3' :
                ['INSERT INTO customers VALUES (NULL, "Antonio Moreno Taquería", "Antonio Moreno", "Mataderos 2312", "México D.F.", 05023, "Mexico")', 'inserted']
                },
                { 'insert_customer4' :
                ['INSERT INTO customers VALUES (NULL, "Around the Horn", "Thomas Hardy", "120 Hanover Sq.", "London", "WA1 1DP", "UK")', 'inserted']
                },
                { 'insert_customer5' :
                ['INSERT INTO customers VALUES (NULL, "Berglunds snabbköp", "Christina Berglund", "Berguvsvägen 8", "Luleå", "S-958 22", "Sweden")', 'inserted']
                },
                { 'insert_customer63' :
                ['INSERT INTO customers VALUES (63, "QUICK-Stop", "Horst Kloss", "Taucherstraße 10", "Cunewalde", "01307", "Germany")', 'inserted']
                },
                { 'insert_customer25' :
                ['INSERT INTO customers VALUES (25, "Frankenversand", "Peter Franken", "Berliner Platz 43", "München", "80805", "Germany")', 'inserted']
                },
                { 'insert_customer17' :
                ['INSERT INTO customers VALUES (17, "Drachenblut Delikatessen", "Sven Ottlieb", "Walserweg 21", "Aachen", "52066", "Germany")', 'inserted']
                },
                { 'insert_product1' :
                ['INSERT INTO products VALUES (NULL, "Chais", 1, 1 , "10 boxes x 20 bags", 18)', 'inserted']
                },
                { 'insert_product2' :
                ['INSERT INTO products VALUES (NULL, "Chang", 1, 1 , "24 - 12 oz bottles", 19)', 'inserted']
                },
                { 'insert_product3' :
                ['INSERT INTO products VALUES (NULL, "Aniseed Syrup", 1, 2 , "12 - 550 ml bottles", 10)', 'inserted']
                },
                { 'insert_product4' :
                ['INSERT INTO products VALUES (NULL, "Chef Antons Cajun Seasoning", 2, 2 , "48 - 6 oz jars", 22)', 'inserted']
                },
                { 'insert_product5' :
                ['INSERT INTO products VALUES (NULL, "Chef Antons Gumbo Mix", 2, 2 , "36 boxes", 21.35)', 'inserted']
                },
                { 'insert_product6' :
                ['INSERT INTO products VALUES (NULL, "Grandmas Boysenberry Spread", 3, 2 , "12 - 8 oz jars", 25)', 'inserted']
                },
                { 'insert_product7' :
                ['INSERT INTO products VALUES (NULL, "Uncle Bobs Organic Dried Pears", 3, 7 , "12 - 1 lb pkgs", 30)', 'inserted']
                },
                { 'insert_product8' :
                ['INSERT INTO products VALUES (NULL, "Northwoods Cranberry Sauce", 3, 2 , "12 - 12 oz jars", 40)', 'inserted']
                },
                { 'insert_product9' :
                ['INSERT INTO products VALUES (NULL, "Mishi Kobe Niku", 4, 6 , "18 - 500 g pkgs", 97)', 'inserted']
                },
                { 'insert_order1' :
                ['INSERT INTO orders VALUES (10248, 1, 5, "7/4/1996", 3)', 'inserted']
                },
                { 'show_customer_id' :
                ['SELECT CustomerID FROM Orders WHERE OrderID=10248', None]
                },
                { 'insert_order2' :
                ['INSERT INTO orders VALUES (10249, 1, 6, "7/5/1996", 1)', 'inserted']
                },
                { 'insert_order3' :
                ['INSERT INTO orders VALUES (10250, 2, 4, "7/8/1996", 2)', 'inserted']
                },
                { 'insert_order4' :
                ['INSERT INTO orders VALUES (10251, 3, 3, "7/9/1996", 1)', 'inserted']
                },
                { 'insert_order5' :
                ['INSERT INTO orders VALUES (10252, 63, 4, "7/10/1996", 2)', 'inserted']
                },
                { 'insert_supplier1' :
                ['INSERT INTO suppliers VALUES (NULL, "Exotic Liquid", "Charlotte Cooper", "49 Gilbert St.", "London", "EC1 4SD", "UK")', 'inserted']
                },
                { 'insert_supplier2' :
                ['INSERT INTO suppliers VALUES (NULL, "New Orleans Cajun Delights", "Shelley Burke", "P.O. Box 78934", "New Orleans", "70117", "USA")', 'inserted']
                },
                { 'insert_supplier3' :
                ['INSERT INTO suppliers VALUES (NULL, "Grandma Kellys Homestead", "Regina Murphy", "707 Oxford Rd.", "Ann Arbor", "48104", "USA")', 'inserted']
                },
                { 'insert_supplier4' :
                ['INSERT INTO suppliers VALUES (NULL, "Tokyo Traders", "Yoshi Nagase", "9-8 Sekimai Musashino-shi", "Tokyo", "100", "Japan")', 'inserted']
                },
                { 'insert_shipper1' :
                ['INSERT INTO shippers VALUES (NULL, "Speedy Express")', 'inserted']
                },
                { 'insert_shipper2' :
                ['INSERT INTO shippers VALUES (NULL, "United Package")', 'inserted']
                },
                { 'insert_shipper3' :
                ['INSERT INTO shippers VALUES (NULL, "Federal Shipping")', 'inserted']
                },
                { 'insert_shipper4' :
                ['INSERT INTO shippers VALUES (NULL, "DHL")', 'inserted']
                },
                { 'insert_shipper5' :
                ['INSERT INTO shippers VALUES (NULL, "Deutsche Post")', 'inserted']
                },
                { 'insert_employee1' :
                ['INSERT INTO employees VALUES (NULL, "Davolio", "Nancy", "1968-12-08", "EmpID1.pic" , "Education includes a BA....")', 'inserted']
                },
                { 'insert_employee2' :
                ['INSERT INTO employees VALUES (NULL, "Fuller", "Andrew", "1952-02-19", "EmpID2.pic" , "Andrew received his BTS....")', 'inserted']
                },
                { 'insert_employee3' :
                ['INSERT INTO employees VALUES (NULL, "Leverling", "Janet", "1963-08-30", "EmpID3.pic" , "Janet has a BS degree....")', 'inserted']
                },
                { 'insert_orderDetail1' :
                ['INSERT INTO orderDetails VALUES (NULL, 10248, 9, 12)', 'inserted']
                },
                { 'insert_orderDetail2' :
                ['INSERT INTO orderDetails VALUES (NULL, 10248, 8, 10)', 'inserted']
                },
                { 'insert_orderDetail3' :
                ['INSERT INTO orderDetails VALUES (NULL, 10248, 5, 5)', 'inserted']
                },
                { 'insert_orderDetail4' :
                ['INSERT INTO orderDetails VALUES (NULL, 10249, 2, 9)', 'inserted']
                },
                { 'insert_orderDetail5' :
                ['INSERT INTO orderDetails VALUES (NULL, 10249, 6, 40)', 'inserted']
                },
                { 'insert_orderDetail6' :
                ['INSERT INTO orderDetails VALUES (NULL, 10250, 1, 10)', 'inserted']
                },
                { 'insert_orderDetail7' :
                ['INSERT INTO orderDetails VALUES (NULL, 10250, 5, 35)', 'inserted']
                },
                { 'insert_orderDetail8' :
                ['INSERT INTO orderDetails VALUES (NULL, 10250, 7, 15)', 'inserted']
                },
                { 'insert_orderDetail9' :
                ['INSERT INTO orderDetails VALUES (NULL, 10251, 6, 6)', 'inserted']
                },
                { 'insert_orderDetail10' :
                ['INSERT INTO orderDetails VALUES (NULL, 10252, 8, 15)', 'inserted']
                },
                { 'show_suppliers' :
                ['SELECT * FROM suppliers', None]
                },
                { 'show_orders' :
                ['SELECT * FROM Orders', None]
                },
                { 'show_shippers' :
                ['SELECT * FROM shippers', None]
                },
                { 'show_employees' :
                ['SELECT * FROM employees', None]
                },
                { 'show_orderDetails' :
                ['SELECT * FROM orderDetails', None]
                },
                { 'delete' :
                ['DELETE FROM stocks WHERE date="2020-11-18"', 'deleted']
                },
                { 'select_country' :
                ['SELECT Country from customers', None]
                },
                { 'select_distinct_country' :
                ['SELECT DISTINCT Country from customers', None]
                },
                { 'count_countrys' :
                ['SELECT COUNT(DISTINCT Country) from customers', None]
                },
                { 'count_rows' :
                ['SELECT COUNT(*) from customers', None]
                },
                { 'show_stocks' :
                ['SELECT * FROM stocks ORDER BY "price"', None]
                },
                { 'show_customers' :
                ['SELECT * FROM customers', None]
                },
                { 'show_stock_ids' :
                ['SELECT _rowid_ FROM stocks', None]
                },
                { 'show_all_tables' :
                ['SELECT name FROM SQLITE_SCHEMA WHERE type="table" ORDER BY name', None]
                },
                { 'select_mexico' :
                ['SELECT * FROM customers WHERE Country="Mexico"', None]
                },
                { 'select_mexico_and_5021' :
                ['SELECT * FROM customers WHERE Country="Mexico" AND PostalCode="5021"', None]
                },
                {'select_mexico_or_germany' :
                ['SELECT * FROM customers WHERE Country="Mexico" OR Country="Germany"', None]
                },
                {'select_not_mexico' :
                ['SELECT * FROM customers WHERE NOT Country="Mexico"', None]
                },
                {'select_combo' :
                ['SELECT * FROM customers WHERE Country="Germany" AND (City="München" OR City="Aachen")', None]
                },
                {'select_not_combo' :
                ['SELECT * FROM customers WHERE NOT Country="Germany" AND NOT Country="Mexico"', None]
                },
                {'order_id' :
                ['SELECT * FROM customers ORDER BY CustomerID', None]
                },
                {'order_id_desc' :
                ['SELECT * FROM customers ORDER BY CustomerID DESC', None]
                },
                {'order_country_name' : # order by Country then by CustomerName
                ['SELECT * FROM customers ORDER BY Country, CustomerName', None]
                },
                {'update1' : 
                ['UPDATE customers SET ContactName="Alfred Schmidt", City="Frankfurt" WHERE CustomerID = 1', "updated"]
                },
                {'update_multi' : 
                ['UPDATE customers SET City="Mexico City" WHERE Country="Mexico"', "updated"]
                },
                {'update_all' : 
                ['UPDATE customers SET Country="Belarus"', "updated"]
                },
                {'del_alfred' : 
                ['DELETE FROM customers WHERE CustomerName="Alfreds Futterkiste"', "deleted"]
                },
                {'del_all_sweden' : 
                ['DELETE FROM customers WHERE Country="Sweden"', "deleted"]
                },
                {'del_all_customers' : 
                ['DELETE FROM customers', "deleted"]
                },
                {'limit_3' : 
                ['SELECT * FROM Customers LIMIT 3', None]
                },
                {'limit_2_ger' : 
                ['SELECT * FROM Customers WHERE Country="Germany" LIMIT 2', None]
                },
                {'show_products' : 
                ['SELECT * FROM Products', None]
                },
                {'min_product' : 
                ['SELECT MIN(Price) AS SmallestPrice FROM Products', None]
                },
                {'max_product' : 
                ['SELECT MAX(Price) AS LargestPrice FROM Products', None]
                },
                {'avg_products' : 
                ['SELECT AVG(Price) FROM Products', None]
                },
                {'sum_products' : 
                ['SELECT SUM(Price) FROM Products', None]
                },
                {'start_a' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "a%"', None]
                },
                {'end_a' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "%a"', None]
                },
                {'any_or' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "%or%"', None]
                },
                {'second_r' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "_r%"', None]
                },
                {'start_a_2' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "a_%"', None]
                },
                {'start_a_3' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "a__%"', None]
                },
                {'startend_a_o' : 
                ['SELECT * FROM Customers WHERE CustomerName LIKE "a%o"', None]
                },
                {'start_bsp' : 
                ['SELECT * FROM Customers WHERE City LIKE "[bsp]%"', None]
                },
                {'start_a_h' : 
                ['SELECT * FROM Customers WHERE City LIKE "[a-h]%"', None]
                },
                {'in' : 
                ['SELECT * FROM Customers WHERE Country IN ("Mexico", "Sweden", "UK")', None]
                },
                {'not_in' : 
                ['SELECT * FROM Customers WHERE Country NOT IN ("Mexico", "Sweden", "UK")', None]
                },
                {'between' : 
                ['SELECT * FROM Products WHERE Price BETWEEN 10 AND 20', None]
                },
                {'not_between' : 
                ['SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20', None]
                },
                {'between_dates' : 
                ['SELECT * FROM Orders WHERE OrderDate BETWEEN "1996-07-01" AND "1996-07-31"', None]
                },
                {'alias' : 
                ['SELECT CustomerID AS ID, CustomerName AS Customer FROM Customers', None]
                },
                {'table_alias' : 
                ['SELECT o.OrderID, o.OrderDate, c.CustomerName FROM Customers AS c, Orders AS o WHERE c.CustomerName="Antonio Moreno Taquería" AND c.CustomerID=o.CustomerID', None]
                },
                {'join' : 
                ['SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID', None]
                },
                {'left_join' : 
                ['SELECT Customers.CustomerName, Orders.OrderID FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID ORDER BY Customers.CustomerName', None]
                },
                {'self_join' : 
                ['SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City FROM Customers A, Customers B WHERE A.CustomerID <> B.CustomerID AND A.City = B.City ORDER BY A.City', None]
                },
                {'union' : 
                ['SELECT City FROM customers UNION SELECT City FROM suppliers ORDER BY City', None]
                },
                {'union_all' : 
                ['SELECT City FROM customers UNION ALL SELECT City FROM suppliers ORDER BY City', None]
                },
                {'union2' : 
                ['SELECT "Customer" AS Type, ContactName, City, Country FROM customers UNION SELECT "Suppliers", ContactName, City, Country FROM suppliers', None]
                },
                {'group_by' : 
                ['SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country', None]
                },
                {'group_by_join' : 
                ['SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID GROUP BY ShipperName', None]
                },
                {'having' : 
                ['SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) >= 2', None]
                },
                {'having_order_by' : 
                ['SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) >= 2 ORDER BY COUNT(CustomerID) ASC', None]
                },
                {'having2' : 
                ['SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders FROM (Orders INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID) GROUP BY LastName HAVING COUNT(Orders.OrderID) >= 1', None]
                },
                {'exists' : 
                ['SELECT SupplierName FROM suppliers WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.SupplierID AND Price < 20)', None]
                },
                {'like_any' : 
                ['SELECT ProductName FROM Products WHERE ProductID IN (SELECT ProductID FROM orderDetails WHERE Quantity = 10)', None]
                },
                {'all' : 
                ['SELECT ALL ProductName FROM Products WHERE TRUE', None]
                },
                {'all2' : 
                ['SELECT ProductName FROM Products', None]
                },
                ]


def connect():
    con = sqlite3.connect(DATABASES / 'example_2.db')
    cur = con.cursor()

    return con, cur


def show(database_rows):
    for row in database_rows:
        print(row)


def main():
    con, cur = connect()
    cur.execute('''PRAGMA foreign_keys = ON''')
    print("enabled foreign key support")
    while True:
        try:
            is_command = False
            user_input = input('SQL-Command Name: ')
            if user_input == 'q':
                if con.in_transaction:
                    user_input = input('Do you want to commit your changes? (y/n): ')
                    if user_input == 'y':
                        con.commit()
                con.close()
                break
            if user_input == 'commit':
                con.commit()
                is_command = True
            if user_input == 'rollback':
                con.rollback()
                is_command = True
            for command in SQL_COMMANDS:
                if user_input in command:
                    com = command[user_input][0]
                    output =command[user_input][1]
                    database_rows = cur.execute(com)
                    if output is None:
                        show(database_rows)
                    else:
                        print(command[user_input][1])
                    is_command = True
                    break
            if is_command == False:
                print('Command does not exists.')
        except sqlite3.OperationalError as error:
            print(error)
        except sqlite3.IntegrityError as error:
            print(error)
    
    
            
                

if __name__ == '__main__':
    main()


# https://sqlite.org/lang_createtable.html
# https://sqlite.org/lang_select.html
# https://sqlite.org/faq.html#q7
# https://docs.python.org/3/library/sqlite3.html
# https://www.w3schools.com/sql/sql_select.asp
# Last: https://www.w3schools.com/sql/sql_select_into.asp