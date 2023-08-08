This is a single-player game of BlackJack. The dealer automatically plays against the player. 

The game logic requires:
- Card class: creates a card with suit, rank, and value
- Deck class: creates the cards and puts them in a list called 'all_cards', which is the deck. Includes a shuffle 
                 method and a deal one card method
- Bank class: manages the chips of the player and the dealer. Includes bet, cash_in, and clear_chips methods. 
                The Player class inherits the Bank class
- Player class: creates the player and the dealer. Includes hit, stay, clear_hand, face_up, and face_down methods. 
                Player class inherits the Bank class
