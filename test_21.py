# sample of update mothod for MongoDB

import pymongo

client = pymongo.MongoClient(host = '127.0.0.1', port = 27017, connect=False)

db=client.test

collection = db.students

condition={'name':'Mike'}

student=collection.find_one(condition)
student['age']=25
result = collection.update(condition, student)
print(result)
