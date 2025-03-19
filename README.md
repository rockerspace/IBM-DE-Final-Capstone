# IBM-DE-Final-Capstone
**Module 1**
OLTP Database- MySQL 8.0.22
phpMyAdmin 5.0.4 
design the schema for OLTP database.
load data into OLTP database.
automate admin tasks.


Task 3 - Import the data in the file oltpdata.csv
Task 4 - List the tables in the database sales.
Write a query to find out the count of records in the tables sales_data.
Task 5. Write a query to find out the count of records in the tables sales_data.
Task 6 - Create an index
Create an index named ts on the timestamp field.

Task 8 - Write a bash script to export data.
Write a bash script named datadump.sh that exports all the rows in the sales_data table to a file named sales_data.sql

Take a screenshot of the contents of the datadump.sh bash file command you used and the output. Also save the code in a text document for later use.

Name the screenshot as exportdata.jpg. (images can be saved with either .jpg or .png extension)


**Module 2 **

Querying Database in NOSQL
You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.
Task 1 - Import ‘catalog.json’ into mongodb server into a database named ‘catalog’ and a collection named ‘electronics’
Task 2 - List out all the databases
Take a screenshot of the command you used and the output.

Name the screenshot as list-dbs.jpg. (images can be saved with either .jpg or .png extension)

Task 3 - List out all the collections in the database catalog.
Take a screenshot of the command you used and the output.

Name the screenshot as list-collections.jpg. (images can be saved with either .jpg or .png extension)

Task 4 - Create an index on the field “type”
Take a screenshot of the command you used and the output.

Name the screenshot as create-index.jpg. (images can be saved with either .jpg or .png extension)

Task 5 - Write a query to find the count of laptops
Take a screenshot of the command you used and the output.

Name the screenshot as mongo-query-laptops.jpg. (images can be saved with either .jpg or .png extension)

Task 6 - Write a query to find the number of smart phones with screen size of 6 inches.

Task 7. Write a query to find out the average screen size of smart phones.
Take a screenshot of the command you used and the output.

Name the screenshot as mongo-query-mobiles2.jpg. (images can be saved with either .jpg or .png extension)

Task 8 - Export the fields _id, “type”, “model”, from the ‘electronics’ collection into a file named electronics.csv
Take a screenshot of the command you used and the output.

Name the screenshot as mongoexport.jpg. (images can be saved with either .jpg or .png extension)

**Module 3**
Data Warehousing 

You will start your project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. Name your database as softcart
Exercise 1 - Design a Data Warehouse
The ecommerce company has provied you the sample data.



You will start your project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. Name your database as softcart

Task 1 - Design the dimension table softcartDimDate
Using the ERD design tool design the table softcartDimDate. The company is looking at a granularity of a day. Which means they would like to have the ability to generate the report on yearly, monthly, daily, and weekday basis.

Here is a partial list of fields to serve as an example:

dateid

month

monthname

…

…

Take a screenshot of the table softcartDimDate in the ERD tool clearly showing all the fieldnames and data types.

Name the screenshot softcartDimDate.jpg. (Images can be saved with either the .jpg or .png extension.)

Task 2 - Design the dimension table softcartDimCategory
Using the ERD design tool design the table softcartDimCategory.

Task 3 - Design the dimension table softcartDimItem
Using the ERD design tool design the table softcartDimItem.

Task 4 - Design the dimension table softcartDimCountry
Using the ERD design tool design the table softcartDimCountry.

Take a screenshot clearly showing all three tables(softcartDimCategory, softcartDimItem, softcartDimCountry) in the ERD tool with all the fieldnames and data types. Name the screenshot dimtables.jpg. (Images can be saved with either the .jpg or .png extension.)

Task 5 - Design the fact table softcartFactSales
Using the ERD design tool design the table softcartFactSales.

Take a screenshot of the table softcartFactSales in the ERD tool clearly showing all the fieldnames and data types.

Name the screenshot softcartFactSales.jpg. (Images can be saved with either the .jpg or .png extension.)

Task 6 - Design the relationships
Using the ERD design tool design the required relationships(one-to-one, one-to-many etc) amongst the tables.

Take a screenshot of the entire ERD clearly showing all the relationships amongst the tables.

Name the screenshot softcartRelationships.jpg. (Images can be saved with either the .jpg or .png extension.)

Task 7 - Create the schema.
Download the schema sql from ERD tool and create the schema in a database named staging.

Take a screenshot showing the success of the schema creation.

Name the screenshot createschema.jpg. (Images can be saved with either the .jpg or .png extension.)


