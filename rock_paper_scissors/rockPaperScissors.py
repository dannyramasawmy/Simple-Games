
# import relevant modules
from random import randint


def getUserChoice():
    ''' This gets the user choice'''
    # get the choice with input
    userChoice = input('Rock, paper or scissors?')
    # set as lower case
    userChoice = userChoice.lower()
    # print so the user can see
    print("You have chosen {}".format(userChoice))    
    return userChoice


def getRobotChoice():
    '''Automatically choose for the robot'''    
    # list of robot optiob
    robotOptions = ["rock", "paper", "scissors"]
    # get random integer, find entry in list
    robotChoice = robotOptions[randint(0,2)]
    # Show the user what the robot chose
    print("Robot chose {}".format(robotChoice))
    return robotChoice


def welcomeMessage():
    ''' Prints the welcome message'''
    print('===========================================')
    print('Hello, you are playing rock paper scissors!')
    return None


def compareChoices(userChoice, robotChoice):
    ''' Compare the two options and return outcome'''
    # some outcome options
    outcomeOptions = ['user', 'robot', 'draw', 'wrong']

    # logic
    if userChoice == robotChoice:
        outcome = outcomeOptions[2]
    elif userChoice == 'rock' and robotChoice == 'paper':
        outcome = outcomeOptions[1]
    elif userChoice == 'rock' and robotChoice == 'scissors':
        outcome = outcomeOptions[0]
    elif userChoice == 'paper' and robotChoice == 'rock':
        outcome = outcomeOptions[0]
    elif userChoice == 'paper' and robotChoice == 'scissors':
        outcome = outcomeOptions[1]
    elif userChoice == 'scissors' and robotChoice == 'rock':
        outcome = outcomeOptions[1]
    elif userChoice == 'scissors' and robotChoice == 'paper':
        outcome = outcomeOptions[0]
    else:
        outcome = outcomeOptions[3]
    # return result
    return outcome


def assignScore(outcome):
    ''' Assigns the score based on the outcome'''
    
    # assign correct score, if its a bad choice the score is 0
    # also print who winds
    if outcome == 'user':
        userScore = 2
        robotScore = 0
        print('You wins!')
    elif outcome == 'robot':
        userScore = 0
        robotScore = 2
        print('The robot wins!')
    elif outcome == 'draw':
        userScore = 1
        robotScore = 1
        print('Its a draw')
    else:
        userScore = 0
        robotScore = 0
        print('Pass this game')
    # assign score to a list
    scores = [userScore, robotScore]
    return scores     

    
def playGame():
    '''The actual game'''
    
    # get the user choice
    userChoice = getUserChoice()  
    # get robot choice
    robotChoice = getRobotChoice()    
    # compare the choices
    outcome = compareChoices(userChoice, robotChoice)
    # print result
    scores = assignScore(outcome)
    # return the scores to 
    return scores


def updateScores(currentScore, newScore):
    '''Update and print scores'''  
    # first index is user score, second index is robot
    currentScore[0] = currentScore[0] + newScore[0]
    currentScore[1] = currentScore[1] + newScore[1]
    # print
    print("You:{} , robot:{}".format(currentScore[0], currentScore[1]))
    # return the current score as a list  
    return currentScore

def finalOutcome(currentScore):
    '''Prints the message for the winner'''
    
    # to make the output nice
    print('===========================================')
    print('             FINAL SCORE                   ')
    print('===========================================')
    
    # find out who wins
    if currentScore[0] > currentScore[1]:
        print('You win overall, noice!')
    elif currentScore[0] < currentScore[1]:
        print('You lose hahaha!')
    else:
        print('Its a draw :/')
    # return nothing
    return None
    
    
def main():
    '''The main function'''
    
    # print a welcome message
    welcomeMessage()    
    
    # initalise scores with 0 0, I have written it out to make it obvious
    userInitialScore   = 0
    robotInitialScore  = 0
    currentScore = [userInitialScore, robotInitialScore]
    
    # play 5 rounds of the game
    for gameRound in range(5):
        # round message
        print('===========================================')
        print("Round {}".format(gameRound))
        # run play game
        newScore = playGame()
        # update scores
        currentScore = updateScores(currentScore, newScore)
    
    # print the message for the final outcome after the 5 rounds
    finalOutcome(currentScore)
    
    # return none means return nothing
    return None
    
    
# run program
main()
