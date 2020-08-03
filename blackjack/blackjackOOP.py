from random import shuffle, randint

# ==============================================================================
#   PLAYER CLASS
# ==============================================================================
class Player:
    def __init__(self, name='Player'):
        # the current collection of cards
        self.hand = CardGroup()
        # the name of the player
        self.name = name
        # the state, stick/twist/bust
        self.state = 'twist'
        
    def getPlayerName(self, userNumber=''):
        '''Get the payer name'''
        self.name = input('Hi Player {}, what is your name?'.format(userNumber))
        print('Hi {}, lets go!'.format(self.name))
        return None

    def getChoice(self):
        '''Get the choice and update state.'''
        
        # exit if bust
        if self.tally > 21:
            print('YOU WENT BUST!!!')
            self.state = 'stick'
            return None
        
        # get input
        playerChoice = input("Stick or twist?")
        # format
        playerChoice = playerChoice.lower()
        print(playerChoice)
        if playerChoice == 'stick':
            print('You have chosen to stick!')
            self.state = 'stick'
        elif playerChoice == 'twist':
            print('You have chosen to twist!')
            self.state = 'twist'
        else:
            print('Not valid, Type your answer again!')
            self.getChoice()
            
        return None

    def showHand(self):
        '''Print the hand to the screen.'''
        print('{} hand: total = {}'.format(self.name, self.tally))
        print(self.hand)
        return None

    @property
    def tally(self):
        '''Counts the cards in hand.'''
        return self.hand.total

    def addCard(self,card):
        '''Add a card to the hand.'''
        self.hand.addCard(card)
        return None

    def changeAceValue(self):
        ''' Change the value of ace between 11 and 1.'''
        # for every card in the hand
        for card in self.hand:
            # for all the aces
            if card.isAce == True:
                # ask if they want to switch the value
                #self.showHand()           
                print('You have an {}'.format(card.__str__()))
                choice = input('Would you like to change the value of the ace? [y/n?]')   
                if choice == 'y':
                    card.flipAceValue()    
        
        print(' ')              
        return None
    
    def reset(self):
        '''Remove cards in the hand'''
        self.hand = CardGroup()
        self.state = 'twist'
        return None
    
    
    
    def __repr__(self):
        '''String representation'''
        return '{}: {} cards in hand'.format(self.name, self.hand.length)

    
# ==============================================================================
#   ROBOT CLASS
# ==============================================================================
    
class Robot(Player):
    def __init__(self):
        Player.__init__(self, name='Robot')
        
    def getPlayerName(self, userNumber=''):
        '''OVerride super class get name'''
        print('Hi Player {}, what is your name?'.format(userNumber))
        self.name = 'Robot{}'.format(randint(1000,2000))
        print('Hi {}, lets play!'.format(self.name))
        return None

    def getChoice(self):
        '''Automatic choice with robot logic.'''
        # what value to decide to stick or twist
        decideValue = 17
        # choose to stick or twist
        if self.tally < decideValue:
            self.state = 'twist'
            print('{} chooses to twist'.format(self.name))
        else:
            self.state = 'stick' 
            print('{} chooses to stick'.format(self.name))
        # return the choice   
        return None

    def changeAceValue(self):
        '''Automatic choice with robot.'''
        return None


# ==============================================================================
#   CARD CLASS
# ==============================================================================    
    
class Card:
    def __init__(self, name='Ace', suit='Spades'):
        # the name of the card
        if name in self.availableNames:
            self.name = name
        # the suit of the card
        if suit in self.availableSuits:
            self.suit = suit
        # the value of the card
        self.value = self.availableNames[name]
        # boolean if ace
        self.isAce = False
        # assign true so isAce if Ace
        self.checkAce()
    
    @property # this is a property decorator (fnc is an attribute)
    def  availableNames(self):
        '''Get the available card names as a dictionary'''
        availableNames = {
            'Ace':11, '2':2, '3':3, 
            '4':4, '5':5, '6':6, 
            '7':7, '8':8, '9':9, '10':10,
            'Jack':10, 'Queen':10, 'King':10
            }
        return availableNames

    @property
    def availableSuits(self):
        '''Get the list of available suits'''
        availableSuits = ['Diamonds','Clubs','Hearts','Spades']
        return availableSuits

    def flipAceValue(self):
        '''Changes if the ace is 1 or 11'''
        if self.isAce == True:
            if self.value == 1:
                self.value = 11
            elif self.value == 11:
                self.value = 1
        return None

    def checkAce(self):
        ''' Checks the name, if Ace then change isAce bool'''
        if self.name == 'Ace':
            self.isAce = True
        return None

    def __str__(self):
        '''Print function.'''
        return('{} of {} | Value : {}'.format(self.name, self.suit, self.value))

    def __repr__(self):
        '''Best string representation'''
        return(self.__str__())

    
