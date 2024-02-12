#alter the existing table
#we can add the new columns to existing tables by using 'ALTER'
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
mycursor.execute('ALTER TABLE employees ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY')
print('table got altered')