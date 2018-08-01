# sample of MYSQL table creation

import mysql.connector

db=mysql.connector.connect(user='root', password='123456', host='localhost', database='spiders')

cursor=db.cursor()

sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, ' \
     'PRIMARY KEY(id))'

cursor.execute(sql)

db.close()