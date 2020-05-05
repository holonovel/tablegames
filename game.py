# To run this, run in this format:
# python3 game.py 1 2 1000
#                 | | |
#                 | | Number of games
#                 | Number of players
#                 Which game is to be played. Greed is game 1.

import argparse

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
		self.strat = 0

### Game Setups ###

# A Setup: used by Greed, Pig, Firefly
def asetup(pnum):
	for w in range(1,(pnum + 1)): # Create pnum players
		p[w] = APlayer()
	hiscore = 0 # Score of person who's in the lead
	return p, hiscore

### Game List ###

# Play Greed
def playgreed(p, stuff):
	from greed import greedgame
	greedgame(p, stuff)

def playpig(p, stuff):
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

	play[game](p, stuff)

reportlist[game](p)

# Greed strategy discussion:
# P[i][j][k] is the player's probability of winning if the player's score is i, the opponent's score is j, and the player's unbanked is k

# i = 9700 to 9950, j = 9950, k = 0
# P[i][j][k] = ~96%

# i = 9650, j = 9950, k = 0
# P[i][j][k] = ~74%

# i = 9600, j = 9950, k = 0
# P[i][j][k] = ~64%

# i = 8000, j = 9950, k = 0
# P[i][j][k] = ~3%

# i = 7600, j = 9950, k = 0
# P[i][j][k] = ~1%

# i = 0 to 7550, j = 9950, k = 0
# P[i][j][k] = >1%

# I think to figure this out, we need to MC a one-player varient to figure out how likely a player is to win on their next turn.