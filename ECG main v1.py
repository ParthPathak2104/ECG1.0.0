from gameCards import *
from gameSetup import *
from gameFunctions import *

playerTracker= 0    # variable to track the current player
win = 0             # variable to check if any player has won the game


while win == 0:
    endTurn = 0
    drawnCounter = 0
    while endTurn == 0:
        
        playerList= [parth, saksham, yajur]
        currentPlayer = playerList[playerTracker]       # Get current player's object from play list
        print("It's {}'s turn:".format(currentPlayer.name))
        print("**************************************")
        choice = getChoice()
        print("\n")

        if choice == 1:                                 # Chooses to trigger skill cards
            skillCards(currentPlayer)
        elif choice == 2:                              # Chooses to trigger actionable cards
            drawnCounter=actionCards(currentPlayer, currentActionPile, discardedActionPile, drawnCounter)
            print(drawnCounter)
        elif choice == 3:                               # Chooses to view Resources hand
            currentPlayer.printResources()
            print("\n")
        elif choice == 4:
            currentPlayer.printHold()
            print("\n")
        elif choice == 9:
            if checkWin(currentPlayer):
                print("\n**************************************")
                print("Congrats!! {} wins the game".format(currentPlayer.name))
                print("**************************************")
                win = 1
            if drawnCounter==0:
                print("You have drawn 0 action cards in this chance. It is compulsary to draw atleast 1 action card")
            else:
                currentPlayer.drawResource(3, currentResourcePile)
                print("\n\n\n**************************************")
                endTurn = 1

    playerTracker += 1
    playerTracker = playerTracker % 3
print("GAME OVER")
    
        
        