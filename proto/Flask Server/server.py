import pyrebase
import os
from flask import *
from flask import Flask
from flask import requests

from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, mean_absolute_error
from numpy import random
from sklearn.model_selection import train_test_split

config = {
  "apiKey" : "AIzaSyABxv8e7n4Wns-0rXDVGDI3V6vCjSFq8VU",
  "authDomain" : "ml-calendar-a454d.firebaseapp.com",
  "databaseURL" : "https://ml-calendar-a454d.firebaseio.com",
  "projectId" : "ml-calendar-a454d",
  "storageBucket" : "ml-calendar-a454d.appspot.com",
  "messagingSenderId" : "1095759067582",
  "appId" : "1:1095759067582:web:8c98359c27d1fde93f21ef"
}

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

sample_data = "sample"

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

db = firebase.database()

auth = firebase.auth()

email = input("Please enter your email\n")
password = input("Please enter your password\n")

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to ML Time Finder"

# AUTHENTICATION --------

@app.route("/createnewauth/<string:username>", methods=['POST'])
def create_new_auth(username):
    # authenticate user
    auth.create_user_with_email_and_password(email, password)
    return "{} has been authenticated".format(username)

@app.route("/signinauth/<string:username>", methods=['POST'])
def sign_in_auth(username):
    # authenticate user
    auth.sign_in_with_email_and_password(email, password)
    return "{} has been signed in".format(username)


# DEALING WITH DATABASE --------

@app.route("/data", methods=['GET'])
def get_user_info():
    # will get info on the SGD regressor of a particular user
    return "sample user information"


@app.route("/postdata", methods=['POST'])
def post_user_info():
    # will do something to post a new data point into the SGD regressor
    return "sample user information has been updated"

@app.route("/postdata/<string:username>", methods=['POST'])
def post_info(username):
    # will do something to post a new data point into the SGD regressor
    return "{} user information has been updated".format(username)

@app.route("/createuser/<string:username>", methods=['POST'])
def create_user(username):
    # will do something to post a new data point into the SGD regressor
    db.child("users").push({"user" : username})
    return "{} user information has been updated".format(username)

# FIREBASE STORAGE -------------

@app.route("/createfolder/<string:username>", methods=['POST'])
def create_folder(username):
    # I'm not sure how to just create a folder, I had to add this sample.txt file
    storage.child(username).put("sample.txt")
    return "{} user information has been updated".format(username)

@app.route("/getURL/<string:username>", methods=['GET'])
def get_url(username):
    # getting the URL
    url = storage.child(username).get_url(False)
    return str(url)

# upload data, PATCH 
# - we go into the user's folder and pull down their existing model (which is compressed)
# - then we decompress it and partial fit the new data and get a new model
# - then we compress it again and send it 

@app.route("/upload_data/<string:username>", methods=['PATCH'])
def upload_data(username):
    # getting the URL
    url = storage.child(username).get_url(False)
    return str(url)





# ----------------

# need code to update the current regressor with the new data and partial fit

@app.route("/receive_data/<string:username>", methods=['GET'])
def receive_data(username):
    # getting the URL
    f = open('{}.txt'.format(username), 'w')

    url = storage.child(username).get_url(False)
    return str(url)


# need code to get the data 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 

