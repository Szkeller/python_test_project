# sample of MYSQL connection & database creation

import mysql.connector

db= mysql.connector.connect(user='root', password='123456', host='localhost')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()