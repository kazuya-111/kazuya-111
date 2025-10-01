#
# File: nakky007@mymail.unisa.edu.au_Bonus Work
# Author:Kazuya Nakayama
# SAIBT ID:50587
# Version: 1.0 current date 30/11/2024
# Description: Assignment 1- \ldots.
# This is my own work as definded by SAIBT's
# Academic Misconduct policy.

#card_game
#add rule when cpu bet complete list
#add game rule
#change 1=A, 11=J, 12=Q, 13=K but it can replace the card1 and card3
#all card count 52 and shufflu not
#count number of all card not

import random

A="A"<"2"<"3"<"4"<"5"<"6"<"7"<"8"<"9"<"10"<"J"<"Q"<"K"
J="A"<"2"<"3"<"4"<"5"<"6"<"7"<"8"<"9"<"10"<"J"<"Q"<"K"
Q="A"<"2"<"3"<"4"<"5"<"6"<"7"<"8"<"9"<"10"<"J"<"Q"<"K"
K="A"<"2"<"3"<"4"<"5"<"6"<"7"<"8"<"9"<"10"<"J"<"Q"<"K"

card_rist1=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card1_replace_list=["A","2","3","4","5","6"]
card3_replace_list=["7","8","9","10","J","Q","K"]
#card_value="A"<"2"<"3"<"4"<"5"<"6"<"7"<"8"<"9"<"10"<"J"<"Q"<"K"


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
computer_bet=0
game_round=0

play_again=input("Do you wish to play a round? (y/n)")
while play_again !="y" and play_again !="n":
    print("Please enter 'y' or 'n'")
    play_again=input("Do you wish to play a round? (y/n)")

if play_again=="n":
        print("--- GAME SUMMARY ---")
        print("Player: $",player_money, "Computer: $",computer_money)
        print("Ante:  $", Adds, "Pot : ", Pot)
        print("You played",game_round,"rounds.")
    

