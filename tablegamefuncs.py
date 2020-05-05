from random import randrange
import pdb # dwd
# pdb.set_trace() # dwd

### Shared Functions ###

# B-Setup: used by Cure
def bsetup(pnum, gamesplayed):
	for w in range(1,(pnum + 1)): # Create pnum players
		p[w] = BPlayer()
	diseases = [0, 0, 0, 0]

# d6: used by Greed, Firefly
def d6(dicenumber):
	return [randrange(1,7) for _ in range(dicenumber)]

# dSpecial: used by Cure, Darwin Carlo
def ds(dicenumber, die):
	return [die[randrange(0,6)] for _ in range(dicenumber)]

# Deal: used by UNUSED
def deal(dealstyle, p):
	if dealstyle == 0: # 0 is 52 card deck dealt to 4 players
		deck = [52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
		for w in p:
			while len(p[w].cards) < 13:
				z = randrange(0, len(deck))
				p[w].cards.append(deck.pop(z))
	return players

# High Score: used by Greed
def highscore(p):
	scores = []
	for w in p:
		scores.append(p[w].score)
	scores.sort() # Sort scores low to high
	return scores.pop(len(p) - 1) # Check highest score

#https://en.wikipedia.org/wiki/List_of_dice_games

#Press your luck
#	Dungeon Roll
#	Dragon Slayer
#	Greed
#	Firefly
#	Farkle
#	Cosmic Wimpout
#	Cinq-O
#	Can't Stop
#	Ten Thousand
#	Backgammon
#	Pickomino
#	Fill or Bust
#	Hoppladi Hopplada
#	Excape
#	Pig
#	Reiner Knizia's Decathlon
#	Sushizock im Gockelwok
#	Roll Through the Ages: The Bronze Age
#	Second Story
#	Cookie Fu
#	Pass the Pigs
#	Train Wreck
#	Toss Up
#	Mountain Climber
#	Cloud 9
#	Pachisi
#	Risk Express
#	Aggravation
#	Joker Marbles
#	Sorry!
#	DOG
#	CirKle Duo228
#	King of Tokyo
#Dice placement
#	Steampunk Rally
#Dice Drafting
#	Roll Player
#Roll and Write
#	Yahtzee
#	Twenty One
#	Dice Stars
#	Noch Mal!
#	Qwixx
#	Rolling America
#	Ganz Schon Clever
#	Qwinto
#	Let's Make a Bus Route
#	Kokoro / Avenue -- Avenue has dice
#	Saint Malo

#Noctiluca
#Seasons
#Roll for the Galaxy
#Dice Masters
#Yahtzee
#Bilge Dice
#Dice Poker
#Craps
#Shut the Box
#Balut
#Beetle
#Poker Dice
#Bunco
#Cee-lo
#Dragon Dice
#Diceland
#Battle Dice
#Sic bo
#Liar's dice
#Kismet
#Pugasaing

#Button Men