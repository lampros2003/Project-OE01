from enum import Flag
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
#always to remain false unless user logged in or first time signed in 
#do not alter outside of login and signup functions

global authorizedentry 
authorizedentry= False


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
        # password for player object
        self.password_hash = generate_password_hash(password)
        #print(check_password_hash(self.password_hash,password))
     
    
    @staticmethod
    def load_players(self):
        pass
    def __init__(self, name, password,update=True):
        self.name = name
        self.password = password
        self.set_password(password)
        self.values = [name,self.password_hash,0]

    def check_password(self):
        #checks password on db
        passondb = dbmanage.fetchplayer(conn,self.values)[0][1]
        authorizedentry =  check_password_hash(passondb,self.password)
        return authorizedentry
        
    def new_game(self, score, update=True):
        pass
    #updates the database with current inputed player if conditions met
    def update_players(self):
        #hashes the password for safe store on db
        if dbmanage.fetchplayer(conn,self.values):
            #user already exists block signup
            return False
        self.values[1] = self.password_hash
        dbmanage.insertplayer(conn,self.values )
        authorizedentry = True
        return authorizedentry
    ##only to hapen after authorization
    def update_player_stats(self):
    
        dbmanage.editplayer(conn,self.values)


    def __str__(self):
        pass
    def receiveperformance(self,grade):
        self.values[2] = grade

def makeplayer(username,password):
    #makes player object 
    #not currently usefull
    return Player(username,password)

def load_quiz():
    pass
    ## load players
    #Player.load_players()

def play_quiz():
    pass
if __name__ == "__main__":
    pass
    #load_quiz()
    #play_quiz()



#####################TEST#########TEST######################
testplay = makeplayer("carmalo","!@balana243")
print(testplay.update_players())
authorizedentry= testplay.check_password()
print(authorizedentry)
testplay.receiveperformance(16)
if authorizedentry:
    testplay.update_player_stats()

print(dbmanage.fetchplayer(conn,testplay.values))





