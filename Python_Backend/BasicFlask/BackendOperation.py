from flask import Flask
from requests import request


app =Flask(__name__)

@app.route('/')
def add():
    a = 10
    b = 20 
    c = a+b
    return str(c)

'''Note : When you return any value That should be in String , 
if any other type fo type casting because to display the result in the UI'''



if __name__ == "__main__":
    app.run(debug=True)