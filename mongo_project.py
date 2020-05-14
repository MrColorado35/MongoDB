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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit ")

    option = input("Enter option: ")
    return option

#               Here we receiving our document        
def get_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database!")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc

# Here we are adding one record to our database
def add_record():
    print("")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter date of birth (DD/MM/YYYY): ")
    gender = input("Enter gender: ")
    hair_colour = input("Enter hair colour: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")

    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 
                'occupation': occupation, 'nationality': nationality}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted!")
    except:
        print("Error accessing the database! Whole world will burn in 3... 2... 1.. au")

# To find one record, using our get_record function:        

def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

# To edit our record:

def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "]: ")
                #now if we did not put any information for some key=value pairs, we don't want it to disappear:
                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated! Great job Stan! \n Computers love you! ")
        except:
            print("Error accessing the database. You unlucky, poor human. Don't play lotto tonight.")

# To delete record:

def delete_record():

    doc = get_record()

    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
            
        print("")
        confirmation = input("Is this the document you want to delete?\n Y or N >")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")


# Main loop gives us our menu. It's a loop that will bring it back on the end of every task, until 5 will be choosen
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()


