
import os

from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ, path
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


SECRET_KEY = os.environ.get("SECRET_KEY")
IP = os.environ.get("IP")
PORT = os.environ.get("PORT")
MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DBNAME = os.environ.get("MONGO_DBNAME")


app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def index():
    """
    Returns to index.html
    """
    return render_template("index.html")


@app.route("/")
def trails():
    trails = list(mongo.db.trails.find())
    return render_template("index.html", trails=trails)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

