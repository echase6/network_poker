# network_poker
Poker application that enables two users to play 5-card stud
via a network connection.  Tracks bets and winnings.  Also implements a GUI
to display cards and chips.

Collaborative project between Stephen Muller and Eric Chase.


Major components:
-- Deck management
   -- shuffle
   -- dealing cards
-- Bank management
   -- tracking amounts per player
   -- tracking bets per player
-- Network implementation
   -- client
   -- server
-- GUI
   -- cards
   -- chips
   -- table
-- Computer player
   -- codify intelligent card-play
   -- codify intelligent betting

 Workflow:
-- define data structures
    -- card
    -- hand
    -- player
    -- stash
    -- table
-- implement deck management
-- implement rudimentary GUI
-- implement stash management
-- implement game logic (one hand)
-- write master loop
-- (for Network)
   -- define data structure necessary to pass between
