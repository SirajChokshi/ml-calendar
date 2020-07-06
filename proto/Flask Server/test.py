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

user = None

email = input("Please enter your email\n")
password = input("Please enter your password\n")

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)
print(user)

user = auth.sign_in_with_email_and_password(email, password)
print(user['idToken'])

print("\n\n", auth.get_account_info(user['idToken']), "\n")

username = "sirajtest"

if user is None:
    print ("Error: User Not Autheticated")
else:
    data = {
        "name": username,
        "desc": "description"
    }
    db.child("user").child(username).set(data, user['idToken'])
    print("{} user information has been updated".format(username))