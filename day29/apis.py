from flask import Flask,  Response, request
from datetime import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from pathlib import Path
from dotenv import load_dotenv
import json
import pymongo
import os

app = Flask(__name__)

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

MANGODB_URI = os.environ['MONGODB_URI']
client = pymongo.MongoClient(MANGODB_URI)
db = client['thirty_days_of_python']

@app.route('/api/v1.0/students', methods = ['GET'])
def students():
    all_students = db.students.find()
    return Response(dumps(all_students), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student(id):
    student = db.students.find_one({"_id": ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    created_at = datetime.now()
    student = {
        'name': name,
        'age': age,
        'country': country,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return Response(dumps({'result': 'success'}), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
def update_student (id):
    name = request.form['name']
    country = request.form['country']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    created_at = datetime.now()
    student = {
        'name': name,
        'age': age,
        'country': country,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }

    db.students.update_one(student)
    return Response(dumps({'result': 'success'}), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return Response(dumps({'result': 'success'}), mimetype='application/json')

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)