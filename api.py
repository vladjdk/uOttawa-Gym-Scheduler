from flask import Flask, request
import scheduler
import pickle as pk
import json

app = Flask(__name__)


@app.route('/')
def hello():
    print("Hello")
    return "Hello"


@app.route('/login', methods=['GET', 'POST'])
def login():
    return request.values.get("username")
