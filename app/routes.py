from app import app
from flask import jsonify
from app.view_data import view_sample_data

@app.route('/')
def hello_world():
	data = {'msg' : "Hello, world"}
	return jsonify(data)


@app.route('/head')
def head():
	json_data = view_sample_data('./data/table1')
	return jsonify(json_data)