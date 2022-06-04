import pymongo 
import os
from info import DATABASE_URI, DATABASE_NAME

DB_NAME = DATABASE_NAME
DB_URL = DATABASE_URI
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def setWelcome(group_id, welcome):
    dbcol.update_one({"_id": group_id},{"$set":{"welcome": welcome}})
	
