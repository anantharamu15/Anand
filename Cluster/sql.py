import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def setWelcome(group_id, welcome):
    dbcol.update_one({"_id": group_id},{"$set":{"welcome": welcome}})
	
