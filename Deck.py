import random



#DECK class. Create 52 cards
class Deck():
    

    def __init__(self):
        from Card import Card
        from BlackJackGame import suits,ranks,values
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.new_card = Card(suit,rank)
                self.all_cards.append(self.new_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop(0)