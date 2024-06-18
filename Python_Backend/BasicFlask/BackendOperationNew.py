from flask import Flask
from requests import request


app =Flask(__name__)

@app.route('/')
def home():
    return "Hi ,Welcome to Backend Technology"

@app.route('/concat')
def add():
    a = "10"
    b = "20" 
    c = a+b
    return c

@app.route('/mul')
def mul():
    a = 10
    b = 20 
    c = a*b
    return str(c) 


if __name__ == "__main__":
    app.run(debug=True)