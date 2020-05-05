from tablegamefuncs import d6, highscore

# Greed dice tally: used by Greed
def greedtally(tally):
	count = {}
	for w in tally[1]: # count duplicates
		count[w] = count.get(w, 0) + 1
	for w in count: # identify triples
		if count[w] > 2:
			tally[3] = w
	if tally[3] > 0: # remove triples
		tally[1].remove(tally[3])
		tally[1].remove(tally[3])
		tally[1].remove(tally[3])
	for w in tally[1]: # sort scoring dice
		if w == 1: # If ones,
			tally[4] += 100 # add 100 to hardscore
			tally[0] -= 1 # remove them from dice that can be rolled.
		elif w == 5: # If fives,
			tally[5] += 50 # add 50 to softscore
			tally[6] += 1 # add 1 to softscoring.
	if tally[3] > 1: # If triples are not ones,
		tally[5] += tally[3] * 100 # add them to softscore
		tally[6] += 3 # and to softscoring.
	elif tally[3] == 1: # If triples is ones,
		tally[4] += 1000 # add 1000 to hardscore
		tally[0] -= 3 # remove them from dice that can be rolled.
	if tally[4] + tally[5] == 0: # If none scoring
		tally[2] = 0 # No unbanked
		tally[0] = 0 # No dice
	if tally[6] == tally[0]: # If all scoring,
		tally[0] = 5 # all dice can now be rolled,
		tally[2] += (tally[4] + tally[5]) # add everything to unbanked
		tally[4], tally[5] = 0, 0 # clear hard and soft
	tally[3] = 0 # Reset triples, or we'll get errors

# Greed strategy: used by Greed
def greedstrategy(tally, strat):
	if tally[0] < 3 and tally[0] > 0: # If less than 3 dice, 
		tally[2] += (tally[4] + tally[5]) # add everything to unbanked
		tally[0] = 0 # stop rolling
	elif tally[0] == 3 and tally[4] + tally[5] > 250: # If 3 dice and 250+
		tally[2] += (tally[4] + tally[5]) # add everything to unbanked
		tally[0] = 0 # stop rolling

# Greed: used by Greed
def greedgame(p, hiscore):
	while hiscore < 10000: # Every turn until end of game:
		for t in p:
			tally = [5, [], 0, 0, 0, 0, 0] # 0: dice number, 1: dice, 2: unbanked score, 3: triple, 4: hardscore, 5: softscore, 6: softscorING, 
			while tally[0] > 0:
				tally[1] = d6(tally[0])
				greedtally(tally)
				greedstrategy(tally, p[t].strat)
			p[t].score += tally[2]
			hiscore = highscore(p)
			if hiscore > 9950:
				break
	p[t].wins += 1