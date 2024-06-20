from flask import Flask,request,render_template


app = Flask(__name__)


@app.route('/index')
def home():
    return render_template('index.html')



@app.route('/')
def index():
    return "🥸Hello Coder👨‍💻"

if  __name__ == "__main__":
    app.run(debug=True)