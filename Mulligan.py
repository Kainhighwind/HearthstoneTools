''' This is a script that calculates and displays probabilities of hitting certain outs based on available outs and cards drawn.
This script relys on using the hypergeometric distribution method found in numpy
'''
from scipy.stats import hypergeom
import numpy as np
import matplotlib.pyplot as plt

# data input commands
Deck_Size = int(input("Enter the size of remaining deck: "))
Number_of_Draws = int(input("Enter the total number of draws: "))
Number_of_Outs = int(input("Enter the number of outs remaining in the deck: "))

# Calculated the probability mass function
RV = hypergeom(Deck_Size, Number_of_Outs, Number_of_Draws)
Outs = np.arange(0, Number_of_Outs +1)
PMF = RV.pmf(Outs)

# plotting
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Outs, PMF, 'bo')
ax.vlines(Outs, 0, PMF, lw=2)
ax.set_xlabel('# of successes')
ax.set_ylabel('Probability')
plt.show(block=False)

# Returning the "at least" percentages
Odds = np.empty(Number_of_Outs+1, dtype=float)
for out in range(1, len(Outs)):
    Odds[out] = RV.sf(out-1)
    print("The odds of getting at least {0:d} outs is {1:3f}".format(out, Odds[out]))
plt.show()
