#sample of remove mothod of MongoDB

import pymongo

client = pymongo.MongoClient(host = '127.0.0.1', port = 27017, connect=False)

db=client.test

collection = db.students

condition = {'name':'Jordan2'}

result=collection.remove(condition)

print(result)