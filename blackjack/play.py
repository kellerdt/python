# Set up the imports
import sys
path = "C:\\code\\python\\blackjack"
if path not in sys.path:
    sys.path.append(path)

import games, tables, players

# Main
print ("\nFirst Blackjack Game!\n")
again = True
game = games.BlackJack()

table = tables.DealerTable(8, game)
player1 = players.Player("Dustin")
player2 = players.Player("Tim")
player3 = players.Player("Jeff")
player4 = players.Player("Justin")
table.sit(player1)
table.sit(player2)
table.sit(player3)
table.sit(player4)

while again:
    game.play(table)
    again = player1.askResponse("Continue to next round? (y/n) ")
