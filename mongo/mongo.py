import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb
users = db.users
user1 = {"username":"nick", "password":"password123","favorite_number":445,"hobbies":["pyhon","games","pizza"]}
user_id = users.insert_one[user1].inserted_id

