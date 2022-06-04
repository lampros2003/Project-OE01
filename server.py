from flask import Flask
import pythonquiz
import dbmanage
from flask import request, session
from flask import render_template, redirect, url_for
app = Flask(__name__)

@app.route ("/")
def root():
    return redirect(url_for("login"))
@app.route("/login", methods=["GET", "POST"])
def login():
    #loginpage to go here
    if request.method == "GET":
        return render_template("index.html")
    else:
        #check if user exists
        username = request.form.get("username")
        password = request.form.get("password")
        if dbmanage.check_user(username, password):
            session["username"] = username
            return redirect(url_for("start"))
        else:
            return render_template("login.html", message="Invalid username or password")

@app.route("/start")
def start():
    
    return render_template("start.html")

@app.route("/end")
def end():

    pass

@app.route('/q/<id>')
def question(id):
    return render_template('main_page.html', user_name=session["username"], replies=0, answer=score)
    
    pass
if __name__ == "__main__":
    app.run(debug=True)
