# sample of MongoDB

import pymongo

client = pymongo.MongoClient(host = '127.0.0.1', port = 27017, connect=False)

db=client.test

collection = db.students

results=collection.find({'age':{'$gte':20}})
#print(type(results))
print(results)
for result in results:
    print(result)