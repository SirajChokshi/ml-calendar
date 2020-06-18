import pyrebase
from flask import *
from flask import Flask

config = {
    "apiKey": "AIzaSyABxv8e7n4Wns-0rXDVGDI3V6vCjSFq8VU",
    "authDomain": "ml-calendar-a454d.firebaseapp.com",
    "databaseURL": "https://ml-calendar-a454d.firebaseio.com",
    "projectId": "ml-calendar-a454d",
    "storageBucket": "ml-calendar-a454d.appspot.com",
    "messagingSenderId": "1095759067582",
    "appId": "1:1095759067582:web:8c98359c27d1fde93f21ef"
}

firebase = pyrebase.initialize_app(config)

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
    return "{} has been authenticated".format(username)


# DEALING WITH DATA --------

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 

