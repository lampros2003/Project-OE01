import re
import os
import random
import datetime
import dbmanage
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
total_questions = 5
conn = dbmanage.connecttodb()
class Quiz:
    allQuiz = {}
    def __init__(self, id, question, replies, correct):
        pass
    def calculate_score(self, reply):
        pass
    def __str__(self):
        pass

class Player:
    players = {}
    
    
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        print(check_password_hash(self.password_hash,password))
     
    
    @staticmethod
    def load_players(self):
        pass
    def __init__(self, name, password,update=True):
        self.name = name
        self.password = password
        self.set_password(password)
        self.values = [name,self.password_hash,0]

    def check_password(self):
        passondb = dbmanage.fetchplayer(conn,self.values)[0][1]
        print(passondb)
        print(self.password)
        return check_password_hash(passondb,self.password)
        
    def new_game(self, score, update=True):
        pass
    def update_players(self):
        #self.set_password(self.values[1])
        self.values[1] = self.password_hash
        print(self.values)
        dbmanage.manageplayer(conn,self.values )
    def __str__(self):
        pass
def getplayer(username,password):
    
    return Player(username,password)

def load_quiz():
    pass
    ## load players
    ##Player.load_players()

def play_quiz():
    pass
if __name__ == "__main__":
    pass
    #load_quiz()
    #play_quiz()
testplay = getplayer("palooza","1234")
testplay.update_players()

print(testplay.check_password())





