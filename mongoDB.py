from xml.sax.handler import property_interning_dict

import pymongo #llibary
import datetime

from requests import delete

#connection string
Client = pymongo.MongoClient("mongodb+srv://srinivasan:4FOEjoiP6kFsvRAr@pythonfordatabases.xj9xzln.mongodb.net/?retryWrites=true&w=majority&appName=PythonForDatabases")

#database
hockeydb = Client["hockeyleage"]

#table or collection
playerstb = hockeydb["players"]

#single row
dictOne = {
    "_id": 1,
    "name": "John Smith",
    "birthdate": "02/08/2000",
    "nationality": "Canada",
    "games_played": 12,
    "goals": 8,
    "assists": 10,
    "total_points": 18,
    "team_id": 1
}

#insert single
#ins = playerstb.insert_one(dictOne)

listMany = [
    {
        "_id": 2,
        "name": "Emily Johnson",
        "birthdate": "02/08/2000",
        "nationality": "USA",
        "games_played": 11,
        "goals": 3,
        "assists": 3,
        "total_points": 6,
        "team_id": 1
    },
    {
        "_id": 3,
        "name": "Michael Brown",
        "birthdate": "02/08/2000",
        "nationality": "USA",
        "games_played": 12,
        "goals": 16,
        "assists": 1,
        "total_points": 17,
        "team_id": 1
    }
]

#insert many
#ins2 = playerstb.insert_many(listMany)

#selecting one row
#print(playerstb.find_one())

#selecting multiple rows
#for i in playerstb.find().limit(1):
#    print(i)


#select with where clause
#where = {'goals' : 16}

#for i in playerstb.find(where):
#    print(i)


#update in mongoDB (easy)
#where = {'nationality' : 'USA'}
#update = {"$set" : {'team_id' : 10}}

#a = playerstb.update_many(where,update)

#for  i in playerstb.find():
#    print(i)

#deleting a row in mongoDB
deletee = {'goals' : 16}

a = playerstb.delete_many(deletee)

for i in playerstb.find():
    print(i)