# ==============================================================================
#   CARD GROUP CLASS
# ==============================================================================

class CardGroup:
    def __init__(self):
        # initialise with a loop
        self.cards = []
        self.iterValue = 0
    
    def __getitem__(self, key):
        '''Get an indexed card'''
        return self.cards[key]
    
    def getCard(self):
        '''Get the first card from the pile'''
        # get the first card
        if self.length:
            returnCard = self.cards[0]
            # remove the first card from the array
            self.removeCard()
            return returnCard
        else:
            return None

    def addCard(self, card):
        self.cards.append(card)
        return None

    @property
    def length(self):
        ''' The number of cards in the group'''
        return len(self.cards)

    def removeCard(self):
        '''Removes the first card.'''
        self.cards.pop(0)

    @property
    def total(self):
        '''Iterate through the cards and get their total.'''
        total = 0
        for card in self:
            total = total + card.value
        return total

    def print(self):
        '''Prints cards in hand'''
        for card in self:
            print(card)
        return None
    
    def __iter__(self):
        '''Make card group iterable'''
        self.iterValue = 0
        return self
    
    def __next__(self):
        '''Make card group iterable'''
        if self.iterValue < len(self.cards):
            returnCard = self.cards[self.iterValue]
            #  add 1 to counter
            self.iterValue += 1
            return returnCard
        else:
            raise StopIteration
            
    def __str__(self):
        '''Print function.'''
        # returnString = 'Your cards: ({}) \n'.format(self.length)
        returnString = ''
        for card in self:
            returnString = returnString + card.__str__() + '\n'
        return(returnString)

    def __repr__(self):
        return(self.__str__())

# ==============================================================================
#   CARD DECK CLASS
# ==============================================================================   
            
class CardDeck(CardGroup):
    def __init__(self, shuffleDeck=False):
        '''Initialise with 52 cards'''
        self.cards = []
        # loop over all names and suits and add to deck
        for cardSuit in Card().availableSuits:
            for cardName in Card().availableNames:
                self.addCard(Card(cardName, cardSuit))
        # if shuffle deck is true the shuffle
        if shuffleDeck == True:
            self.shuffleDeck()

    def shuffleDeck(self):
        '''Shuffle the order of the cards.'''
        shuffle(self.cards)
        return None

# ==============================================================================
#   DEALER CLASS
# ==============================================================================
    
class Dealer:
    def __init__(self):
        # a collection of cards
        self.decks = CardDeck()
        self.burnPile = CardGroup()

    def dealCard(self):
        '''Select a card from the deck'''
        return self.decks.getCard()

    def shuffleCards(self):
        '''Shuffle the deck'''
        self.decks.shuffleDeck()

    def burnCard(self):
        '''Gets rid of the first card of the deck.'''
        print('Burning a card.')
        self.burnPile.addCard(self.decks.getCard())
        return None

    @property
    def remainingCards(self):
        return self.decks.length
        
    def addDeck(self):
        '''Add a deck of cards'''
        pass
    
    def __repr__(self):
        '''String representation'''
        return 'Dealer: {} remaining cards'.format(self.remainingCards)
    

# ==============================================================================
#   OTHER FUNCTIONS 
# ==============================================================================

def twoPlayers():
    '''Returns true for two players false for one'''
    # ask question
    choice = input('Would you like one or two players? [one/two]')
    # assign boolean
    if choice == 'two':
        players = True
    elif choice == 'one':
        players = False
    else:
        players = twoPlayers()
    return players
    
# ==============================================================================
#   OTHER FUNCTIONS 
# ==============================================================================
    
