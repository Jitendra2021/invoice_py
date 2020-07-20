
import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='root', password='spark123',
                              host='127.0.0.1',
                              database='srl')
cursor = cnx.cursor()
query = "SELECT * FROM orgdetails"

cursor.execute(query, {'id': 456})
rows = cursor.fetchall()
print(rows)

print(type(rows))
cursor.close()
cnx.close()

