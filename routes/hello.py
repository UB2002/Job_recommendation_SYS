# routes/hello.py

from flask import Blueprint

# Initialize the blueprint
hello = Blueprint("hello", __name__)

@hello.route("/", methods=["GET"])
def hello_world():  # Renamed function to avoid conflict
    return "Hello, World!"
