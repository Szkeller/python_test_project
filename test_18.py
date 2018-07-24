# sample of mongoDB

import pymongo

client = pymongo.MongoClient(host = '127.0.0.1', port = 27017, connect=False)

db=client.test

collection = db.students

student = {
    'id':'20170103',
    'name': 'Jordan2',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_one(student)

print(result)
