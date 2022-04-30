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
     
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    @staticmethod
    def load_players(self):
        pass
    def __init__(self, name, password,update=True):
        self.set_password(password)
        self.values = [name,self.password_hash,0]
        
    def new_game(self, score, update=True):
        pass
    def update_players(self):
        self.set_password(self.values[1])
        self.values[1] = self.password_hash
        print(self.values)
        dbmanage.manageplayer(conn,self.values )
    def __str__(self):
        pass

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
test = Player("kloe","!afefR34")
test.update_players()
print(test.password_hash)
print(check_password_hash (dbmanage.fetchplayer(conn,test.values)[0][1],"!afefR34"))




