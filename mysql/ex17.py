#update records:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('UPDATE users SET address="delhi" WHERE address="mumbai"')
mycursor.execute('UPDATE users SET name="giri" WHERE id="100"')

mydb.commit()
print(mycursor.rowcount,'records got affected')