import pyrebase

config = {
  "apiKey" : "AIzaSyABxv8e7n4Wns-0rXDVGDI3V6vCjSFq8VU",
  "authDomain" : "ml-calendar-a454d.firebaseapp.com",
  "databaseURL" : "https://ml-calendar-a454d.firebaseio.com",
  "projectId" : "ml-calendar-a454d",
  "storageBucket" : "ml-calendar-a454d.appspot.com",
  "messagingSenderId" : "1095759067582",
  "appId" : "1:1095759067582:web:8c98359c27d1fde93f21ef"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

storage.child("images/newimage.png").put("bear.png")

print("image uploaded")