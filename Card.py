


# CARD class
# suit of card, rank of card, and values of card
# print out the card with both its suit and rank
# for every suit each rank will be matched up, creating a total of 52 cards

class Card():
    
    def __init__(self,suit,rank):
        from BlackJackGame import suits,ranks,values
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.covered = False
        
    def __str__(self):
        return self.rank+' of '+self.suit