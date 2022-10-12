# Put your app in here.
from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

@app("/add")
def add_a_to_b():
    a = int(request.args["a"])
    b = int(request.args["b"])
    #a,b = request.args["a","b"] ???
    #result = operations.add(a,b)
    result = add(a,b)
    html = f"<p>{a} + {b} = {result}</p>"
    return html

@app("/sub")
def sub_b_from_a():
    a = int(request.args["a"])
    b = int(request.args["b"])
    #a,b = request.args["a","b"] ???
    result = sub(a,b)
    html = f"<p>{a} - {b} = {result}</p>"
    return html

@app("/mult")
def multiply_a_by_b():
    a = int(request.args["a"])
    b = int(request.args["b"])
    #a,b = request.args["a","b"] ???
    result = mult(a,b)
    html = f"<p>{a} * {b} = {result}</p>"
    return html

@app("/div")
def divide_a_by_b():
    a = int(request.args["a"])
    b = int(request.args["b"])
    #a,b = request.args["a","b"] ???
    result = div(a,b)
    html = f"<p>{a} / {b} = {result}</p>"
    return html