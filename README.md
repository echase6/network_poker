# network_poker
Poker application that enables two users to play 5-card stud
via a network connection.  Tracks bets and winnings.  Also implements a GUI
to display cards and chips.

Collaborative project between Stephen Muller and Eric Chase.

Instructions to run:
- On server machine:  
    C:\> python main.py
  - Note address of server (127.0.0.1 as default)
- On first client machine:  
    C:\> python client.py
  - Enter address of server
  - Enter port number (8000)
- On second client machine:  
    C:\> python client.py
  - Enter address of server
  - Enter port number (8001)
- Each player gets a GUI representing the table
- Each player responds to command-line prompts
- Game is over when either:
  - One player runs out of chips
  - Either player responds (after a hand) that they do not want to continue

Major components of the programs:
- Deck management
  - shuffle
  - dealing cards
- Stash and Pot management
   - tracking amounts per player
   - tracking bets per player
- Network implementation (uses python socket, in stream mode)
   - client
   - server
   - information protocol (uses JSONpickle for table information)
- GUI (uses PIL and Tkinter)
   - cards
   - chips
   - table
- Game loop
   - hand-off between dealing cards and placing bets
   - decision tree, asking for player decision based on other player's move
   - find the winning hand

   Example of GUI window, displayed on client:
   ![GUI window](https://github.com/echase6/network_poker/blob/master/images/GUI_example.jpg)
