
import tables, players, cards

class BlackJack(object):
    """ Represents the rules to playing blackjack """

    def getValue(hand):
        """ Returns the value of a hand using blackjack rules """
        points = 0
        for card in hand.cards:
            if card.rank in ("J", "Q", "K"):
                points += 10
            elif card.rank == "A":
                if points > 10:
                    points += 1
                else:
                    points += 11
            else:
                points += int(card.rank)
        return points

