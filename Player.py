from Bank import Bank


#Player class. Inherits Bank class
class Player(Bank):
    
    def __init__(self,name,balance=0):
        super().__init__(self,balance)
        self.name = name
        self.cards = []
        
        
    def hit(self,add_card):
        self.cards.append(add_card)
        print(f"\n{self.name}'s card -> {add_card}\n")
    def stay(self):
        return True
    
    
    def clear_hand(self,deck):
        while self.cards!=[]:
            deck.all_cards.append(self.cards.pop(0))
            
                    
        
    def face_up(self,card_index=-1): # this method uncovers the card and reveals it to the player. 
                                    #Pass in the index of the card you want to cover
        current_card = self.cards[card_index]
        if current_card.covered:
            current_card.covered = False
            print(f"\n{self.name}'s covered card is -> {current_card} \n")
        else:
            print(f"\n{self.name}'s card -> {current_card}\n")
        
    def face_down(self,card_index=-1): #this method covers the card and conceals it from the player
                                    #Pass in the index of the card you want to uncover
        self.cards[card_index].covered = True
        print(f"\n{self.name}'s card ~ This card is covered ~\n")
        
    def __str__(self):
        return f'{self.name} now has {self.chips_amount} chips\n'