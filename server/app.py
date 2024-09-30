#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# creating a route for the index function/page
@app.route("/")
def index():
    return "<h1>Welcome to my page!</h1>"

#creating a dynamic application 
# In the app.route surround the route with angle brackets <>
#What is inside the angle brackets should be passed as the parameter for the function
# You can specify the type in the angle brackets eg string, float, int e.t.c
@app.route("/<string:username>")
def user(username):
    return f"<h1>Profile for {username}</h1>"


# using the app.run() method
if __name__ == "__main__":
    app.run(port=5555, debug=True)