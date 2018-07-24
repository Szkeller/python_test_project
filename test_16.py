#sample of insert record into mysql tables
import mysql.connector

db=mysql.connector.connect(user='root', password='123456', host='localhost', database='spiders')

cursor=db.cursor()

id='20180720'
name = 'Bob'
age=20

sql='INSERT INTO students(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id,name,age))
    db.commit()
except:
    db.rollback()

db.close()