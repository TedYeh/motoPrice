from flask import Flask, render_template, request
from location import location

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/location")
def location_function():
    return location()
