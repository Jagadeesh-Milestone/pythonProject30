#sort the records:
import  mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('SELECT * FROM users ORDER BY name')
#mycursor.execute('SELECT * FROM users ORDER BY address')
#mycursor.execute('SELECT * FROM users ORDER BY name DESC')
#mycursor.execute('SELECT * FROM users ORDER BY address DESC')
mycursor.execute('SELECT * FROM users ORDER BY id DESC')
result=mycursor.fetchall()
for i in result:
    print(i)