from flask import Flask
app = Flask(__name__)

@app.route("/login")
def login():

@app.route("/start")
def start():

@app.route("/end")
def end():

@app.route('/q/<id>')
def question(id):
if __name__ == "__main__":
    app.run(debug=True)