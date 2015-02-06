#Francesco Melpignano

from SoloBlackjack import *
import unittest
from cards import *
import random

class TestSoloBlackjack(unittest.TestCase):
    '''tests for solo blackjack game'''

    def setUp(self):
        '''setup that contains the game, the card, and example hands used
        in other test'''
        random.seed(12)
        self.game = SoloBlackjack()
        self.seededDeal = []
        for i in range(52):
            self.game.deal()
            self.seededDeal.append(str(self.game.getDealtCard()))
        random.seed(12)
        testCardValues = [['a', 'k'], ['k', 'k'], ['a', 'k', 'k'],
                          ['a', 'a', 'k'], ['9', '9', '5'], ['a', '5', 'a'],
                          ['a', 'a', 'a', 'a']]
        self.hands = [[Card(r, 'h') for r in hand] for hand in testCardValues]
        self.game = SoloBlackjack()
        
    def testInit(self):
        '''makes sure init does not raise any errors'''
        game = SoloBlackjack()

    def testScoreHand(self):
        '''checks if the function scoreHand correctly scores the hands
        in testCardValue list of lists'''
        expectedScores = [10, 5, 7, 1, 0, 2, 1]
        for hand, value in zip(self.hands, expectedScores):
            self.assertEqual(self.game.scoreHand(hand), value)

    def testScoreIncompleteHand(self):
        '''raises attribute error if hand is incomplete'''
        incompleteHand = self.hands[0] + [3]
        self.assertRaises(AttributeError, self.game.scoreHand, incompleteHand)

    def testDeal(self):
        '''checks if dealt card is the same when first dealt
        and also if it is different when deal() is called again'''
        self.game.deal()
        dealtCard = self.game.getDealtCard()
        self.assertEqual(dealtCard, self.game.getDealtCard())
        self.assertEqual(str(dealtCard), self.seededDeal[0])
        self.game.deal()
        dealtCardTwo = self.game.getDealtCard()
        self.assertNotEqual(dealtCard, dealtCardTwo)

    def testDealWholeDeck(self):
        '''raises index error when all all cards all dealt from deck'''
        for card in self.seededDeal:
            self.game.deal()
        self.assertRaises(IndexError, self.game.deal)

    def testGetDealtCard(self):
        '''returns none before any cards are dealt'''
        self.assertEqual(None, self.game.getDealtCard())
        
    def testSeededDeal(self):
        '''tests if dealt card of a seeded randomized deal is the same as
        the seeded random deal created in setUp'''
        lastCard = None
        for i in range(10):
            random.seed(12)
            game = SoloBlackjack()
            game.deal()
            if lastCard is None:
                lastCard = game.getDealtCard()
            self.assertEqual(str(lastCard), str(game.getDealtCard()))

    def testGetTableRows(self):
        '''tests if getTableRows recreates game's rows'''
        expectedList = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                        [11, 12, 13], [14, 15, 16]]
        self.assertEqual(expectedList, self.game.getTableRows())

    def testGetTableCoulmns(self):
        '''tests is getTableColums recreates game's columns'''
        expectedList = [[1, 6], [2, 7, 11, 14], [3, 8, 12, 15], [4, 9, 13, 16], 
                        [5, 10]]
        self.assertEqual(expectedList, self.game.getTableColumns())

    def testMakeMove(self):
        '''checks if placed card is placed in selected position'''
        self.game.deal()
        self.game.makeMove(12)
        expectedValue = str(self.seededDeal[0])
        gotValue = self.game.getTableRows()[2][1]
        self.assertEqual(str(gotValue), expectedValue)

    def testDuplicateInMakeMove(self):
        '''raises RuntimeError if there is already a card in the position'''
        self.game.deal()
        self.game.makeMove(3)
        self.assertRaises(RuntimeError, self.game.makeMove, 3)

    def testOutOfRangePositionInMakeMove(self):
        '''raises RuntimeError if position is out of range'''
        self.game.deal()
        self.assertRaises(RuntimeError, self.game.makeMove, 0)
        self.assertRaises(RuntimeError, self.game.makeMove, 21)

    def testScoreTable(self):
        '''recreates a table then scores it to see if is equal to scoreTable'''
        rows = [[], [], [], []]
        columns = [[], [], [], [], []]
        indexDict = {1:(0, 0), 2:(1, 0), 3:(2, 0), 4:(3, 0), 5:(4, 0),
                     6:(0,1), 7:(1, 1), 8:(2, 1), 9:(3, 1), 10:(4, 1),
                     11:(1, 2), 12:(2, 2), 13:(3, 2),
                     14:(1, 3), 15:(2, 3), 16:(3, 3)}
        for position in range(1, 17):
            self.game.deal()
            card = self.game.getDealtCard()
            column, row = indexDict[position]
            columns[column].append(card)
            rows[row].append(card)
            self.game.makeMove(position)
        rowScore = sum([self.game.scoreHand(row) for row in rows])
        columnScore = sum([self.game.scoreHand(column) for column in columns])
        self.assertEqual(rowScore + columnScore, self.game.scoreTable())

    def testIsGameComplete(self):
        '''tests if an incomplete game passed in isGameComplete returns false
        and a complete game passed through isGameComplete returns true'''
        for position in range(1, 17):
            self.game.deal()
            self.assertFalse(self.game.isGameComplete())
            self.game.makeMove(position)
        self.assertTrue(self.game.isGameComplete())
        
unittest.main()
