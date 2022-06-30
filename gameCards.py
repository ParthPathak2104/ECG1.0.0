# File containing all game cards
from heapq import merge
from itertools import repeat
import random

# Resource Cards

time = []
time.extend(repeat(1,27))
time.extend(repeat(2,22))
time.extend(repeat(4,11))

money = []
money.extend(repeat(500,25))
money.extend(repeat(1000,20))
money.extend(repeat(1500,15))

resourcePile = time +  money


# Actionable Cards 

# General Skills (research and marketing):  7hr*3  +  9hr* 6  +  13hr*4
generalHourCost = [7, 9, 13]            # Hour cost of general skill cards
generalCardQuantity = [3, 6, 4]         # Quantities of general skill cards

researchActionCards = []
researchActionCards.extend(repeat(("Research", generalHourCost[0]), generalCardQuantity[0]))
researchActionCards.extend(repeat(("Research", generalHourCost[1]), generalCardQuantity[1]))
researchActionCards.extend(repeat(("Research", generalHourCost[2]), generalCardQuantity[2]))

marketingActionCards = []
marketingActionCards.extend(repeat(("Marketing", generalHourCost[0]), generalCardQuantity[0]))
marketingActionCards.extend(repeat(("Marketing", generalHourCost[1]), generalCardQuantity[1]))
marketingActionCards.extend(repeat(("Marketing", generalHourCost[2]), generalCardQuantity[2]))


# Specialized Skills (design and technology):   9hr*3  +  11hr* 6  +  15hr*4
specializedHourCost = [9, 11, 15]          # Hour cost of special skill cards
specializedCardQuantity = [3, 6, 4]        # Quantities of special skill cards

technologyActionCards = []
technologyActionCards.extend(repeat(("Technology", specializedHourCost[0]), specializedCardQuantity[0]))
technologyActionCards.extend(repeat(("Technology", specializedHourCost[1]), specializedCardQuantity[1]))
technologyActionCards.extend(repeat(("Technology", specializedHourCost[2]), specializedCardQuantity[2]))

designActionCards = []
designActionCards.extend(repeat(("Design", specializedHourCost[0]), specializedCardQuantity[0]))
designActionCards.extend(repeat(("Design", specializedHourCost[1]), specializedCardQuantity[1]))
designActionCards.extend(repeat(("Design", specializedHourCost[2]), specializedCardQuantity[2]))


actionCardPile = researchActionCards + marketingActionCards + technologyActionCards + designActionCards

# create a random Resources pile and Actionable Cards pile
currentResourcePile = resourcePile.copy()
random.shuffle(currentResourcePile)
random.shuffle(currentResourcePile)

currentActionPile = actionCardPile.copy()
random.shuffle(currentActionPile)
random.shuffle(currentActionPile)
discardedActionPile = []
discardedActionPile.append(currentActionPile.pop())     # Adding 1st card to the discard pile

# Skill Cards costs and benefits

# generalSkillCost = [0, 500, 2000, 4000, 6000]
# generalSkillReduction = [0, 1, 3, 6, 9]

# specialSkillCost = [0, 1500, 3500, 4500, 7000]
# specialSkillReduction = [0, 2, 5, 8, 11]


# Service Cards
serviceCards = ["Research", "Marketing", "Design", "Technology"]

# MVP Cards (r,m,d,t)
MVPCards=[[3,2,3,2],[3,2,2,3],[2,3,3,2],[2,3,2,3],[3,2,3,2],[3,2,2,3],[2,3,3,2],[2,3,2,3]]


