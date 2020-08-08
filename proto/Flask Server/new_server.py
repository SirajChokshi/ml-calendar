import pyrebase
import os
from flask import *
from flask import Flask, request

import pickle

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

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to ML Time Finder"

# ----------------

@app.route("/create_user/<string:username>", methods=['POST'])
def create_user(username):
    gradient = SGDRegressor()
    with open('{}.pkl'.format(username), 'wb') as fid:
        pickle.dump(gradient, fid)
    return "file created for user: {}".format(username)

@app.route("/load_model/<string:username>", methods=['GET'])
def load_model(username):
    with open('{}.pkl'.format(username), 'rb') as fid:
        model = pickle.load(fid)
    # the return is just temporary, im not sure what to replace it with yet
    return str(model.intercept_)

@app.route("/update_model/<string:username>", methods=['POST'])
def update_model(username):
    json_input = request.get_json()
    with open('{}.pkl'.format(username), 'rb') as fid:
        model = pickle.load(fid)

    X = json_input["X"]
    Y = json_input["Y"]

    newX = np.array(X)
    newY = np.array(Y)
    model.partial_fit(newX, newY)

    with open('{}.pkl'.format(username), 'wb') as fid:
        pickle.dump(model, fid)

    return "regressor updated for user: {}".format(username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 