import re
import os
import random
import datetime

total_questions = 5
class Quiz:
    allQuiz = {}
    def __init__(self, id, question, replies, correct):
        ...
    def calculate_score(self, reply):
        ...
    def __str__(self):
        ...

class Player:
    players = {}
    @staticmethod
    def load_players():
        pass
    def __init__(self, name, update=True):
        pass
    def new_game(self, score, update=True):
        pass
    def update_players(self):
        pass
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