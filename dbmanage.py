from multiprocessing.dummy import current_process
from click import command
import psycopg2
import sys, os
import numpy as np
import pandas as pd
import dbcreds as creds
import pandas.io.sql as psql

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
    cursor.execute(command)
    

    
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
    VALUES('{}','{}',{},{},{},{}) ;""".format(pvs[0],pvs[1],pvs[2],0,0,0)
    cursor.execute(sql)
def editplayer(conn,pvs):
    cursor =conn.cursor()
    updatevals = fetchplayer(conn,pvs)
    command = """UPDATE players
    SET player_tries4 = {player_tries3},player_tries3={player_tries2},player_tries2={player_tries1},player_tries1={}
    WHERE player_name = '{}';
    """.format(pvs[2],pvs[0],player_tries3 = updatevals[0][4],player_tries2 = updatevals[0][3],player_tries1 = updatevals[0][2])
    cursor.execute(command)
def manageplayer(conn,pvs):
    
    vals = fetchplayer(conn,pvs)
    if vals:
       editplayer(conn,pvs)
       conn.commit()
    else :
        insertplayer(conn,pvs)
        conn.commit()
