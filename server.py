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
#SOS
#SOS LOGIN WRAPPER ONLY USE FUNCTIONS THROUGH THIS 
#DO NOT USE AN UNWRAPPED FUNCTION ON FINAL BUILD IT WILL BE UNSAFE
#THANKS
#SOS
def loginwrap(func):
    
    #wrapper function
    #defines wrapper to be returned
    #wrapper will check if user is logged in
    #if not, redirect to login page
    #if so, return function to be called

    
    def wrapper(*args, **kwargs):
        if "logged_in" not in session or not session["logged_in"]:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    #return wrapper as function not as a value / object
    return wrapper
app = Flask(__name__)
#use secret key
app.config['SECRET_KEY'] = secret
@app.route ("/")
def root():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    #loginpage to go here
    reply = request.query_string.decode()

    if not reply :
        return render_template("index.html")
    elif reply:
        #check if user exists
        
        username = reply.split("&")[0].split("=")[1]
        password = reply.split("&")[1].split("=")[1]
        if Player.check_password(username, password):
            session["username"] = username
            session["password"] = password
            session["score"] = 0
            session["tries"] = 0
            session["logged_in"] = True
            
            return redirect(url_for("start"))
        else:
            flash("Login unsuccessful")
            return render_template("index.html", message="Invalid username or password")

def loggedstart():
    if request.query_string :
        return url_for("question", id=1)
    return render_template("start.html")
@app.route("/start")
def start():

    return loginwrap(loggedstart)()
   

@app.route("/end")
def end():

    pass

def loggedquestion(*args, **kwargs):
    return render_template("question.html",id=args[0])
@app.route('/q/<id>')
def question(id):
    return loginwrap(loggedquestion(id))
    

    
if __name__ == "__main__":
    app.run(debug=True)
