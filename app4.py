import uuid
from flask import Flask, jsonify, request
import json
import bookdb

# f = open("books.json")
# BOOKS = json.load(f)
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify ('pong!')

@app.route('/books', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    response_object['books'] = bookdb.getBooks()
    return jsonify(response_object)


app.run()