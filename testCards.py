#Francesco Melpignano

from cards import *
import unittest

class TestCard(unittest.TestCase):

    def testInit(self):
        '''tests cards can be created case insensitvely'''
        cardList = [Card('A', 'c'), Card('a', 'c'), Card('J', 'd'),
              Card('q', 'h'), Card('K', 's'), Card('6', 'd'),
              Card(6, 'd'), Card('10', 's')]
        rankList = ['a', 'a', 'j', 'q', 'k', '6', '6', '10']
        suitList = ['c', 'c', 'd', 'h', 's', 'd', 'd', 's']
        for card, rank, suit in zip(cardList, rankList, suitList):
            self.assertEqual(card.get_rank(), rank)
            self.assertEqual(card.get_suit(), suit)

    def testGetRank(self):
        '''tests that the rank part of the card as a string corresponds'''
        self.assertEqual(Card('6', 's').get_rank(), '6')

    def testGetSuit(self):
        '''tests that the suit part of the card as a string corresponds'''
        self.assertEqual(Card('6', 's').get_suit(), 's')

    def testStr(self):
        '''tests return of rank + string concatenation'''
        self.assertEqual(str(Card('6', 's')), '6s')

class TestDeck(unittest.TestCase):

    def testInit(self):
        pass

    def testGetDeck(self):
        '''test len of deck is 52'''
        self.assertEqual(len(Deck().get_deck()), 52)

    def testDeal(self):
        '''tests dealt card and that there are 51 cards left in deck after card dealt'''
        deck = Deck()
        self.assertEqual(str(deck.deal()), str(Card('K', 'd')))
        self.assertEqual(len(deck.get_deck()), 51)

    def testShuffle(self):
        '''tests that reshufflinf a deck gives different order'''
        deck = Deck()
        originalOrder = deck.get_deck()
        self.assertEqual(deck.get_deck(), originalOrder)
        deck.shuffle()
        shuffledDeck = deck.get_deck()
        self.assertNotEqual(shuffledDeck, originalOrder)

    def testStr(self):
        '''test that Str returns a multiline string of cards in the deck'''
        rankList = ['a', '2', '3', '4', '5', '6', '7', '8', '9',
                    '10', 'j', 'q', 'k']
        suitList = ['s', 'c', 'h', 'd']
        cardStrings = [r + s + "\n" for r in rankList for s in suitList]
        self.assertEqual(str(Deck()), ''.join(cardStrings))

unittest.main()
