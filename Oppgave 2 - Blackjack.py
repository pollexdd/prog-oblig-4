
import random
dealer_cards = []
player_cards = []

   
def Blackjack():
    # Klarte ikke å få til chips betting
    Chips = int(10)
    bet = int(input("you have "+ str(Chips) + " chips how many chips do you want to bet? "))

    # dealer får 2 kort
    dealer_cards.append(random.randint(1, 11))
    dealer_cards.append(random.randint(1, 11))
    print("Dealer has X &", dealer_cards[1])
        
    # spiller får 2 kort
    player_cards.append(random.randint(1, 11))
    player_cards.append(random.randint(1, 11))
    print("You have ", player_cards)   

    if sum(dealer_cards) == 21:
        print("Dealer has 21 and wins!")
        Chips -= bet
    elif sum(dealer_cards) > 21:
        print("Dealer has busted!")
        Chips += bet
        
         
   

    # While loop helt til spilleren velger stay
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
                    Chips -= bet
                    break
        # Hvis man velger stay tar dealeren kort helt til han er under 18
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
                    Chips += bet
                    break

            elif sum(dealer_cards) > sum(player_cards):
                print("Dealer wins!")
                Chips -= bet
                break

            else:
                print("You win!")
                Chips += bet
                break


x = True
while x is True:
    # sletter alt i listene
    player_cards.clear()
    dealer_cards.clear()
    # kjører blackjack spillet
    Blackjack()









