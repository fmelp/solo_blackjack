#Francesco Melpignano
import random  

class Card(object):
    '''represents a playing card'''
    
    def __init__(self, r, s):
        '''where r is the rank, s is suit'''
        self.r = str(r).lower()
        self.s = s.lower()

    def __str__(self):
        '''returns lowercase string with rank + suit'''
        return self.get_rank() + self.get_suit()

    def get_rank(self):
        '''returns lowercase rank string'''
        return self.r

    def get_suit(self):
        '''returns lowercase suit string'''
        return self.s

class Deck():
    """Denote a deck to play cards with"""
     
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        
        rankList = ['a', '2', '3', '4', '5', '6', '7', '8', '9',
                    '10', 'j', 'q', 'k']
        suitList = ['s', 'c', 'h', 'd']
        self.__deck = [Card(r, s) for r in rankList for s in suitList]
        
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        '''returns a copied list of all cards'''
        return [card for card in self.__deck]

    def deal(self):
        '''return and remove the last card of the deck'''
        return self.__deck.pop()
    
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them 
        return reduce(lambda x,y: x + str(y) + "\n", self.__deck, '')
