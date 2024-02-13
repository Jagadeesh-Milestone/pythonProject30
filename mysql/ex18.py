#delete record:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
#mycursor.execute('DELETE FROM users WHERE address="Delhi"')
#mycursor.execute('DELETE FROM users WHERE id="100"')
mycursor.execute('DELETE FROM users WHERE name="hari"')
mydb.commit()
print(mycursor.rowcount,'records are deleted')
