#Francesco Melpignano

from cards import *

class SoloBlackjack(object):
    '''A game of solo blackjack'''

    def __init__(self):
        '''this function initializes the game by providing  shuffled deck and
        the playing board'''
        self.deck = Deck()
        self.deck.shuffle()
        self.dealtCard = None
        self.table = {'row1':[1, 2, 3, 4, 5], 'row2': [6, 7, 8, 9, 10],
                      'row3':[11, 12, 13], 'row4':[14, 15, 16]}
        self.discards = [17, 18, 19, 20]

    def deal(self):
        '''deals a card, but does not return its value,
        raises IndexError if deck is empty'''
        self.dealtCard = self.deck.deal()

    def getDealtCard(self):
        '''returns the value of the last card dealt'''
        return self.dealtCard

    def getTableRows(self):
        '''returns list of lists of four horizontal hands'''
        rowNames = ['row1', 'row2', 'row3', 'row4']
        return [[card for card in self.table[rowName]] for rowName in rowNames]

    def getTableColumns(self):
        '''returns list of list of the five vertical hands'''
        columns = [[] for column in range(5)]
        for row in self.getTableRows():
            if len(row) == 5:
                offset = 0
            else:
                offset = 1
            for columnNum in range(len(row)):
                columns[columnNum + offset].append(row[columnNum])
        return columns
        
    def makeMove(self, position):
        '''Places dealt card at a given position, raises
        RuntimeError if not possible'''
        if not(1 <= position <= 20):
            raise RuntimeError, "value out of board range"
        rowToChange = None
        indexToChange = None
        if position <= 5:
            rowToChange = self.table['row1']
            indexToChange = position - 1
        elif position <= 10:
            rowToChange = self.table['row2']
            indexToChange = position - 6
        elif position <= 13:
            rowToChange = self.table['row3']
            indexToChange = position - 11
        elif position <= 16:
            rowToChange = self.table['row4']
            indexToChange = position - 14
        else:
            rowToChange = self.discards
            indexToChange = position - 17
        if rowToChange[indexToChange] != position:
            raise RuntimeError, "position is occupied"
        rowToChange[indexToChange] = self.getDealtCard()
            
  
    def scoreHand(self, hand):
        '''returns the solo blackjack score for hand (list of Card objects),
        raises AttributError if hand is incomplete'''
        rankValues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10,
                      'k': 10, 'a': 1}
        handNoSuits = [card.get_rank() for card in hand]
        cardValues = [rankValues[rank] for rank in handNoSuits]
        tentativeSum = sum(cardValues)
        if tentativeSum <= 11 and 1 in cardValues:
            tentativeSum += 10
        if len(cardValues) == 2 and tentativeSum == 21:
            return 10
        if tentativeSum == 21:
            return 7
        if tentativeSum == 20:
            return 5
        if tentativeSum == 19:
            return 4
        if tentativeSum == 18:
            return 3
        if tentativeSum == 17:
            return 2
        if tentativeSum <= 16:
            return 1
        else:
            return 0

    def scoreTable(self):
        '''returns total score in the game,
        Raises AttributeError if game is incomplete'''
        rowScore = sum([self.scoreHand(row) for row in self.getTableRows()])
        columnScore = sum([self.scoreHand(column) for column in self.getTableColumns()])
        return rowScore + columnScore
        
    def isGameComplete(self):
        '''returns true if table is full of cards'''
        try:
            self.scoreTable()
        except AttributeError:
            return False
        return True

    def displayBoard(self):
        '''prints board info to console'''
        print 'Current Board: '
        for row in self.getTableRows():
            rowString = "\t".join([str(card) for card in row])
            if len(row) == 5:
                print rowString
            else:
                print "\t" + rowString
        print "\nDiscards: "
        print "\t".join([str(card) for card in self.discards])
        print "\nDealt Card: "
        print str(self.getDealtCard())

    def askUserForMove(self):
        '''prompts the user for move and makes the move'''
        goodInput = False
        while not goodInput:
            userChoice = raw_input("Please enter your next desired location: ")
            try:
                self.makeMove(int(userChoice))
            except RuntimeError, e:
                print e
            except ValueError, e:
                print "Please enter an integer representing an available location"
            else:
                goodInput = True
    
    def scoreGame(self):
        '''prints final state and score of the game to the console'''
        self.displayBoard()
        print "YOUR TOTAL SCORE IS: " + str(self.scoreTable())
        
        
    def play(self):
        '''plays one game of solo blackjack'''
        print "Welcome to Solo Blackjack!"
        while not self.isGameComplete():
            self.deal()
            self.displayBoard()
            self.askUserForMove()
        self.scoreGame()
        
   

if __name__ == '__main__':
    game = SoloBlackjack()
    game.play()

        
