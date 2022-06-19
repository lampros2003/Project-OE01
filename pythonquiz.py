import random
import dbmanage
from werkzeug.security import generate_password_hash, check_password_hash
total_questions = 5
conn = dbmanage.connecttodb()
#always to remain false unless user logged in or first time signed in 
#do not alter outside of login and signup functions

global authorizedentry 
authorizedentry= False


class Quiz:
    allQuiz = []
    def __init__(self, id, question, player, answer, tries,score = 0 ):
        self.qid = id
        self.question = question
        self.player = player
        self.answer = answer
        self.tries = tries
        self.score = score
    def calculate_score(id, reply):
        #score calculation
        #exact formula for score calculation to be discussed
        if reply == dbmanage.takequestion(conn,id)[0][3]:
            
            return 1
        else:
            return 0
    def draw_questions():
        #draw questions from database
        #returns a list of questions
        num = dbmanage.numqs(conn)
        questions = []
        for i in range(total_questions):
            qid = random.randint(1,num)
            questions += [qid]

        return questions

    def show_question(id):
        #returns the question
        q = dbmanage.takequestion(conn,id)[0]
        qout = {"id":q[0], "question":q[1],"answer":[i for i in q[2].split("$")],"correct":q[3]}
        return qout


    def __str__(self):
        pass




class Player:
    players = {}
    
    
    def set_password(password):
        # password for player object
        password_hash = generate_password_hash(password)
        return password_hash
        #print(check_password_hash(self.password_hash,password))


    @staticmethod
    def load_players(self):
        pass
    def __init__(self, name, password,update=True):
        self.name = name
        self.password = password
        self.set_password(password)
        self.values = [name,self.password_hash,0]

    def check_password(name, password):
        #checks password on db
        print(name,password)
        print(dbmanage.fetchplayer(conn, [name,password]))
        #no username
        if not dbmanage.fetchplayer(conn, [name,password]):
            return False
        #username exists check password
        passondb = dbmanage.fetchplayer(conn,[name,password])[0][1]

        
        return check_password_hash(passondb,password)
        
    def new_game(self, score, update=True):
        pass
    #updates the database with current inputed player if conditions met
    def update_players(self,values):
        #hashes the password for safe store on db
        if dbmanage.fetchplayer(conn,values):
            #user already exists block signup
            return False
        values[1] = Player.set_password(values[1])
        dbmanage.insertplayer(conn,values )
        return True
    ##only to happen after authorization
    def update_player_stats(name, score):
        dbmanage.editplayer(conn, [name,score])
    def __str__(self):
        pass
    def receiveperformance(self,grade):
        self.values[2] = grade

def makeplayer(username,password):
    #makes player object 
    #not currently usefull
    return Player(username,password)
#quiz contains question id,questin text and player playing
def load_quiz(player):
    global quiz 
    q = dbmanage.takequestion(conn)
    quiz = Quiz(q[0],q[1],player,q[2],0)
    quiz.allQuiz.append(q[0])
    return quiz
    ## load players
    #Player.load_players()

def play_quiz(quiz,response):
    #plays quiz
    #checks if response is correct
    #if correct, adds to score
    #adds to tries
    #implement using while loop?
    if quiz.tries < total_questions:
        quiz.tries = quiz.tries + 1
        quiz.calculate_score(response)
        q = dbmanage.takequestion(conn)
        quiz.id = q[0]
        quiz.question = q[1]
        quiz.answer = q[2]
        return False#quiz not over
    else:
        quiz.calculate_score(response)
        quiz.player.values[2] = quiz.score
        quiz.player.update_player_stats()
        return True#quiz over

""" def save_game(name, score):
    return
    player = Player.players[name]
    if (name in Player.players) 
    else Player(name, update=False)
    player.new_game( 100*score/total_questions ) """

def question_score(id, reply):
    q = Quiz.allQuiz[id]
    return q.calculate_score(reply)


        
if __name__ == "__main__":
    q= Quiz.draw_questions()
    print(q)
    #load_quiz()
    #play_quiz()



#####################TEST#########TEST######################
""" testplay = makeplayer("test","test123")
print(testplay.update_players())
authorizedentry= Player.check_password("test","test123")
print(authorizedentry)
testplay.receiveperformance(16)
if authorizedentry:
    testplay.update_player_stats()

print(dbmanage.fetchplayer(conn,testplay.values))  """







