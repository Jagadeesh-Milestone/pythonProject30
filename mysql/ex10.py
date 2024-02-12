#select all the records from a table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM users')
#result=mycursor.fetchone()#for the single record
result=mycursor.fetchall()#for all the records
for i in result:
    print(i)