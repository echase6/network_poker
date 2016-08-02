# network_poker
Poker application that enables two users to play 5-card stud
via a network connection.  Tracks bets and winnings.  Also implements a GUI
to display cards and chips.

Collaborative project between Stephen Muller and Eric Chase.


Major components:
- Deck management
  - shuffle
  - dealing cards
- Stash and Pot management
   - tracking amounts per player
   - tracking bets per player
- Network implementation
   - client
   - server
- GUI
   - cards
   - chips
   - table
- Game loop
   - hand-off between dealing cards and placing bets
   - decision tree, asking for player decision based on other player's move
   - find the winning hand

   Example of GUI window, displayed on client:
   ![GUI window](https://github.com/echase6/network_poker/blob/master/images/GUI_example.jpg)
