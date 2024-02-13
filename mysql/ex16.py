#limit the result:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('SELECT * FROM users LIMIT 5')
mycursor.execute('SELECT * FROM users LIMIT 5 OFFSET 4')
result=mycursor.fetchall()
for i in result:
    print(i)