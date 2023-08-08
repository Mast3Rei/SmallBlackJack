#Bank class
#To inherit with the Player class
class Bank():
    
    def __init__(self,player,balance=0):
        self.chips_amount = int(balance)
    
    def bet(self):
        def bet_input():
            while True: #checks if the input is correct format
                try:
                    bet_in = int(input("Enter, how many chips do you want to bet? "))
                except:
                    print("Sorry, that is not an acceptable bet")
                    continue
                else:
                    return bet_in
            
            
        self.bet_amount = bet_input()
        
        acceptable = False 
        while not acceptable: #checks if the bet_amount is a valid amount
            
            if self.bet_amount == 0:
                print('Sorry, must bet more than 0')
                self.bet_amount = bet_input()
            elif self.chips_amount < self.bet_amount:
                print("Not enough funds!")
                self.bet_amount = bet_input()
            else:
                self.chips_amount -= self.bet_amount
                acceptable = True
                print(f"{self.name} just placed a bet of {self.bet_amount} chips and has {self.chips_amount} chips!")
                return self.bet_amount
        
        
    def cash_in(self,add_amt):
        self.chips_amount += add_amt
        print("{} chips have been added, and {} has {} chips total.".format(add_amt,self.name,self.chips_amount))
    
    def clear_chips(self):
        self.chips_amount = 0
    
    def __str__(self):
        raise NotImplementedError("Subclass must be implemented with Player Class")
    