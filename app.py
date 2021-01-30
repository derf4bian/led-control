# app.py
from flask import Flask, render_template

app = Flask(__name__)

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return render_template("index.html")

@app.route("/home")
def second():
    return render_template("home.html")

app.run(debug = True)