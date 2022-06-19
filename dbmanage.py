import psycopg2
import dbcreds as creds
def connecttodb():
    conn_string = "host="+ creds.PGHOST +" port="+ "5432" +" dbname="+ creds.PGDATABASE +" user=" + creds.PGUSER \
    +" password="+ creds.PGPASSWORD
    conn=psycopg2.connect(conn_string)
    return conn
conn = connecttodb()
def create_tables(conn):
    cursor =conn.cursor()
    command = """
        CREATE TABLE players (
            player_name VARCHAR(255) NOT NULL,
            player_pass VARCHAR(255) NOT NULL,
            player_tries1 INT,
            player_tries2 INT,
            player_tries3 INT,
            player_tries4 INT
        )
        
        """
    command2 = """
            CREATE TABLE questions (
            question_id  INT,
            question_content VARCHAR(1000) NOT NULL,
            question_answers VARCHAR(1000) NOT NULL,
            answer INT NOT NULL
        )"""
    cursor.execute(command)
    conn.commit()
    
    cursor.execute(command2)
    conn.commit()
    

    
def fetchplayer(conn,pvs):
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM players WHERE player_name = '{}'".format(pvs[0]))
    vals = cursor.fetchall()
    return vals

playervars = ("Jane","12345678",19)
def insertplayer(conn,pvs):
    cursor =conn.cursor()
    """ insert a  player into the players table """
    sql = """INSERT INTO players (player_name,player_pass,player_tries1,player_tries2,player_tries3,player_tries4) 
    VALUES('{}','{}',{},{},{},{}) ;""".format(pvs[0],pvs[1],0,0,0,0)
    cursor.execute(sql)
    conn.commit()
def editplayer(conn,pvs):
    cursor =conn.cursor()
    updatevals = fetchplayer(conn,pvs)
    print(updatevals)
    command = """UPDATE players
    SET player_tries4 = {player_tries3},player_tries3={player_tries2},player_tries2={player_tries1},player_tries1={}
    WHERE player_name = '{}';
    """.format(pvs[1],pvs[0],player_tries3 = updatevals[0][4],player_tries2 = updatevals[0][3],player_tries1 = updatevals[0][2])
    cursor.execute(command)
    conn.commit()

def manageplayer(conn,pvs):
    
    vals = fetchplayer(conn,pvs)
    if vals:
       editplayer(conn,pvs)
       conn.commit()
    else :
        insertplayer(conn,pvs)
        conn.commit()

#explicit type declaration TO DO ---- DONE
#add on rest of functions for ease of use and deubbuging TO DO 
##function returns tuple including question id and question content
def numqs(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(question_id) from questions;")
    numofquestions = cursor.fetchone()[0]
    return numofquestions-2
def takequestion(conn,id):#:psycopg2.connection):
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM questions WHERE question_id = {}".format(id))
    question = cursor.fetchall()
    return question 
def addqtodbfromtxt(conn):
    cursor = conn.cursor()
    id = 0
    content ="""Before you start the quiz:
    \n1)You will have to select one of the possible answers.
    \n2)There is always a correct answer.
    \n3)There is no penalty if your answer is wrong.
    \n4)You can see how you did in the end screen.
    \n5)Begin the test whenever you feel ready.
    """
    answer = 1
    answers =['Begin']
    with open("questions.txt","r",encoding="utf-8")  as file:
        for line in file:
            if not line.strip():
                continue
            if line.startswith("Q"):
                id =line.strip()
                id = id.translate({ord(i): None for i in 'Q.'})
                print(answers)
                answtxt = "$".join([(i.replace("'","''")).replace("***","") for i in answers])
                sql = """INSERT INTO questions (question_id,question_content,question_answers,answer) 
                    VALUES({},'{}','{}',{}) ;""".format(int(id)-1,content.replace("'","''"),answtxt,answer)
                cursor.execute(sql)
                conn.commit()
                content = ''
                answer = 0
                answers = []
            else:
                if line.strip().endswith("***"):
                    answer = int(line.split()[0].strip("."))
                    line = line.strip().rstrip("***")
                    answers.append(line[2:-1])
                elif line[0].isdigit() and line[1]==".":
                    answers.append(line[2:-1].lstrip())
                   
                
                else:
                    content += line


def addrule(conn):
    cursor = conn.cursor()
    rules ="""Before you start the quiz:
    \n1)You will have to select one of the possible answers.
    \n2)There is always a correct answer.
    \n3)There is no penalty if your answer is wrong.
    \n4)You can see how you did in the end screen.
    \n5)Begin the test whenever you feel ready.
    """
    sql = """INSERT INTO questions (question_id,question_content,question_answers,answer) 
                    VALUES({},'{}','{}',{}) ;""".format(0,rules,"Begin",1)
   
    cursor.execute(sql)
    conn.commit()

if __name__ == "__main__":
    create_tables(conn)
    addqtodbfromtxt(conn)
    
