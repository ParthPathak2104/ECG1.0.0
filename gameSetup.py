import random
from gameCards import *

class player():
    
    def __init__(self, number, name, MVP, serviceCards,personalityCard ):#******************created new
        self.playerNumber = number
        self.name = name
        self.time = 0
        self.money = 0
        self.skillLevel = [0,0,0,0]         # skill level is in the order Research, Media, Design, Technology
        self.actionCards = [0,0,0,0]        # this convention is followed for all skill and actions lists further
        self.MVP = MVP
        self.serviceCards = serviceCards
        self.resourceCardsNumber = 0
        self.skillReduction = [0,0,0,0]     # variable holding the discount value of each action due to player skill
        self.perosnalityCard=personalityCard #********************created new
        self.perosnalityCardName=personalityCard[0]
        self.perosnalityCardDef=personalityCard[1]
        self.perosnalityCardCoolDown=personalityCard[2]
        self.cooldown=personalityCard[2]
        # Initial Creation of a player
        print("Creating player {}: {}".format(self.playerNumber, name))
        print("\n********************************")
        self.printMVP()
        self.printServiceCards()
        self.printPersonalityCard()#***************created new 
        print("********************************\n")
        # Drawing 4 initial resources as the starting hand
        print("Drawing initial resources")    
        self.drawResource(4, currentResourcePile)


    # Functions to print player info
    # to print cards held
    def printTime(self):
         print("Total Time:   {} hrs".format(self.time))
    
    def printMoney(self):
        print("Total Money:   ${}".format(self.money))
    
    def printResourceCardsNumber(self):
        print("You have {} resources cards in hand".format(self.resourceCardsNumber))
    def printResources(self):
        print("Total Time:   {} hrs".format(self.time))
        print("Total Money:   ${}".format(self.money))
        
    def printSkillLevel(self):
        print("Your current Skill Level (R,M,D,T) is: {}".format(self.skillLevel))
    
    def printActionCards(self):
        print("You have acquired the following Actionable Cards (R,M,D,T): {}".format(self.actionCards))
    
    def printSkillReduction(self):
        print("Your current discount on skills (R,M,D,T) is:    {}".format(self.skillReduction))
    
    # to print every card player owns
    def printHold(self):
        print("Total number of Resource Cards: {}".format(self.resourceCardsNumber))
        print("Money: {}    Time: {}".format(self.money, self.time))
        print("Skill Level (R,M,D,T):   {}".format(self.skillLevel))
        print("Actionable Cards (R,M,D,T):  {}".format(self.actionCards))
        

    # function to show your MVP
    def printMVP(self):
        print("Your MVP requirement (R,M,D,T) is:   {}".format(self.MVP))
    # function to show your Service Cards
    def printServiceCards(self):
        print("You can offer the following services:    {}".format (self.serviceCards))
    #function to show your personality card
    def printPersonalityCard(self):#******* created New ********
        print("Your Personality Card is n: {} ".format(self.perosnalityCardName)) 
        print("Function: ".format(self.perosnalityCardDef))
        print("Cooldown: {}".format(self.perosnalityCardCoolDown))

    # function to draw n Resource Cards
    def drawResource(self, n, currentResourcePile):
        for i in range(n):
            resource = currentResourcePile.pop()
            if resource < 10:
                self.time += resource
                print("{} drew:    {} hrs".format(self.name, resource))
            else:
                self.money += resource
                print("{} drew:    ${}".format(self.name, resource))
        self.resourceCardsNumber += n
        print("\n")
        self.printResourceCardsNumber()
        self.printResources()
    #functions to add/subtract money or time
    def addMoney(self,moneyToBeAdded):
        self.money+=moneyToBeAdded
    def subtractMoney(self,moneyToBeSubtracted):
        self.money-=moneyToBeSubtracted
    def addTime(self,timeToBeAdded):
        self.time+=timeToBeAdded
    def subtractTime(self,timeToBeSubtracted):
        self.time-=timeToBeSubtracted

def getServicecards(serviceCards):
    NumberOfplayers=input("Number of players: ")

    if NumberOfplayers=='3':
        serviceCardscopy=serviceCards.copy()
        random.shuffle(serviceCardscopy)
        serviceCardscopy.pop(3)
        return serviceCardscopy

    elif NumberOfplayers=='4':
        serviceCardscopy=serviceCards.copy()
        random.shuffle(serviceCardscopy)
        return serviceCardscopy

    elif NumberOfplayers=='5':
        serviceCardscopy=serviceCards.copy()
        random.shuffle(serviceCardscopy)
        
        serviceCardscopy2=serviceCards.copy()
        random.shuffle(serviceCardscopy2)

        serviceCardsshuffled=0 #means cards are not properly shuffled for distribution yet ie two players can get same card

        while serviceCardsshuffled==0: 
            if serviceCardscopy[0]==serviceCardscopy2[0] or serviceCardscopy[1]==serviceCardscopy2[1] or serviceCardscopy[2]==serviceCardscopy2[2] or serviceCardscopy[3]==serviceCardscopy2[3]:
                random.shuffle(serviceCardscopy2) 
            else:
                serviceCardsshuffled=1 #means cards are properly shuffled for distribution yet ie no two players can get same card
    #to give random service cards to players use pop function inside object attribute.
    #  NOTE- for 5 players give array of both coppy of service cards having same index
    else:
        print("Enter between 3-5 players")
        exit()

def getMVP(MVPCards):   #to give random MVP cards to players use pop function inside object attribute
    MVPCardscopy=MVPCards.copy()
    random.shuffle(MVPCardscopy)
    return MVPCardscopy

playerName= ["Parth", "Saksham", "Yajur"]

# HARDCODING PLAYERS WITH CERTAIN MVPS AND SERVICE CARDS FOR PLAYTESTING
print("\n\n")
parth= player(1, playerName[0], [2,3,2,3], ["Research"],("Rebel","Move your skill from one division to another but on the same level",5))
print("\n\n")
saksham= player(2, playerName[1], [3,2,3,2], ["Design","Technology"],("Solopreneur","Pick 2 extra resources",3))
print("\n\n")
yajur= player(3, playerName[2], [2,3,3,2], ["Marketing","Technology"],("Wannapreneur","Get a free level 1 or 2 skill card",2))
print("\n\n")


playerList= [parth, saksham, yajur]
# TO GIVE RANDOM MVP AND SERVICE CARDS AND INITIATING PLAYERS
# currentMVPCards= getMVP(MVPCards)
# currentServiceCards= getServicecards(serviceCards)
# p1= player("Saksham", currentMVPCards.pop(), currentServiceCards.pop())


parth.skillLevel=[4,4,3,2]



