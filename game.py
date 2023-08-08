from Card import Card
from Deck import Deck
from Bank import Bank
from Player import Player
import random

suits = ['Hearts','Spades','Clubs','Diamonds']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,
        'King':10,'Ace':11}
def SmallBlackJack():

    # Reset everything in the game: clear the cards, distribute the chips,
    def reset_match():
        for player in [dealer,player1]:
            player.clear_hand(new_deck)

            
    # User can choose to keep playing. This should trigger the game_on or new_match loops
    def keep_playing_choice():
        while True:
            try:
                new_match_choice = str(input("Would you like to keep playing? Y or N: "))[0].upper()
            except:
                print("That is not an acceptable answer")
                continue
            else:
                while new_match_choice not in ['Y','N']: #Error checking
                    print("Sorry, that is not an acceptable choice!")
                    new_match_choice = str(input("Would you like to keep playing? Y or N: "))[0].upper()
                    
                if new_match_choice=='Y':
                    return True
                else:
                    return False

    def check_game_on():
        #When game ends on chips
        if player1.chips_amount==0:
            #Game off, player loses
            print(f"\n{player1.name} has run out of chips and lost the game!\n")
            print("\nThanks for playing!")
            new_match=False
            game_on=False
            
        elif dealer.chips_amount<=0: #if dealer goes below zero 
            #Game off, player wins
            print(f"\n{player1.name} has defeated the dealer and wins the game!\n")
            print("\nThanks for playing!")
            new_match=False
            game_on=False
            
        else:
            pass

    #=============================================================================================================

    #GAME LOGIC




    dealer = Player('Dealer',balance=100) #insert how many chips dealer starts with
    player1 = Player(input("Enter your username: "),balance=10) #insert how many chips player starts with
    new_deck = Deck()

    game_on = True
    new_match = False



    print("\nWelcome to this game of BlackJack! The goal is to get your cards to total up to 21 in order to beat the dealer. ")
    print("Each round you have the option to 'hit' and gain a new card, or 'stay' and stop drawing cards.")
    print("The ultimate goal of this game is to win all the chips from the dealer. Note: Aces are equal to 11\n")
    print(player1)
    print(dealer)


    while game_on:

        #Shuffle the deck at beginning of each round
        new_deck.shuffle()


        # Game starts and player places a bet of at least 1 chip
        bet_amount = player1.bet()
        reward = 0 #reward for later
        return_chips = bet_amount

        # Once bet is placed, 1 card dealt to player face up, 1 card to dealer face up, 1 card to player face up,
        # 1 card to dealer face down
        
        
        player1.cards.append(new_deck.deal_one()) #deal 1 to player face up
        player1.face_up() #face_up method reveals the card
        dealer.cards.append(new_deck.deal_one())  #deal one to dealer face up
        dealer.face_up()
        player1.cards.append(new_deck.deal_one()) #deal 1 to player face up
        player1.face_up()
        dealer.cards.append(new_deck.deal_one()) #deal 1 to dealer face down
        dealer.face_down() #face_down method covers the card
        
        

        # Player can choose to 'hit' until he says 'stay', using a while loop
        
        #------------PLAYER-------------
        player1_values = sum(list(map(lambda card: card.value, player1.cards))) # this line takes the values of each object and puts them in a 
                                                            #list, then returns the sum of that list
        stay = False
        while not stay:
            
            hit_choice = input("Enter, would you like to hit? Y or N: ")[0].upper() #Player hit
            
            while hit_choice not in ['Y','N']: #Error checking
                print("Sorry, that is not an acceptable choice!")
                hit_choice = input("Enter, would you like to hit? Y or N: ")[0].upper()
            
            if hit_choice=='Y':
                player1.hit(new_deck.deal_one())
                player1_values += player1.cards[-1].value
            else:
                print(f"\n{player1.name} stays!\n") #Player stay
                stay = player1.stay()
                
            if player1_values > 21: #Player bust!
                print(f"{player1.name} busts! {dealer.name} collects the reward.\n")
                reward = bet_amount
                dealer.chips_amount += reward
                print(player1) #prints how many chips player1 has
                print(dealer) #prints how many chips dealer has
                break
                
        bust_amount = 21
        if player1_values > bust_amount:       
            #Check if game ends on chips
            if player1.chips_amount==0:
                #Game off, player loses
                print(f"\n{player1.name} has run out of chips and lost the game!\n")
                print("\nThanks for playing!")
                new_match=False
                game_on=False
                break

            elif dealer.chips_amount<=0: #if dealer goes below zero 
                #Game off, player wins
                print(f"\n{player1.name} has defeated the dealer and wins the game!\n")
                print("\nThanks for playing!")
                new_match=False
                game_on=False
                break
            else:
                pass


                #Keep playing?
                new_match = keep_playing_choice()
                if new_match==True: 
                    reset_match()
                    new_match = False
                    input('\n...Press enter to continue...\n')
                    print('\n'*50)
                    continue
                else:
                    print('\nGame is finished!\n')
                    print("\nThanks for playing!")
                    break
        

        
        #------------DEALER-------------
        # Dealer reveals covered card
        
        dealer.face_up()
        
        dealer_values = sum(list(map(lambda card: card.value, dealer.cards))) # this line takes the values of each object and puts them in a 
                                                            #list, then returns the sum of that list
        # If dealer's cards add to 16 or less, then must grab a third card and then stay
        if dealer_values <= 16:
            dealer.hit(new_deck.deal_one())
            dealer_values += dealer.cards[-1].value
            if dealer_values <= 21:
                print("\nDealer stays!\n")
            else:
                pass
        # If dealer's cards add up to 17 or more immediately, they must stay.
        elif dealer_values >= 17 and dealer_values <= 21:
            print("\nDealer stays!\n")
        if dealer_values > 21:  # Dealer busts
            print("\nDealer busts!\n")  
            
            #take away from dealer the bet amount of the player, then add the amount to player chips_amount
            reward = bet_amount
            dealer.chips_amount -= reward
            player1.chips_amount += return_chips + reward #return the bet amount and reward
            print(player1) #prints how many chips player1 has
            print(dealer)  #prints how many chips dealer has
            
            #After dealer busts:
            #Check if game ends on chips
            if player1.chips_amount==0:
                #Game off, player loses
                print(f"\n{player1.name} has run out of chips and lost the game!\n")
                print("\nThanks for playing!")
                new_match=False
                game_on=False
                break

            elif dealer.chips_amount<=0: #if dealer goes below zero 
                #Game off, player wins
                print(f"\n{player1.name} has defeated the dealer and wins the game!\n")
                print("\nThanks for playing!")
                new_match=False
                game_on=False
                break
            else:
                pass
            
            
            #Keep playing?
            new_match = keep_playing_choice()
            if new_match==True: 
                reset_match()
                new_match = False
                input('\n...Press enter to continue...\n')
                print('\n'*50)
                continue
            else:
                print('\nGame is finished!\n')
                print("\nThanks for playing!")
                break

        

        
        
        #WAYS THE MATCH ENDS:
        #After player and dealer stay
        if player1_values==21 and dealer_values==21: #tie, stand off; finish match
            print(f"{player1.name} and {dealer.name} have a tie for Blackjack! This is a stand off, and {player1.name} and {dealer.name} gain no reward. \n")
            player1.chips_amount += return_chips
            print(player1) #prints how many chips player1 has
            print(dealer)
            
            
        elif player1_values==21: #win; finish match
            print(f"{player1.name} has a blackjack! They receive 1.5x of their bet as a reward.\n")
            reward = bet_amount*1.5
            dealer.chips_amount -= reward
            player1.chips_amount = return_chips + reward
            print(player1)
            print(dealer)
            
            
        elif dealer_values==21: #dealer wins; finish match
            print(f"{dealer.name} has a blackjack! The player pays the dealer their bet amount.\n")
            reward = bet_amount
            dealer.chips_amount += reward
            print(player1)
            print(dealer)

        
        elif player1_values%21 > dealer_values%21: #if player is closer to 21 than dealer, player earns 2x betting amount from dealer
            print(f"{player1.name} is closer to 21! The player gets 2x their bet as a reward.\n")
            reward = bet_amount*2
            dealer.chips_amount -= reward
            player1.chips_amount += return_chips + reward
            print(player1)
            print(dealer)
            
            
        elif player1_values%21 < dealer_values%21: #if dealer is closer to 21 than player, dealer earns the bet from player
            print(f"{dealer.name} is closer to 21! The player pays the dealer their bet amount.\n")
            reward = bet_amount
            dealer.chips_amount += reward
            print(player1)
            print(dealer)
        
        
        elif player1_values == dealer_values: #if player and dealer have a tie
            print(f"{player1.name} and {dealer.name} have a tie! This is below the total of 21, so player pays the dealer their bet.\n")
            reward = bet_amount
            dealer.chips_amount += reward
            print(player1)
            print(dealer)
            
            
            
        
        
        #When game ends on chips
        if player1.chips_amount==0:
            #Game off, player loses
            print(f"\n{player1.name} has run out of chips and lost the game!\n")
            print("\nThanks for playing!")
            new_match=False
            game_on=False
            
        elif dealer.chips_amount<=0: #if dealer goes below zero 
            #Game off, player wins
            print(f"\n{player1.name} has defeated the dealer and wins the game!\n")
            print("\nThanks for playing!")
            new_match=False
            game_on=False
            
        else:
            #Keep playing?
            new_match = keep_playing_choice()
            if new_match==True: 
                reset_match()
                new_match = False
                input('\n...Press enter to continue...\n')
                print('\n'*50)
                continue
            else:
                print('\nGame is finished!')
                print('\nThanks for playing!')
                break
        

if __name__=="__main__":
    SmallBlackJack()
else:
    print("This is a Main File!")     
    

