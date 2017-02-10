-- Table definitions for the tournament project.
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\connect tournament;

CREATE TABLE players (
  playerid SERIAL PRIMARY KEY,
  FullName TEXT,
  score INTEGER,
  matches INTEGER);

CREATE TABLE matches (
  matchid SERIAL PRIMARY KEY,
  winner INT REFERENCES players(playerid),
  loser INT REFERENCES players(playerid),
  draw BOOLEAN);