# To run this, run in this format:
# python3 game.py 1 2 1000
#                 | | |
#                 | | Number of games
#                 | Number of players
#                 Which game is to be played. Greed is game 1.

import argparse
from random import randrange

parser = argparse.ArgumentParser(description='Play games.')
parser.add_argument('game_settings', type=int, nargs=3)
args = parser.parse_args()
game, pnum, gamesplayed = args.game_settings # We're taking two numbers given as arguments and making them the number of players, and the number of games to be played

p = {} # In every game, p stands for Player, t stands for Turn

### Players ###

# APlayer: used by Greed, Pig, Firefly
class APlayer:
	def __init__(self):
		self.score = 0
		self.wins = 0
		self.strat = 1 # 0 is player, 1 is default AI, 2 is neural net

### Game Setups ###

# A Setup: used by Greed, Pig, Firefly
def asetup(pnum):
	for w in range(1,(pnum + 1)): # Create pnum players
		p[w] = APlayer()
	hiscore = 0 # Score of person who's in the lead
	return p, hiscore

### Game List ###

# Play Greed
def playgreed(p, stuff, gamesplayed):
	if gamesplayed == 1: # If we're only playing one game
		p[randrange(1, (len(p)+1))].strat = 0 # Set a random player to human control
	from greed import greedgame
	greedgame(p, stuff)

def playpig(p, stuff, gamesplayed):
	from pig import piggame
	piggame(p, stuff)

### Game Resets ###

# A Reset: used by Greed, Pig, Firefly
def areset(p, stuff):
	for w in p: # Set all player scores to zero.
		p[w].score = 0

# B Reset: used for testing
def breset(p, stuff):
	p[1].score = 9650
	p[2].score = 9950

### Game Reports ###

# A Report: used by Greed, Pig, Firefly
def areport(p):
	for w in p: print('Player', w, ':', p[w].wins)

### Game Dicts ###

# 0: Testing, 1: Greed, 2: Pig, 3: 

# Setup list
setuplist = {1:asetup, 2:asetup, 0:asetup}

# Play list
play = {1:playgreed, 2:playpig, 0:playgreed}

# Reset list
resetlist = {1:areset, 2:areset, 0:breset}

# Report list
reportlist = {1:areport, 2:areport, 0:areport}

### Game picker ###
p, stuff = setuplist[game](pnum)
for _ in range(gamesplayed): # Play this many games
	resetlist[game](p, stuff)

	play[game](p, stuff, gamesplayed)

reportlist[game](p)

