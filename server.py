from bottle import route, run, template, request, Bottle
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json
import time

client = MongoClient('mongodb://ocl:ocl@13.126.64.71/ocl_test')

db = client.ocl_test

app = Bottle(__name__)

@app.route('/')
def root():
    return "Hello from Root!!"

@app.route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@app.route('/testinsert')
def test():
	data = request.GET.get('data')
	cur = db.test_data.insert({'data':data,'timestamp':time.time()})
	return dumps(cur)

@app.route('/testretrieve')
def test():
	data = request.GET.get('data')
	cur = db.test_data.find_one({'_id':ObjectId(data)})
	return dumps(cur)