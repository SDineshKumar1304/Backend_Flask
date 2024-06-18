from flask import Flask
from requests import request


app =Flask(__name__)

@app.route('/')
def add():
    a = "10"
    b = "20" 
    c = a+b
    return c



if __name__ == "__main__":
    app.run(debug=True)