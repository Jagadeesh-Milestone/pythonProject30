#create a table in a existing database:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE students (name VARCHAR(30),address VARCHAR(40))')
print('one table created successfully')