def addGameScore(scores, playerOne, playerTwo):
    '''Decide who wins'''
    
    print('====================================')
    # player one OK player two ok
    if (playerOne.tally <= 21) and (playerTwo.tally <= 21):
        # equal scores
        if playerOne.tally == playerTwo.tally:
            print('Its a draw')
            playerOneAdd = 1
            playerTwoAdd = 1
            
        # player one higher
        elif playerOne.tally > playerTwo.tally:
            print('Player one wins') 
            playerOneAdd = 2
            playerTwoAdd = 0
            
        # player two higher
        elif playerOne.tally < playerTwo.tally:
            print('Player two wins') 
            playerOneAdd = 0
            playerTwoAdd = 2
    
    # player one OK player two bust
    elif (playerOne.tally <= 21) and (playerTwo.tally > 21):
        print('Player one wins')  
        playerOneAdd = 2
        playerTwoAdd = 0
    
    # player one bust player two ok
    elif (playerOne.tally > 21) and (playerTwo.tally <= 21):
        print('Player two wins')
        playerOneAdd = 0
        playerTwoAdd = 2
        
    # player one bust player two bust    
    else:
        print('Neither player wins')
        playerOneAdd = 0
        playerTwoAdd = 0
    
    # update scores
    scores[0] = scores[0] + playerOneAdd
    scores[1] = scores[1] + playerTwoAdd
    
    print('{} scores: {} | {} scores {}'.format(playerOne.name, scores[0], playerTwo.name, scores[1]))
    
    return scores

def finalScore(scores):
    '''Who is the ultimate winner'''
    print(' ')
    print('======================================')
    if scores[0] == scores[1]:
        print('Its a draw overall!')
    elif scores[0] < scores[1]:
        print('Player two wins overall!')
    elif scores[0] > scores[1]:
        print('Player one wins overall!')
    
    print('======================================')

# ==============================================================================
#   MAIN GAME CLASS
# ==============================================================================

    
def playGame():
    
    # print colours
    white = "\033[1;37;48m"
    green = "\033[1;32;48m"
    purple = "\033[1;35;48m"
    red = "\033[1;31;48m"
        
    # initialise players and the dealer
    playerOne = Player()
    playerTwo = Robot()
    dealer = Dealer()
    # check if one or two players
    if twoPlayers():
        playerTwo = Player()
        
    # initialise score
    playerOneScore = 0
    playerTwoScore = 0
    scores = [playerOneScore, playerTwoScore]
    
    # get the player names
    print(green)
    playerOne.getPlayerName('One')
    print(purple)
    playerTwo.getPlayerName('Two')
    
    # play three games
    numberGames = 3
    
    for game in range(numberGames):
        gameCounter = game + 1
        # shuffle the deck, although the deck is already shuffled
        dealer.shuffleCards()

        # give top two cards to the player
        playerOne.addCard( dealer.dealCard() )
        # give next two cards to the robot
        playerTwo.addCard( dealer.dealCard() )

        roundCounter = 1
        

        # Loop
        while (playerOne.state == 'twist') or (playerTwo.state == 'twist'):
            print(white) # sets the colors
            print('====================================')
            print('   ROUND {}  | GAME {}'.format(roundCounter, gameCounter))
            print('====================================')
            roundCounter += 1
            # get the choices from player and robot
            # deal cards
            if playerOne.state == 'twist':
                print(green) # sets the colors
                playerOne.addCard( dealer.dealCard() )
                playerOne.showHand()
                playerOne.changeAceValue() if roundCounter > 1 else 'do nothing'
                playerOne.getChoice()

            if playerTwo.state == 'twist':
                
                print(white) # sets the colors
                if playerOne.state == 'twist':
                    print('====================================') 
                print(purple) # sets the colors
                
                playerTwo.addCard( dealer.dealCard() )
                playerTwo.showHand()
                playerTwo.changeAceValue() if roundCounter > 1 else 'do nothing'
                playerTwo.getChoice()
                
            # click to continue
            print(red)
            input('...press enter to continue...')

        print(red)                
        print('====================================')
        print('   FINAL TALLY | GAME {}'.format(gameCounter))
        print('====================================')
        print(green)
        playerOne.showHand()
        print(white)
        print('------------------------------------')
        print(purple)
        playerTwo.showHand()
    
    
        print(red)
        input('...press enter to continue...')
    
        # get the scores here
        scores = addGameScore(scores, playerOne, playerTwo)
    
        # reset the players
        playerOne.reset() 
        playerTwo.reset()
        
    # print final score       
    finalScore(scores)
            
    return 
    
    
# main script
if __name__ == '__main__': 
    playGame()
    
    
# tests
"""
player = Player()
player.addCard( Card('Ace','Hearts') )
player.addCard( Card('Ace','Spades') )
player.addCard( Card('Ace','Diamonds') )
player.addCard( Card('Ace','Clubs') )
player.changeAceValue()
"""

