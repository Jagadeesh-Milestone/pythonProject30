#connect to mysql.
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)

print('connected to mysql succesfully')