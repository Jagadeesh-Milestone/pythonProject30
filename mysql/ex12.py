#select with a filter:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('SELECT * FROM users WHERE address="bangalore"')
mycursor.execute('SELECT * FROM users WHERE name="hari"')
result=mycursor.fetchall()
for i in result:
    print(i)


print('hello world')