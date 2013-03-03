import tables, players, cards

class CardGame(object):
    """ Abstract object representing a card game """
    def setHandSize(self, num):
        self.handSize = num

class BlackJack(CardGame):
    """ Represents the rules to playing blackjack """
    def __init__(self):
        self.handSize = 2

    def getValue(self, hand):
        """ Returns the value of a hand using blackjack rules """
        points = 0
        containsAce = False
        for card in hand.cards:
            if card.rank in ("J", "Q", "K"):
                points += 10
            elif card.rank == "A":
                containsAce = True
                points += 1
            else:
                points += int(card.rank)
        if containsAce and points <= 11:
            points += 10 # already added 1 so just add 10 more
        return points

    def play(self, table):
        text1 = " you have "
        text2 = " points. Would you like to hit? (y/n) "
        table.deal()
        table.dealer.hand.cards[0].flip()
        print (table)

        # Run each player
        for player in table.players:
            if not player == table.dealer:
                answer = True
                while answer:
                    value = self.getValue(player.hand)
                    answer = player.askResponse(player.name + \
                                            text1 + str(value) + text2)
                    if answer:
                        table.deck.get(player.hand, 1)
                        print (player.hand)
                    if self.getValue(player.hand) > 21:
                        answer = False
                        print ("Bust!")

        # Run the dealer
        table.dealer.hand.cards[0].flip()
        print ("\nHidden dealer card:", table.dealer.hand.cards[0])
        value = self.getValue(table.dealer.hand)
        while value < 16:
            table.deck.get(table.dealer.hand, 1)
            value = self.getValue(table.dealer.hand)
            print ("Dealer has", value, "points")

        # Check who won
        print (table)
        if value == 21 and len(table.dealer.hand.cards) == 2:
            print ("Dealer blackjack, everyone loses")
        elif len(table.dealer.hand.cards) > 5:
            print ("Dealer got 6 cards, everyone loses")
        else:
            for player in table.players:
                if not player == table.dealer:
                    playerVal = self.getValue(player.hand)
                    if playerVal > 21:
                        print (player.name, "Busted")
                    elif playerVal == 21 and len(player.hand.cards) == 2:
                        print (player.name, "BlackJack!")
                    else:
                        if not value > 21:
                            if value > self.getValue(player.hand):
                                print (player.name, "lost")
                            elif value == self.getValue(player.hand):
                                print (player.name, "pushes")
                            else:
                                print (player.name, "won")
                        else:
                            print (player.name, "won")
        # Clean up the table
        table.clear()
