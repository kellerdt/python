import cards

class Player(object):
    """ A player for a game """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
        self.hand = cards.Hand()

    def __str__(self):
        return self.name + "(" + str(self.score) + ")" + self.hand.__str__()

    def askResponse(self, question):
        """ Ask the player to respond yes or no """
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response == "y"

    def askNumber(self, question, low, high):
        """ Ask the player to give a number in a valid range """
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

# main check
#if __name__ == "__main__"
#    print ("Please don't run this module directly")
#    input("\n\nPress any key to exit.")
