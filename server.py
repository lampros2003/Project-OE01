
from flask import Flask, flash
from pythonquiz import Quiz, Player
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
conn = dbmanage.conn
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
    if "counter" not in session:
        session["counter"] = 0
    if not reply :
        return render_template("index.html")
    else:
        #check if user exists
        
        username = reply.split("&")[0].split("=")[1]
        password = reply.split("&")[1].split("=")[1]
        if Player.check_password(username, password):
            print("ooo")
            session["username"] = username
            session["password"] = password
            session["score"] = 0
            session["tries"] = 0
            session["logged_in"] = True
            
            return redirect(url_for("start"))
        else:
            print(username,password)
            flash("Incorrect username or password")
            return render_template("index.html")
@app.route("/register")
def register():
    reply = request.query_string.decode()
    if not reply :
        return render_template("register.html")
    else:
        #check if user exists
        
        username = reply.split("&")[0].split("=")[1]
        password = reply.split("&")[1].split("=")[1]
        if  Player.update_players(conn, [username,password]):
            print(username,password)
            flash("Username already exists")
            session["username"] = username
            session["password"] = password
            session["score"] = 0
            session["tries"] = 0
            session["logged_in"] = True
            return redirect(url_for("start"))
           
        else:
            flash("User already exists")
           
            return render_template("register.html", message="Username already exists")


    return render_template("register.html")
def loggedstart():
    name = session["username"]
    print(name,0)
    history=dbmanage.fetchplayer(conn,[name])[0]
    print(history,"wwww")
    try1=history[2]
    try2=history[3]
    try3=history[4]
    try4=history[5]
    questions = Quiz.draw_questions()
    print(questions)
    new_question = questions.pop()
    session["questions"] = questions
    session["score"] = 0
    session["count"] = 0
    if request.query_string:
        
        return redirect(url_for("question", id = new_question))
    else:
        return render_template("start.html",name=name,try1=try1,try2=try2,try3=try3,try4=try4)
            
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
    print("ROUTE /quiz", id)
    # ανάκτησε από το session την κατάσταση...
    name = session.get("username", None)
    score = session.get("score", 0)
    count = session.get("tries",0)
    questions = session.get("questions", [])
    print(":::::::::::::::::questions",questions)
    Player.update_player_stats(name,score+1)
    print(dbmanage.fetchplayer(conn,[name])[0])

    if id == "end":
        session["username"] = name
        Player.update_player_stats(name, score)
        return redirect(url_for("end")) ##### ( 5 ) #####

    
    
    q = Quiz.show_question(id)
    if request.query_string: # ο χρήστης απάντησε
        reply = request.args.get("answer")
        new_score = Quiz.calculate_score(id,reply)
        score += new_score
        name = session.get("username", None)
        score = session.get("score", 0)
        count = session.get("tries",0)
        questions = session.get("questions", [])
        if new_score == 1: feedback = "Σωστή απάντηση"
        else: feedback = "Προσοχή! Η σωστή απάντηση είναι η {}".format(q["correct"])
        
        if questions: 
            next_question = questions.pop()
        else: next_question = "end"
        session["user_name"] = name
        session["score"] = score
        session["questions"] = questions
        ## να δώσουμε ανάδραση για την απάντηση και σκορ
        return render_template('main_page.html', question = q["question"], \
            id = id, user_name=name, replies = q["answer"],
            feedback = feedback, next_question = next_question, button="Επόμενη",
            disabled = "disabled") ####### ( 4 ) ########

    else: # πρέπει να στείλουμε στον χρήστη την ερώτηση
        session["user_name"] = name
        session["score"] = score
        session["questions"] = questions
        session["count"] = count + 1
        print(q["answer"])
        return render_template('main_page.html', question = q["question"], \
            id = id, user_name=name, replies = q["answer"], button="Υποβολή")
    return loginwrap(loggedquestion(id))
    

    
if __name__ == "__main__":
    app.run(debug=True)
