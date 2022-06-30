from string import capwords
from gameFunctions import *
from gameSetup import *
from gameCards import *


# how service works
# 1. first a player sees who offers the service 
# 2. the player has to know what is the time required by the service provider to buy that card 

def service(playerList,currentPlayer,currentResourcePile,discardedActionPile):


    def modifiedActionCardCost(currentTopActionCard,serviceProvider): #dont know if working


        startingLetter=currentTopActionCard[0][0]
        if startingLetter=='R':
            modifiedCost=currentTopActionCard[1] - serviceProvider.skillReduction[0]
        elif startingLetter=='M':
            modifiedCost=currentTopActionCard[1] - serviceProvider.skillReduction[1]
        elif startingLetter=='D':
            modifiedCost=currentTopActionCard[1] - serviceProvider.skillReduction[2]
        elif startingLetter=='T':
            modifiedCost=currentTopActionCard[1] - serviceProvider.skillReduction[3]

        
        return modifiedCost

    #function to buy service card
    def buyService(currentPlayer,chosenServiceProvider,modifiedCost,discardedActionPile):
        print(currentPlayer.money)
        print(chosenServiceProvider.time)
        agreedMoney=int(input("Please enter how much you have agreed to pay: "))
        if agreedMoney<=currentPlayer.money and chosenServiceProvider.time>=modifiedCost:
            chosenServiceProvider.addMoney(agreedMoney)
            currentPlayer.subtractMoney(agreedMoney)
            chosenServiceProvider.time-=modifiedCost
            discardedActionPile.pop()
        elif agreedMoney>currentPlayer.money and chosenServiceProvider.time>modifiedCost:
            print("You dont have enough money. You can try negotiating for a lesser price")
            return 0
        elif agreedMoney<currentPlayer.money and chosenServiceProvider.time<modifiedCost:
            print("Service Provider does not have enough time.")
            return 0
        else:
            print("You dont have enough money and service provider doesnt have enough time.You guys  are making the game slow")
        


    #basic defination of variables required 
    currentTopActionCardForService=discardedActionPile[-1]
    print("The Top Action card is {}\n".format(currentTopActionCardForService))

    playerListLocal=playerList.copy()
    playerListLocal.remove(currentPlayer)
    serviceProviderCounter=1

    #list of objects of all players who can provide this service
    cappableServiceProviders=[0]

    #displaying this list and the hours required by them to provide this service
    for serviceProvider in playerListLocal:
        for card in serviceProvider.serviceCards:
            if card==currentTopActionCardForService[0]:
                print("{}.{} provides this service".format(serviceProviderCounter,serviceProvider.name))
                modifiedCost=modifiedActionCardCost(currentTopActionCardForService,serviceProvider)
                print("---It will take {} hours for {} to provide this service\n".format(modifiedCost,serviceProvider.name))
                cappableServiceProviders.append(serviceProvider)
                serviceProviderCounter+=1
    
    #condition if no one provides this service that means player himself provides that service 
    if serviceProviderCounter==1:
        print("No one gives this service")
        return 0
    #options for player to either come out of service menu after seeing 
    #hours required by service players or negotiate with them for price
    print("1.Start negotiating service price")
    print("2.Pass\n")
    
    playerServiceBuyChoice=int(input())

    #statement if player wants to choose service negotiation
    if playerServiceBuyChoice==1:
        #basic statements to tell them to talk to each other
        print("You can now start negotiating with the service provider/ers .............. ")
        print("Press 1 when your negotiations are over")
        endNegotiation=0
        #loop that runs till player has negotiated final rpice
        while endNegotiation!=1:
            endNegotiation=int(input())
            if endNegotiation!=1:
                print("Take your time and press 1 when your negotiations are over")


        #here the negotiations are ended.

        print("Do you want to buy action card from service")
        print("1.Yes      2.No")
        playerChoice=int(input())
        if playerChoice==1:
            #this is the condition that checks if there is only one service provider so we do not need 
            # to ask player to choose between which servicve provider he has chosen.

            if len(cappableServiceProviders)==2:
                chosenServiceProvider=cappableServiceProviders[1]

            #if there are more than one service provider
            elif len(cappableServiceProviders)>2:
                a=1 
                print("Select the service Provider")
                #loop prints list of service providers that can provide the service in play rn
                for item in cappableServiceProviders:
                    if item==0:
                        continue
                    print("{}.{}".format(a,item.name))
                    a=a+1
                serialChosenServiceProvider=int(input())
                chosenServiceProvider=cappableServiceProviders[serialChosenServiceProvider]
                modifiedCost=modifiedActionCardCost(currentTopActionCardForService,chosenServiceProvider)
            #call of function of buyservice
            print("The service provider from whom your buying the service is {}".format(chosenServiceProvider.name))
            buyService(currentPlayer,chosenServiceProvider,modifiedCost,discardedActionPile)
            
        else:
            return 0
    #if player doesnt want service and passes 
    if playerServiceBuyChoice==2:
        return 0
    
    return 0




service(playerList,parth,currentResourcePile,discardedActionPile)