def tossCoin():
    import random
    return round(random.random())

#Test Function  Zero for Heads, One for tails

heads = 0
tails = 0

for count in range(1,5000):
    toss = tossCoin()
    if toss % 2:
        heads += 1
    else:
        tails += 1
    print "Attempt #%d"
