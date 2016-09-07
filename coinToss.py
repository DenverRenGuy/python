from __future__ import division

def tossCoin():
    import random
    return round(random.random())

#Test Function  Zero for Heads, One for tails

heads = tails = prob = 0
coin = ""


for count in range(1,5001):
    toss = tossCoin()
    if toss % 2:
        heads += 1
        coin = "Heads"
        prob = heads/(heads+tails)
    else:
        tails += 1
        coin = "Tails"
        prob = tails/(heads+tails)

    print "Attempt #%d, throwing the coin! ... It's %s.  You have flipped %d Heads & %d Tails.  Your probability for %s is %f%%" % (count, coin, heads, tails, coin, prob)
