
import os

from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ, path
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".env")
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["IP"] = os.environ.get("IP")
app.config["PORT"] = os.environ.get("PORT")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def trails():
    print(os.environ.get("MONGO_URI"))
    trails = list(mongo.db.trails.find())
    print(trails)
    return render_template("index.html", trails=trails)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

