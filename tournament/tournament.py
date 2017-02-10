#!/usr/bin/env python
# Testing VM persistence
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament user=vagrant")

def registerPlayer(FullName):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
    name: the player's full name (need not be unique).
    tid: id of tournament they are entering.
    """
    DB = connect()
    c = DB.cursor()
    player = "INSERT INTO players (FullName,score,matches) VALUES (%s,%s,%s) RETURNING playerid;"
    c.execute(player,(FullName,0,0))
    playerid = c.fetchone()[0]
    DB.commit()
    DB.close()

def countPlayers():
    """Returns number of players currently active in a tournament."""
    DB = connect()
    c = DB.cursor()
    playerid = "SELECT count(playerid) AS num FROM players;"
    c.execute(playerid,)
    players = c.fetchone()[0]
    DB.commit()
    DB.close()
    return players

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()

def reportMatch(winner,loser):
    """Records the outcome of a single match between two players.
    Args:
    winner:  the id number of the player who won
    loser:  the id number of the player who lost
    """
    w_points = 1
    l_points = 0
    DB = connect()
    c = DB.cursor()
    ins = "INSERT INTO matches (winner, loser) VALUES (%s,%s)"
    win = "UPDATE players SET score = score+%s, matches = matches+1 WHERE playerid = %s"
    los = "UPDATE players SET score = score+%s, matches = matches+1 WHERE playerid = %s"
    c.execute(ins, (winner, loser,))
    c.execute(win, (w_points, winner,))
    c.execute(los, (l_points, loser,))
    DB.commit()
    DB.close()

def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    c.execute("UPDATE players SET matches = 0;")
    c.execute("UPDATE players SET score = 0;")
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
    A list of tuples, each of which contains (id, name, wins, matches):
    id: the player's unique id (assigned by the database)
    name: the player's full name (as registered)
    wins: the number of matches the player has won
    matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    players = ("SELECT playerid, FullName, score, matches FROM players ORDER by score desc;")
    c.execute(players,)
    ranks = []
    for row in c.fetchall():
        ranks.append(row)
    DB.commit()
    DB.close()
    return ranks

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
        A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM players ORDER BY score desc;")
    outcome = c.fetchall()
    pairs = []
    i = 0
    while len(outcome) > 0:
        pairs.append((outcome[0][0], outcome[0][1]))
        outcome.pop(0)
        pairs[i] += (outcome[0][0], outcome[0][1])
        outcome.pop(0)
        i += 1
    DB.close()
    return pairs