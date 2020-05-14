import pymongo
import os
import env

# @app.config["MONGO_URI"] = os.getenv('MONGO_URI', "env value not loaded")

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]



                  #  To add many records:
# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not_much',
#              'occupation': 'writer', 'nationality': 'english'},
#             {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white',
#              'occupation': 'writer', 'nationality': 'american'}]

# coll.insert_many(new_docs)



                    #  To add one record:
# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey',
#              'occupation': 'writer', 'nationality': 'english'}

# coll.insert(new_doc)


                    #  to find all:
# documents = coll.find()

                    #  to find particular record:
# documents = coll.find({'first': 'douglas'})         

                    # to remove one record:
# coll.delete_one({'first': 'stan'})

                    # to update one record:
                    # first argument is a search string, to find all with certain type key:value pair,
                    # then we use $set: keyword and after that another dictionary, with the change that we want to pass
# coll.update_one({'nationality': 'american'}, {'$set':{'hair_colour': 'maroon'}})

                    # To update many:
#coll.update_many({'nationality': 'american'}, {'$set':{'hair_colour': 'maroon'}})

documents = coll.find()

for doc in documents:
    print(doc)
