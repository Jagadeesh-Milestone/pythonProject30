#display the available databases in our workbench
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
result=mycursor.fetchall()
for i in result:
    print(i)