import os
import datetime
import pymongo
from pymongo import MongoClient
 
# Grab our connection information from the MONGOHQ_URL environment variable
# (mongodb://linus.mongohq.com:10045 -u username -pmy_password)

MONGOHQ_URL= "mongodb://tanay:tanay@oceanic.mongohq.com:10049/artists"

# https://api.mongolab.com/api/1/databases?apiKey=wrgSDhTRcpAhF5FBbzvpZSjq_q2zt_3f

# MONGO_URL = os.environ.get(MONGOHQ_URL)
# connection = Connection(MONGO_URL)
client = MongoClient(MONGOHQ_URL)
 
# Specify the database
db = client.artists
# Print a list of collections
print db.collection_names()
 
# Specify the collection, in this case 'monsters'
collection = db.artists
 
# Get a count of the documents in this collection
count = collection.count()
print "The number of documents you have in this collection is:", count
 
# Create a document for a monster
# monster = {"name": "Dracula",
#            "occupation": "Blood Sucker",
#            "tags": ["vampire", "teeth", "bat"],
#            "date": datetime.datetime.utcnow()
#            }
 
# # Insert the monster document into the monsters collection
# monster_id = collection.insert(monster)
 
# # Print out our monster documents
# for monster in collection.find():
#     print monster
 
# Query for a particular monster
# print collection.find_one({"name": "Dracula"})
