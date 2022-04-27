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
        ...
    def __init__(self, name, update=True):
        ...
    def new_game(self, score, update=True):
        ...
    def update_players(self):

    def __str__(self):


def load_quiz():
    ...
    ## load players
    Player.load_players()

def play_quiz():
    ...
if __name__ == "__main__":
    load_quiz()
    play_quiz()