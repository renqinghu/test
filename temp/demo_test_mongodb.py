import pymongo
myclient = pymongo.MongoClient("mongodb://aiops:aiops@192.168.115.41:27017/")
db = myclient.aiops
connector = db.anomaly.service

print(connector.find().count())

for i in connector.find():
    print(i)