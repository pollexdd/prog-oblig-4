
import random
dealer_cards = []
player_cards = []



class Chips:   # keep track of chips

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    def skrivut():
        print(F'you have {Chips.total} chips')

def take_bet(chips):  # ask for user's bet

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry! Please can you type in a number: ")
        else:
            if chips.bet > chips.total:
                print("You bet can't exceed 100!")
            else:
                break


def Blackjack():
    player_chips = Chips()
    


    take_bet(player_chips)
    dealer_cards.append(random.randint(1, 11))
    dealer_cards.append(random.randint(1, 11))
    print("Dealer has X &", dealer_cards[1])
        

    player_cards.append(random.randint(1, 11))
    player_cards.append(random.randint(1, 11))
    print("You have ", player_cards)   

    if sum(dealer_cards) == 21:
        print("Dealer has 21 and wins!")
        Chips.lose_bet
    elif sum(dealer_cards) > 21:
        print("Dealer has busted!")
        Chips.win_bet
        
        
   


    while sum(player_cards) < 21:
        action_taken = str(input("Do you want to stay or hit?  "))
                
        if action_taken == "hit":
            player_cards.append(random.randint(1, 11))
            if sum(player_cards) > 21 and player_cards[-1] == 11:
                print("you got an ace which will be 1 insted of 11")
                player_cards.pop(-1)
                player_cards.append(1)
            print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
            if sum(player_cards) == 21:
                    print("you have blackajck")
            
                    break
            elif sum(player_cards) > 21:
                    print("you busted")
                    Chips.lose_bet
                    break
        if action_taken == "stay":
            while sum(dealer_cards) < 18:
                dealer_cards.append(random.randint(1, 11))
                    
                        
                if sum(dealer_cards) > 21 and player_cards[-1] == 11:
                    print("The dealer got an ace which will be 1 insted of 11")
                    player_cards.pop(-1)
                    player_cards.append(1)
                    print(sum(dealer_cards))
            print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
                
                

            if  sum(player_cards) == sum(dealer_cards):
                print("its a tie you win no chips")
                break
            elif sum(dealer_cards) > 21:
                    print("dealer busted you win!")
                    Chips.win_bet
                    break

            elif sum(dealer_cards) > sum(player_cards):
                print("Dealer wins!")
                Chips.lose_bet
                break

            else:
                print("You win!")
                Chips.win_bet
                break


x = True
while x is True:
    # stake = input("you have "+ str(chips) + " chips how many chips do you want to bet? ")
    Chips.skrivut()
    player_cards.clear()
    dealer_cards.clear()
    Blackjack()