while play_again=="y" and player_money > 0:
    if play_again=="y":
        player_money=player_money-Adds
        computer_money=computer_money-Adds
        Pot=Pot+Adds*2
        print("[PLAYER]  Adds", Adds," to the pot.",)

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

    #Draw the crad from card_list
    for card1 in card1_replace_list:
        card1=random.choice(card1_replace_list)
    
    for card3 in card3_replace_list:
        card3=random.choice(card3_replace_list)

    #Check crad value whether same
    #while card1==card3:
        #card3=random.choice(card_rank)
    #Replace card1 and card3
    #card1_repalece_list=["A","2","3","4","5","6"]
    #card3_replace_list=["7","8","9","10","11",J","Q","K"]
    #if card1>card3:
        #card1,card3=card3,card1


    #Generate three card 
    print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
    print("|", format(card1,"<7s"), "| "," |", format("?","<7s"), "| ", " |", format(card3,"<7s"), "|", sep="")

    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
 
    print("|",format(card1,"_>7s"),"|  |",format("?", "_>7s"),"|  |", format(card3,"_>7s"), "|", sep="")
    print("")

    #Max_bet=minimum number player_money or Pot
    if player_money<Pot:
        max_bet=player_money
    elif Pot<player_money:
        max_bet=Pot

    #f=display {max_bet}
    player_bet=int(input(f"Enter bet (max ${max_bet}): $"))
    while player_bet >max_bet:
        print("You cannot bet more than the pot or player_money amount!($",max_bet,")")
        player_bet=int(input(f"Enter bet (max ${max_bet}) : $"))

    ##when player pass
    if player_bet==0:
        print("[PLAYER] PASS!")

    elif player_bet>0:
        card2=random.choice(card_rist1)
             
    #Generate card
        print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
    #7s=return str, 7d=decimal
        print("|", format(card1,"<7s"),"| ", " |", format(card2,"<7s"),"| ", " |",format(card3,"<7s"),"|", sep="")

        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    
        print("|",format(card1,"_>7s"),"|  |",format(card2,"_>7s"),"|  |",format(card3,"_>7s"),"|", sep="")
        print("")
        
    #implement rule win or lose
        if card1=="A" and card2=="A":
            print("[PLAYER] Double A!! You win $",player_bet*2)
            player_money=player_money+player_bet*2
            Pot=Pot-player_bet
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)

        elif card2=="K" and card3=="K":
            print("[PLAYER] Double K!! You win $",player_bet*2)
            player_money=player_money+player_bet*2
            Pot=Pot-player_bet*2
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)

        elif card3=="10" and card2=="J" or card2=="Q":
            print("[PLAYER] You lose $", player_bet)
            player_money=player_money-player_bet
            Pot=Pot+player_bet
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)

        elif card2==card1 and card2==card3:
            print("[PLAYER]"   , "HIT THE POST!!!")
            print("[PLAYER]"   , "You lose",player_bet*2)
            player_money=player_money-player_bet*2
            Pot=Pot+player_bet*2
            print("")
            print("Player: $ ",player_money,"Pot: $:",Pot)
            print("")
        else:
            print("[COMPUTER] You win $",player_bet)
            player_money=player_money+player_bet
            Pot=Pot-player_bet
            print("")
            print("Computer: $ ",computer_money,"Pot: $:",Pot)

        if player_money <= 0:
            print("Player is broke")

    #Computer turn   
    if computer_money >0 and player_money >0:
        
        input("PRESS <ENTER> to continue")
    
        print("[COMPUTER]", "","", "Cards are:")

    #Draw card
    for card1 in card1_replace_list:
        card1=random.choice(card1_replace_list)
    for card3 in card3_replace_list:
        card3=random.choice(card3_replace_list)

    #Check value
    #while card1==card3:
        #card3=random.choice(card_rist1)

    #=replace card1 and card3 it is not repalce
    #if card1>card3:
        #card1,card3=card3,card1

    #Generate cards
    print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")

    print("|", format(card1,"<7s"),"| ", " |", format("?","<7s"),"| ", " |",format(card3,"<7s"),"|", sep="")

    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    

    print("|",format(card1,"_>7s"),"|  |",format("?","_>7s"),"|  |",format(card3,"_>7s"),"|", sep="")
    print("")


    #computer maxbet minimum pot and money
    if computer_money<Pot:
        max_bet=computer_money
    elif Pot<computer_money:
        max_bet=Pot
    #add enhance computer bet
    card1_bet=["A","2","3"]
    card3_bet=["10","J","Q","K"]
    if card1==card1_bet and card3==card3_bet:
        computer_bet=max_bet
    elif card1 != card1_bet and card3 != card3_bet and computer_money>=30:
        computer_bet=random.randint(1,max_bet)
    else:
        computer_bet=0
    
    
    press=input("PRESS <ENTER> to continue")
    if press=="":
        #str(max_bet) = combine int+str = display number
        print("Enter bet (max $" + str(max_bet) + ") : $" + str(computer_bet))

    if computer_bet==0:
        print("[COMPUTER] PASS!")
    else:
        card2=random.choice(card_rist1)
             

        print(" ", "_"*7, "    ", "_"*7, "    " , "_"*7,    sep="")
    
        #7s=return str, 7d=decimal
        print("|", format(card1,"<7s"),"| ", " |", format(card2,"<7s"),"| ", " |",format(card3,"<7s"),"|", sep="")

        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
        print("|", " "*7, "|  |", " "*7, "|  |", " "*7, "|", sep="")
    
        print("|",format(card1,"_>7s"),"|  |",format(card2,"_>7s"),"|  |",format(card3,"_>7s"),"|", sep="")
        print("")

        #Implement win or lose
        if card1 =="A" and card2=="A":
            print("[COMPUTER] Double A!! You win $",computer_bet*2)
            computer_money=computer_money+computer_bet*2
            Pot=Pot-computer_bet*2
            print("")
            print("Computer: $ ",computer_money,"Pot: $:",Pot)
        elif card3=="10" and card2=="J" or card2=="Q":
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
        else:
            print("[COMPUTER] You win $",computer_bet)
            computer_money=computer_money+computer_bet
            Pot=Pot-computer_bet
            print("")
            print("Computer: $ ",computer_money,"Pot: $:",Pot)
            

        if computer_money <=0:
            print("Computer is broken")

    #game round add and each 5games add*2
    game_round+=1
    if game_round %5==0:
        Adds=Adds*2
        print("Ante increase! It is now $", Adds)
        print("Player:    $",player_money)
        print("Ante is:  $",Adds, "Pot: $", Pot)

    press=input("PRESS <ENTER> to continue")
    print("")

    if press=="":
        print("Player: $",player_money, "Computer:",computer_money)
        print("Ante is: $", Adds, "Pot:$",Pot)

    if player_money > 0:
        play_again=input("Do you wish to play a round ?(y / n ):")
        while play_again !="y" and play_again !="n":
            print("Please enter 'y' or 'n'")
            play_again=input("Do you wish to play a round ?(y / n ):")

        if computer_money<=0:
            print("Computer is broke!($",computer_money,")")
        
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
        













