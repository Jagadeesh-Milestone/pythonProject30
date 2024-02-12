#insert record into a table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha')
mycursor=mydb.cursor()
sql='INSERT INTO users (name,address) values(%s,%s)'
values=('mahesh','bangalore')
mycursor.execute(sql,values)
mydb.commit()
print(mycursor.rowcount,'record got inserted into a table')