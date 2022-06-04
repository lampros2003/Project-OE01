from pprint import pprint
from traceback import print_tb
from flask import Flask, flash
from pythonquiz import *
import dbmanage
from flask import request, session
from flask import render_template, redirect, url_for
import secrets
#make secret key
secret = secrets.token_urlsafe(32)

app = Flask(__name__)
#use secret key
app.config['SECRET_KEY'] = secret
@app.route ("/")
def root():
    session['loggedin'] = False
    return redirect(url_for("login"))
@app.route("/login", methods=["GET", "POST"])
def login():
    #loginpage to go here
    session['loggedin'] = False

    reply = request.query_string.decode()

    if not reply :
        print("session")
        return render_template("index.html")
    elif reply:
        #check if user exists
        print("POST")
        pprint(reply)
        username = reply.split("&")[0].split("=")[1]
        password = reply.split("&")[1].split("=")[1]
        if Player.check_password(username, password):
            print("login successful")
            session["username"] = username
            session["password"] = password
            session["score"] = 0
            session["tries"] = 0
            session["loggedin"] = True
            return redirect(url_for("start"))
        else:
            flash("Login unsuccessful")
            return render_template("index.html", message="Invalid username or password")

@app.route("/start")
def start():
    if session["loggedin"]:
        return render_template("start.html")
    else:
        return redirect(url_for("login"))

@app.route("/end")
def end():

    pass

@app.route('/q/<id>')
def question(id):
    return render_template('main_page.html', user_name=session["username"], replies=0, answer=score)
    
    pass
if __name__ == "__main__":
    app.run(debug=True)
