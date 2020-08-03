# imports
from random import randint

# functions
def getPlayerChoice(playerHand):
    ''' Get player choice: stick or twist'''
    # show the cards
    showHand(playerHand, "Your")
    # get input
    playerChoice = input("Stick or twist?")
    # format
    playerChoice = playerChoice.lower()
    if playerChoice == 'stick':
        print('You have chosen to stick!')
    elif playerChoice == 'twist':
        print('You have chosen to twist!')
    else:
        playerChoice = 'twist'
        print('Typo, lets TWIST!')
    return playerChoice
    
def getRobotChoice(robotHand):
    '''Decide if robot should stick or twist'''
    # what value to decide to stick or twist
    decideValue = 17
    # get current score by adding hand
    currentScore =  addCards(robotHand) 
    # choose to stick or twist
    if currentScore < decideValue:
        robotChoice = 'twist'
    else:
        robotChoice = 'stick' 
    # return the choice   
    return robotChoice


def dealCard(shouldDeal):
    ''' Returns a random card'''
    if shouldDeal == True:
        # define cards
        cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        # get random integer
        randomCard = cards[randint(0,12)]
    else:
        # return 0 if should Deal is 0
        randomCard = 0
    # return the dealt card
    return randomCard
    
    
def addCards(hand):
    '''sums the cards'''
    totalScore = 0
    # check hand and add, if J,Q,K then 10
    for card in hand:
        if card == 'A':
            totalScore = totalScore + 11
        elif card == 'J' or card == 'Q' or card == 'K':
            totalScore = totalScore + 10
        else:
            totalScore = totalScore + card
    # return the total score
    return totalScore
    

def checkIfBust(hand):
    ''' checks if bust returns bool'''
    handTotal = addCards(hand)
    if handTotal > 21:
        bust = True
    else:
        bust = False
    return bust
    

def showHand(dealtHand, name):
    ''' Prints the score'''
    print("{} hand is : ".format(name))
    print(dealtHand)
    return None

def compareScores(robotHand, playerHand):
    ''' compare player and robot scores'''
    
    robotBust = checkIfBust(robotHand)
    playerBust = checkIfBust(playerHand)
            
    if playerBust == True:
        print('You went bust you lose!')
    else:
        if robotBust == True:
            print('The robot went bust')
            print('You won')
        else:
            # calculate the score
            playerScore = addCards(playerHand)
            robotScore = addCards(robotHand)

            if playerScore == robotScore:
                print("its a draw")
            elif playerScore > robotScore:
                print("you win")
            else:
                print("you lose")            
    return None


# initial player and robot state
dealRobot = True
dealPlayer = True

# initialise
robotHand = []
playerHand = []

# round counter
totalRoundCounter = 1

while (dealRobot == True) or (dealPlayer == True):
    
    # welcome
    print('===========================')
    print("This is round {}".format(totalRoundCounter))
    
    #  definitely do not need more than 10 rounds
    totalRoundCounter = totalRoundCounter + 1
    # set both to false if played more than 10 rounds
    if totalRoundCounter == 10:
        dealRobot = False
        dealPlayer = False
    
    # add new cards to the hand
    if dealRobot == True:
        robotHand.append( dealCard(dealRobot ))
    if dealPlayer == True:
        playerHand.append(dealCard(dealPlayer))

    # show hand 
    showHand(robotHand, "Robot")
    #showHand(playerHand, "Player")
    
    # get the choices
    if dealRobot == True:
        robotChoice = getRobotChoice(robotHand)
    if dealPlayer == True:
        playerChoice = getPlayerChoice(playerHand)

    # change boolean if robot is staying
    if robotChoice == 'twist':
        dealRobot = True
    else: 
        dealRobot = False
    # if player stays then leave while loop
    if playerChoice == 'twist':
        dealPlayer = True
    else: 
        dealPlayer = False
        

print('===========================')
showHand(robotHand, 'Final robot')
print("final score {}:".format(addCards(robotHand)))
showHand(playerHand, 'Final player ')
print("final score {}:".format(addCards(playerHand)))
# final scores
compareScores(robotHand, playerHand)
# print the end message
print('Game end, thank you for playing.')
