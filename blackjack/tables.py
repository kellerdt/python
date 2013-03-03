import cards
import players

class Table(object):
    """ Represents a table where the card game is being played """
    def __init__(self, capacity, game):
        self.deck = cards.Deck()
        self.deck.populate()
        self.capacity = capacity
        self.game = game
        self.players = []

    def __str__(self):
        result = "Cards: " + str(len(self.deck.cards)) + "\n"
        for player in self.players:
            result += player.__str__() + "\n"
        return result

    def sit(self, player):
        """ Represents a new player sitting at the table """
        self.players.append(player)

    def getup(self, player):
        """ Represents a current player getting up from the table """
        self.returnCards(player)
        self.player.remove(player)

    def deal(self):
        """ Deal each of the players sitting at the table """
        hands = []
        for player in self.players:
            hands.append(player.hand)
        self.deck.shuffle()
        self.deck.deal(hands, self.game.handSize)

    def returnCards(self, player):
        """ Represents a player returning cards from their hand to the table """
        for i in range(player.hand.size() - 1, -1, -1):
            #Remove cards in reverse order since we are iterating and modifying
            card = player.hand.cards[i]
            player.hand.give(card, self.deck)

    def clear(self):
        """ Clears the table of any current state """
        for player in self.players:
            self.returnCards(player)


class DealerTable(Table):
    """ Represents a table with a dealer that the players play against """
    def __init__(self, capacity, game):
        super(DealerTable, self).__init__(capacity, game)
        self.dealer = players.Player("Dealer")
        self.players.append(self.dealer)
