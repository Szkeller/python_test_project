# sample of MongoDB

import pymongo

client = pymongo.MongoClient(host = '127.0.0.1', port = 27017, connect=False)

db=client.test

collection = db.students

student1 ={
    'id':'20170101',
    'name': 'Jorden1',
    'age':20,
    'gender':'male'
}

student2 ={
    'id':'20170102',
    'name': 'Mike',
    'age':21,
    'gender':'male'
}

result=collection.insert_many([student1,student2])
print(result)
print(result.inserted_ids)