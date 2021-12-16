
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


''' Takes users to the main page index.html '''
@app.route("/")
def trails():
    trails = list(mongo.db.trails.find())
    return render_template("index.html", trails=trails)


''' Allows users to register an account, also checks to see if the username has already been used '''
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = mongo.db.users
        active_user = user.find_one({'name' : request.form.get('username')})
        password = generate_password_hash(request.form['password'])
        if active_user is None:
            user.insert_one({'name' : request.form['username'],
                         'password' : password})
            session['username'] = request.form['username']
            return redirect(url_for('trails'))

        return 'That username already exists!'

    return render_template('register.html')


''' Allows an exisiting user to login, will also check for correct username and password'''
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = mongo.db.users
        login_user = user.find_one({'name' : request.form.get('username')})
        print(login_user)
        if login_user:
            if check_password_hash(login_user['password'], request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('trails'))
            flash('Incorrect Username/Password')
            return redirect(url_for('login'))
    return render_template("login.html")


''' Allows an exisiting user to access their profile page'''
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users
    found_user = user.find_one({"name": username})
    trails = list(mongo.db.trails.find({"created_by": username}))
    print(trails)
    if session["username"]:
        return render_template(
            "profile.html", username=found_user, trails=trails)

    return redirect(url_for("login"))


''' Will log a user out'''
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("username")
    return redirect(url_for("login"))


''' Allows an exisiting user to add a route to the site'''
@app.route("/add_trail", methods=["GET", "POST"])
def add_trail():
    if request.method == "POST":
        trail = {
            "image_url": request.form.get("image_url"),
            "trail_name": request.form.get("trail_name"),
            "terrain": request.form.get("terrain"),
            "start": request.form.get("start"),
            "end": request.form.get("end"),
            "description": request.form.get("description"),
            "created_by": session["username"]
        }
        mongo.db.trails.insert_one(trail)
        flash("Route added!")
        return redirect(url_for("trails"))
    return render_template("add_trail.html")


''' Allows an exisiting user to edit a route they have previously added to the site'''
@app.route("/edit_trails/<trails_id>", methods=["GET", "POST"])
def edit_trails(trails_id):
    if request.method == "POST":
        trail = {
            "image_url": request.form.get("image_url"),
            "trail_name": request.form.get("trail_name"),
            "terrain": request.form.get("terrain"),
            "start": request.form.get("start"),
            "end": request.form.get("end"),
            "description": request.form.get("description"),
            "created_by": session["username"]
        }

        mongo.db.trails.update({"_id": ObjectId(trails_id)}, trail)
        flash("Your route has been updated!")

    trails = mongo.db.trails.find_one({"_id": ObjectId(trails_id)})
    return render_template("edit_trail.html", trail=trails)


''' Allows users to delete a route they added to the site'''
@app.route("/delete_trails/<trails_id>")
def delete_trails(trails_id):
    mongo.db.trails.remove({"_id": ObjectId(trails_id)})
    flash("Your route has been deleted!")
    return redirect(url_for("trails"))


""" Passes user to custom 404 page """
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


""" Passes user to custom 500 page """
@app.errorhandler(500)
def internal_error(e):
    return render_template('pages/500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

