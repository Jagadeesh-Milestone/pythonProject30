#create a database.
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE narasimha')
print('new database created successfully')
