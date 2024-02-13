#fetch particular columns:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT id,name FROM users')
result=mycursor.fetchall()
for i in result:
    print(i)
    print('hello world')