#insert multiple records into a table.
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='narasimha'
)
mycursor=mydb.cursor()
sql='INSERT INTO users(name,address) values(%s,%s)'
values=[('hari','bangalore'),('manoj','hyderabad'),
         ('suresh','chennai'),('sayed','mumbai'),
         ('balaji','andhra')]
mycursor.executemany(sql,values)
print(mycursor.rowcount,'records are added into a table')
mydb.commit()