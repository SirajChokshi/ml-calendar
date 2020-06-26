import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./FirebaseServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

# posting the data
doc_ref = db.collection('user').document('akasar')

doc_ref.set({
    "name" : "A",
    "last name" : "K"
})

#retrieving the data

user_ref = db.collection('user')
docs = user_ref.stream()

for doc in docs:
    print("{} => {}".format(doc.id, doc.to_dict()))
