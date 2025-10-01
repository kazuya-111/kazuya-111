#
# File: nakky007@mymail.unisa.edu.au_aceydeucey
# Author:Kazuya Nakayama
# SAIBT ID:50587
# Version: 1.0 current date 30.11.2024
# Description: Assignment 1- \ldots.
# This is my own work as definded by SAIBT's
# Academic Misconduct policy.


##card_game aceydeucey

import random

print("- - -  ACEY DEUCEY - - -")
instruction="y"
instruction=input("Instruction? (y/n)")
while instruction !="y" and instruction !="n":
    print("Please enter  'y' or 'n'")
    instruction=input("Instruction? (y/n)")
if instruction=="y":
    print("Acey Deucey is a simple card game")
    print("Two cards are drawn and the player places a bet on")
    print("whether the next card drawn will fall between the two cards.")
    print("")
    print("You play against the computer, starting with $50.")
    print("Each round costs an ante of $1, which is doubled every")
    print("five rounds.")
    print("")
    print("If you wish to pass, enter a bet of $0.")
    print("However, you must still pay the ante.")
    print("")
    print("Have fun!")
    print("")

card1=0
card2=0
card3=0
random.randint(1,13)
player_money=50
computer_money=50
Pot=10
Adds=1
print("Player: $",player_money,"Computer: $",computer_money)
print("Ante is: $",Adds,    "Pot: $" ,Pot)
print("")

play_again="y"
player_bet=0
game_round=0

##player put "n" needs to display game summary
play_again=input("Do you wish to play a round? (y/n)")
while play_again !="y" and play_again !="n":
    print("Please enter 'y' or 'n'")
    play_again=input("Do you wish to play a round? (y/n)")
    
