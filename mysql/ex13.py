#select records using wild card characters:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('SELECT * FROM users WHERE name LIKE "%sh%"')
mycursor.execute('SELECT * FROM users WHERE address LIKE "%ai%"')
result=mycursor.fetchall()
for i in result:
    print(i)
print('hello world')