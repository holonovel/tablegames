from tablegamefuncs import d6, highscore, greedtally, greedstrategy, declscore, greedtreset

class GTally:
	def __init__(self):
		self.dnum = 5
		self.dice = []
		self.unbanked = 0
		self.triple = 0
		self.hardscore = 0
		self.softscore = 0
		self.softscoring = 0

# Greed: used by Greed
def greedgame(p, hiscore):
	while hiscore < 10000: # Every turn until end of game:
		for t in p:
			tally = GTally()
			while tally.dnum > 0:
				tally.dice = d6(tally.dnum)
				if p[t].strat == 0:
					print("Opponent score(s):", declscore(p, t), "; Your score:", p[t].score, "; Unbanked:", tally.unbanked, "; You rolled ", tally.dice)
				greedtally(tally)
				greedstrategy(tally, t, p)
				greedtreset(tally)
			p[t].score += tally.unbanked
			hiscore = highscore(p)
			if hiscore > 9950:
				break
	p[t].wins += 1