#primary key:
#while we creating a table we should also create a column with a
#unique key for each record.
#this can be done by defining a 'PRIMARY KEY'.
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20),address VARCHAR(30))')
print('one table created successfully')
