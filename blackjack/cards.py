
# Represents a blackjack game

# Classes to represent the cards themselves
class Card(object):
	""" A Playing card """
	RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	SUITS = ['C','D','H','S']
	
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	
	def __str__(self):
		return self.rank + self.suit

class UnprintableCard(Card):
        """ A card whose value cannot be printed """
        def __str__(self):
                return ""

class FlipableCard(Card):
        """ A card which can be face up or face down """
        def __init__(self, rank, suit, faceup = True):
                super(FlipableCard, self).__init__(rank, suit)
                self.faceup = faceup

        def __str__(self):
                if self.faceup:
                        result = super(FlipableCard, self).__str__()
                else:
                        result = "XX"
                return result

        def flip(self):
                self.faceup = not self.faceup
                        

# Classes for groups of cards
class Hand(object):
	""" A hand of playing cards """
	def __init__(self):
		self.cards = []
	
	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "None"
		return rep
	
	def clear(self):
		self.cards = []
	
	def add(self, card):
		self.cards.append(card)
	
	def give(self, card, otherHand):
		self.cards.remove(card)
		otherHand.add(card)
	
	def remove(self, card):
		self.cards.remove(card)

class Deck(Hand):
        """ The full deck of cards used to play """
        def populate(self):
                for suit in Card.SUITS:
                        for rank in Card.RANKS:
                                self.add(Card(rank,suit))

        def shuffle(self):
                import random
                random.shuffle(self.cards)

        def deal(self, hands, perHand = 1):
                for rounds in range(perHand):
                        for hand in hands:
                                if self.cards:
                                        topCard = self.cards[0]
                                        self.give(topCard, hand)
                                else:
                                        print ("Out of cards")

#if __name__ == "__main__"
#        print ("This module is not meant to be run directly!")
#        input("\n\nPress any key to exit.")
