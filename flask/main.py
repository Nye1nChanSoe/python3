from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

@app.route('/<int:val1>/<int:val2>', methods=['GET'])
def calculate_sum_of_squares(val1: int, val2: int):
    result = val1**2 + val2**2
    return jsonify({"val1": val1, "val2": val2, "result": result})