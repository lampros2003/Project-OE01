from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "morning bro!"

if __name__ == "__main__":
        app.run(debug=True)


for i in range(10):
    print("potato")