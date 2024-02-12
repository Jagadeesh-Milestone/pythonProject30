#display tables in a database
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
mycursor.execute('SHOW TABLES')
result=mycursor.fetchall()
for i in result:
    print(i)