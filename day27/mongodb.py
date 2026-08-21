import pymongo
import os

from pathlib import Path
from dotenv import load_dotenv
from bson.objectid import ObjectId

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

MANGODB_URI = os.environ['MONGODB_URI']
client = pymongo.MongoClient(MANGODB_URI)

db = client['thirty_days_of_python'] # accessing the database
db.students.find().limit(1)

db.students.drop()

query = {
    "country":"Finland"
}
students = db.students.find(query)
for student in students:
    print(students)

query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

students = db.students.find().sort('name')
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
    print(student)

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)