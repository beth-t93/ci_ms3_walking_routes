
import os
import bcrypt

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


''' Takes users to the main page index.html '''
@app.route("/")
def trails():
    print(os.environ.get("MONGO_URI"))
    trails = list(mongo.db.trails.find())
    print(trails)
    return render_template("index.html", trails=trails)


''' Allows users to register an account, also checks to see if the username has already been used '''
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('trails'))
        
        return 'That username already exists!'

    return render_template('register.html')


''' Allows an exisiting user to login, will also check for correct username and password'''
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), existing_user['password'].encode('utf-8')) == existing_user['password'].encode('utf-8'):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


'''
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    trails = list(mongo.db.trails.find())
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    if session["username"]:
        return render_template("profile.html", trails=trails, username=username)
    else:
        return redirect(url_for("login"))
'''


@app.route("/add_trail", methods=["GET", "POST"])
def add_trail():
    if request.method == "POST":
        trail = {
            "trail_name": request.form.get("trail_name"),
            "description": request.form.get("description"),
            "terrain": request.form.get("terrain"),
            "postcode": request.form.get("postcode"),
            "created_by": session["username"]
        }
        mongo.db.trails.insert_one(trail)
        flash("Route added!")
        return redirect(url_for("trails"))
    return render_template("add_trail.html")


@app.route("/edit_trails/<trails_id>", methods=["GET", "POST"])
def edit_trails(trails_id):
    trails = mongo.db.trails.find_one({"_id": ObjectId(trails_id)})
    return render_template("edit_trail.html", trails=trails)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