#if play_again=="y" and player_money >0
while play_again=="y" and player_money > 0:
    player_money=player_money-Adds
    computer_money=computer_money-Adds
    Pot=Pot+Adds*2
    print("[PLAYER]  Adds", Adds," to the pot.")

    if computer_money > 0:
        print("[COMPUTER] Adds",Adds," to the pot.")
        print("Player:",player_money, "Computer: $", computer_money)
        print("Pot:",Pot)
    else:
        print("Player:",player_money)
        print("Pot:",Pot)
        
    #Player turn
    press=input("PRESS <ENTER> to continue")
    if press=="":
        print("[PLAYER]", "","", "Cards are:")
    
    card1=random.randint(1,13)
    card3=random.randint(1,13)

    #Check card value whether same
    while card1==card3:
        card3=random.randint(1,13)
    #=Replace card1 and card3
    if card1>card3:
        card1,card3=card3,card1


    #Generate three card
    #7s=return str, 7d=decimal
    print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
    print("|", format(card1,"<7d"), "| "," |", format("?","<7s"), "| ", " |", format(card3,"<7d"), "|", sep="")

    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
 
    print("|",format(card1,"_>7d"),"|  |",format("?", "_>7s"),"|  |", format(card3,"_>7d"), "|", sep="")
    print("")

    #Max bet=minimun number player_money or Pot
    if player_money<Pot:
        max_bet=player_money
    elif Pot<player_money:
        max_bet=Pot

    #f=display {max_bet} and prompt bet
    player_bet=int(input(f"Enter bet (max ${max_bet}): $"))
    while player_bet >max_bet:
        print("You cannot bet more than the pot or player_money amount!($",max_bet,")")
        player_bet=int(input(f"Enter bet (max ${max_bet}) : $"))

    #when player pass do not draw third card
    if player_bet==0:
        print("[PLAYER] PASS!")
        
    elif player_bet>0:
        card2=random.randint(1,13)
             
        #Generate card as a result
        print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
       
        print("|", format(card1,"<7d"),"| ", " |", format(card2,"<7d"),"| ", " |",format(card3,"<7d"),"|", sep="")

        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        
        print("|",format(card1,"_>7d"),"|  |",format(card2,"_>7d"),"|  |",format(card3,"_>7d"),"|", sep="")
        print("")

        #implement rule win or lose
        if card1<card2<card3:
            print("[PLAYER] You win $",player_bet)
            player_money=player_money+player_bet
            Pot=Pot-player_bet
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)
        elif card2<card1<card3 or card1<card3<card2:
            print("[PLAYER] You lose $", player_bet)
            player_money=player_money-player_bet
            Pot=Pot+player_bet
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)
        elif card2==card1 or card2==card3:
            print("[PLAYER]"   , "HIT THE POST!!!")
            print("[PLAYER]"   , "You lose",player_bet*2)
            player_money=player_money-player_bet*2
            Pot=Pot+player_bet*2
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)
            print("")

        #Player_money <=0 can not play continue display broke
        if player_money <= 0:
            print("Player is broke")
            
    # Computer turn - Ensure the player has not gone broke and make sure computer has enough money
    if computer_money > 0 and player_money > 0:
            
        input("PRESS <ENTER> to continue")
        
        print("[COMPUTER]", "","", "Cards are:")
        
        card1=random.randint(1,13)
        card3=random.randint(1,13)

        #Check card value whether same
        while card1==card3:
            card3=random.randint(1,13)
        #Replace value
        if card1>card3:
            card1,card3=card3,card1

        #Generate  cards
        #7s=return str, 7d=decimal
        print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
        
        print("|", format(card1,"<7d"),"| ", " |", format("?","<7s"),"| ", " |",format(card3,"<7d"),"|", sep="")

        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        
        print("|",format(card1,"_>7d"),"|  |",format("?","_>7s"),"|  |",format(card3,"_>7d"),"|", sep="")
        print("")


        ##computer maxbet minimum number pot or money
        if computer_money<Pot:
            max_bet=computer_money
        elif Pot<computer_money:
            max_bet=Pot

        computer_bet=random.randint(0,max_bet)
        
        input("PRESS <ENTER> to continue")

        #Display max_bet and computer_bet str()
        print("Enter bet (max $" + str(max_bet) + ") : $" + str(computer_bet))

        ##when computer pass do not draw third card
        if computer_bet==0:
            print("[COMPUTER] PASS!")
        else:
            card2=random.randint(1,13)
                 
            ##Generate card as a result
            print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
            
            print("|", format(card1,"<7d"),"| ", " |", format(card2,"<7d"),"| ", " |",format(card3,"<7d"),"|", sep="")

            print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
            print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
            print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
            print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
            
            print("|",format(card1,"_>7d"),"|  |",format(card2,"_>7d"),"|  |",format(card3,"_>7d"),"|", sep="")
            print("")

            ##Implement win or lose
            if card1<card2<card3:
                print("[COMPUTER] You win $",computer_bet)
                computer_money=computer_money+computer_bet
                Pot=Pot-computer_bet
                print("")
                print("Computer: $ ",computer_money,"Pot: $:",Pot)
            elif card2<card1<card3 or card1<card3<card2:
                print("[COMPUTER] You lose $",computer_bet)
                computer_money=computer_money-computer_bet
                Pot=Pot+computer_bet
                print("")
                print("Computer: $ ",computer_money,"Pot: $:",Pot)
            elif card2==card1 or card2==card3:
                print("[COMPUTER]"   , "HIT THE POST!!!")
                print("[COMPUTER]"   , "You lose",computer_bet*2)
                computer_money=computer_money-computer_bet*2
                Pot=Pot+computer_bet*2
                print("")
                print("Computer: $ ",computer_money,"Pot: $:",Pot)
                print("")    

    #game round add and each 5games add*2
    game_round+=1
    if game_round %5==0:
        Adds=Adds*2
        print("Ante increase! It is now $", Adds)
        print("Player:    $",player_money)
        print("Ante is:  $",Adds, "Pot: $", Pot)

    input("PRESS <ENTER> to continue")
    print("")

    print("Player: $",player_money, "Computer:",computer_money)
    print("Ante is: $", Adds, "Pot:$",Pot)
        
    if computer_money<=0:
        print("Computer is broke!($",computer_money,")")
            
    if player_money > 0:    
        play_again=input("Do you wish to play a round ?(y / n ):")
        while play_again !="y" and play_again !="n":
            print("Please enter 'y' or 'n'")
            play_again=input("Do you wish to play a round? (y/n)")

        
if game_round > 0:
    print("--- GAME SUMMARY ---")
    print("Player: $",player_money, "Computer: $",computer_money)
    print("Ante:  $", Adds, "Pot : ", Pot)
    print("You played",game_round,"rounds.")
else:
    print("--- GAME SUMMARY ---")
    print("Player: $",player_money, "Computer: $",computer_money)
    print("Ante:  $", Adds, "Pot : ", Pot)
    print("You played",game_round,"rounds.")






