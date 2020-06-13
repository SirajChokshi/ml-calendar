import pyrebase
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to ML Time Finder"

@app.route("/data", methods=['GET'])
def get_user_info():
    # will get info on the SGD regressor of a particular user
    return "sample user information"


@app.route("/postdata", methods=['POST'])
def post_user_info():
    # will do something to post a new data point into the SGD regressor
    return "sample user information has been updated"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 

