
import cards
import players

class Table(object):
    """ Represents a table where the card game is being played """
    def __init__(self, capacity):
        self.deck = cards.Deck()
        self.deck.populate()
        self.capacity = capacity
        self.players = []

    def __str__(self):
        result = ""
        for player in self.players:
            result += player.__str__() + "\n"
        return result

    def sit(self, player):
        """ Represents a new player sitting at the table """
        self.players.append(player)

    def getup(self, player):
        """ Represents a current player getting up from the table """
        self.player.remove(player)

    def dealTable(self, num):
        """ Deal each of the players sitting at the table """
        hands = []
        for player in self.players:
            hands.append(player.hand)
        self.deck.shuffle()
        self.deck.deal(hands, num)

    def returnCards(self, cards):
        """ Represents a player returning cards from their hand to the table """
        for card in cards:
            self.deck.add(card)


class DealerTable(Table):
    """ Represents a table with a dealer that the players play against """
    def __init__(self, capacity):
        super(DealerTable, self).__init__(capacity)
        self.dealer = players.Player("Dealer")
        self.players.append(self.dealer)
