import motor.motor_asyncio
import os
import pymongo

client = pymongo.MongoClient(os.environ["MONGODB_URL"])

if os.environ["API_TEST"]:
    db = client["testavist"]
else:    
    db = client["avist"]

def drop_database():
    client.drop_database("avist")