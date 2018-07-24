#sample of insert record into mysql table by dict.
import mysql.connector

db=mysql.connector.connect(user='root', password='123456', host='localhost', database='spiders')

cursor=db.cursor()

data = {
    'id':'2018072002',
    'name':'Lee',
    'age': 21
}

table = 'students'

keys=','.join(data.keys())
values = ','.join(['%s']*len(data))

sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:
    cursor.execute(sql, tuple(data.values()))
    print('successful')
    db.commit()
except:
    print('failed')
    db.rollback()

db.close()