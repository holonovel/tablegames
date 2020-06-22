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

# Declare Scores: used by Greed
def declscore(p, t):
	scores = []
	for w in p:
		if w != t:
			scores.append(p[w].score)
	return scores

### Greed Functions ###

# Stop rolling: used by Greed
def greedkeep(tally):
	tally.unbanked += (tally.hardscore + tally.softscore) # add everything to unbanked
	tally.dnum = 0 # stop rolling

# Greed dice tally: used by Greed
def greedtally(tally):
	count = {}
	for w in tally.dice: # count duplicates
		count[w] = count.get(w, 0) + 1
	for w in count: # identify triples
		if count[w] > 2:
			tally.triple = w
	if tally.triple > 0: # remove triples
		tally.dice.remove(tally.triple)
		tally.dice.remove(tally.triple)
		tally.dice.remove(tally.triple)
	for w in tally.dice: # sort scoring dice
		if w == 1: # If ones,
			tally.hardscore += 100 # add 100 to hardscore
			tally.dnum -= 1 # remove them from dice that can be rolled.
		elif w == 5: # If fives,
			tally.softscore += 50 # add 50 to softscore
			tally.softscoring += 1 # add 1 to softscoring.
	if tally.triple > 1: # If triples are not ones,
		tally.softscore += tally.triple * 100 # add them to softscore
		tally.softscoring += 3 # and to softscoring.
	elif tally.triple == 1: # If triples is ones,
		tally.hardscore += 1000 # add 1000 to hardscore
		tally.dnum -= 3 # remove them from dice that can be rolled.
	if tally.hardscore + tally.softscore == 0: # If none scoring
		tally.unbanked = 0 # No unbanked
		tally.dnum = 0 # No dice
	if tally.softscoring == tally.dnum and tally.dnum != 0: # If all scoring,
		tally.dnum = 5 # all dice can now be rolled,
		tally.unbanked += (tally.hardscore + tally.softscore) # add everything to unbanked
		tally.hardscore, tally.softscore = 0, 0 # clear hard and soft

def greedtreset(tally):
	tally.softscore = 0
	tally.triple = 0
	tally.softscoring = 0
	tally.unbanked += tally.hardscore
	tally.hardscore = 0

# Greed strategy: used by Greed
def greedstrategy(tally, t, p):
	if p[t].strat == 1: # default AI
		if tally.dnum < 3 and tally.dnum > 0: # If less than 3 dice, 
			greedkeep(tally)
		elif tally.dnum == 3 and tally.hardscore + tally.softscore > 250: # If 3 dice and 250+
			greedkeep(tally)
	else: # human player or neural net
		if tally.dnum == 0: # If human player busts
			if p[t].strat == 0:
				print("Bust.") # Report. Situation resolves automatically
		else:
			x = ""
			options = ["0", "1"]
			print(tally.softscore, tally.hardscore, tally.dnum) ####
			while x not in options:
				if p[t].strat == 0: # player has no softscoring
					print("0: Keep,", end=" ")
					print("1: Roll max,", end=" ")
				if tally.softscore > 0: # player has simple softscoring
					if "2" not in options:
						options.append("2")
					if p[t].strat == 0:
						print("2: Roll only non-scoring,", end=" ")
				if tally.softscore == 100: # player has two fives
					if "3" not in options:
						options.append("3")
					if p[t].strat == 0:
						print("3: Keep only one five,", end=" ")
				if tally.softscore in (250, 350, 450, 550): # player has triple and five
					if "3" not in options:
						options.append("3")
					if p[t].strat == 0:
						print("3: Keep only one five,", end=" ")
					if "4" not in options:
						options.append("4")
					if p[t].strat == 0:
						print("4: Keep only triple,", end=" ")
				x = input("Your choice? ")
				if x not in options and p[t].strat == 0:
					print("Invalid input.")
			if x == "0": # Stop rolling. No need to check if x == 1, because that's default behavior.
				greedkeep(tally)
			elif x == "2": # Keeping all scoring, rolling the rest
				tally.unbanked += tally.softscore
				tally.dnum -= tally.softscoring
			elif x == "3":
				tally.unbanked += 50
				tally.dnum -= 1
			elif x == "4":
				tally.unbanked += (tally.softscore - 50)
				tally.dnum -= 3