#delete table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('DROP TABLE IF EXISTS users')
#mycursor.execute('DROP TABLE IF EXISTS employees')
#mycursor.execute('DROP DATABASE narasimha')
print('hello world')
