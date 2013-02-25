# main
print ("My first attempt at a card game")
again = True

table = tables.DealerTable(8)
player1 = players.Player("Dustin")
player2 = players.Player("Tim")
player3 = players.Player("Jeff")
player4 = players.Player("Justin")
table.sit(player1)
table.sit(player2)
table.sit(player3)
table.sit(player4)

while again:
    table.dealTable(2)
    print (table)
    again = player1.askResponse("\nContinue to next round? (y/n)")
