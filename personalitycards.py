#Personality Cards
#the cards will be in the form of a dictionary with the key being the card name and the value being its description and cooldown array
#or can make a name description and cooldown as array for every card.

#format-
#["name","description",cooldown]
#{"name":["description",cooldown]}
import random
from gameSetup import *
personalityCards=[
    ("Hustler","Get a 5 hour discount on any actionable card",5),
    ("Innovator","Get a $2500 discount on any skill card",4),
    ("Buyer","Draw 2 extra actionable cards for free",3),
    ("Opportunist","Get a free Chance card",4),
    ("Solopreneur","Pick 2 extra resources",4),
    ("Rebel","Move your skill from one division to another but on the same level",5),
    ("Wannapreneur","Get a free level 1 or 2 skill card",3)
]

def getPersonlityCards(personalityCards):
    personalityCardsCopy=personalityCards.copy()
    random.shuffle(personalityCardsCopy)
    random.shuffle(personalityCardsCopy)
    
    return personalityCardsCopy

#to devide in players return it in some variable and pop it from there while giving arguments

#use ur personality card

# print("Are you sure you want to  use your personality card?")
#     print("1.Yes            2.No")
#     playerConfirmation=int(input())
#     if playerConfirmation==1:
#         personalityCard(player)
#     
#     elif playerConfirmation==2:
#         continue

def personalityCard(player,currentResourcePile):

    def solopreneur(player,currentResourcePile):
        player.drawResource(2, currentResourcePile)
        player.cooldown=0

    def rebel(player):
        validChoice=0
        while validChoice==0:
            print("Your current skill levels are as follows(R,M,D,T) :{}".format(player.skillLevel))
            print("You can move your skill from one division to another but on the same level ie R to M and D to T or viceversa")
            print("which skill do you want to move")
            if player.skillLevel[0]>player.skillLevel[1]:
                print("1.You can move Research Skill to Marketing skill")
                a=0
                b=1
            elif player.skillLevel[1]>player.skillLevel[0]:
                print("1.You can move Marketing Skill to Research skill")
                a=1
                b=0
            elif player.skillLevel[1]==player.skillLevel[0]:
                print("1.You cannot interchange any general skill")
                
            
            if player.skillLevel[2]>player.skillLevel[3]:
                print("2.You can move Design Skill to Technology skill")
                c=2
                d=3
            elif player.skillLevel[3]>player.skillLevel[2]:
                print("2.You can move Technology Skill to Design skill")
                c=3
                d=2
            elif player.skillLevel[2]==player.skillLevel[3]:
                print("2.You cannot interchange any specialised skill")
                
            print("3.Back")
            playerRebelChoice=int(input())
            
            if playerRebelChoice==1:
                if player.skillLevel[0]== player.skillLevel[1]:
                    validChoice=1
                    return 0
                else:
                    player.skillLevel[a]-=1
                    player.skillLevel[b]+=1
                    player.cooldown=0
                    validChoice=1
            elif playerRebelChoice==2:
                if player.skillLevel[2]==player.skillLevel[3]:
                    validChoice=1
                    return 0
                else:
                    player.skillLevel[c]-=1
                    player.skillLevel[d]+=1
                    player.cooldown=0
                    validChoice=1

            elif playerRebelChoice==3:
                validChoice=1
                return 0
            
            else:
                print("Please enter a valid choice number")
                print("*******************************\n")
                validChoice=0

    def wannapreneur(player):
        validChoice=0
        while validChoice==0:
            skillName=["","Research","Marketing","Design","Technology"]
            print("Your current skill levels are as follows(R,M,D,T) :{}".format(player.skillLevel))
            print("You have the following options (SkillName    --> UpgradedLvl)\n")
            upgradableskill=[]
            nameCounter=1
            for item in player.skillLevel:
                if item<2:
                    print("{}.{}   ---> {}".format(nameCounter,skillName[nameCounter],(item+1)))
                    upgradableskill.append(nameCounter)
                elif item>=2:
                    print("{}.You cannot upgrade {} skill with personality card as it has reached level 2".format(nameCounter,skillName[nameCounter]))
                nameCounter+=1
            
            playerUpgradeChoice=int(input("Which skill do you want to upgrade: "))
            
            if playerUpgradeChoice in upgradableskill:
                for skillNumber in upgradableskill:
                    if playerUpgradeChoice==skillNumber:
                        player.skillLevel[skillNumber-1]+=1
                        break
                validChoice=1
            else:
                print("Enter a valid choice")
                print("*******************************************\n")
                validChoice=0

    def hustler(player,discardedActionPile):

        print("The topmost card is {}".format(discardedActionPile[-1]))
        print("You can use your 5 hour discount by buying action card from the action card menu")
        print("Steps--")
        print("1.Go to action card menu ")    
        print("3.Choose buy action card")
        print("Your extra discount will be availed there")  

    def innovator(player):
        player.printSkillLevel()
        print("You can use your 2500$ discount by buying skill card from the skill card menu")
        print("Steps--")
        print("1.Go to Skill card menu ")    
        print("3.Choose buy Skill card")
        print("Your extra discount will be availed there") 

    def buyer(player,discardedActionPile):
        print("The topmost card is {}".format(discardedActionPile[-1]))
        print("You can  draw upto 2 free action cards from the action card menu")
        print("Steps--")
        print("1.Go to action card menu ")    
        print("3.Choose draw action card")
        print("Your can draw upto two action cards for free from there")

    if player.perosnalityCardName=="Hustler":
        hustler(player)
    elif player.perosnalityCardName=="Innovator":
        innovator(player)
    elif player.perosnalityCardName=="Buyer":
        buyer(player)
    elif player.perosnalityCardName=="Opportunist":
        opportunist(player)
    elif player.perosnalityCardName=="Solopreneur":
        solopreneur(player)
    elif player.perosnalityCardName=="Rebel":
        rebel(player)
    elif player.perosnalityCardName=="Wannapreneur":
        wannapreneur(player)





