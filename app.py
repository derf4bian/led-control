# app.py
from flask import Flask, render_template, request



app = Flask(__name__)

# defining a route
@app.route('/', methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return render_template('index.html')

@app.route('/home')
def second():
    return render_template('home.html')

@app.route('/blue-fade')
def bluefade():
    return render_template('index.html')

@app.route('/green-fade')
def greenfade():
    return render_template('index.html')

@app.route('/red-fade')
def redfade():
    return render_template('index.html')

app.run(debug = True)