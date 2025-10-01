#
#File: Workshopweek4
#Author: Trung Kien Than (52721) & Kazuya Nakayama (50587)
#Description: Workshopweek4 Locj, paper, scissors game

import random

times=0
try_again='y'

while try_again =='y':
        user_choice=input("rock(1), paper(2) or scissors (3): ")
        
        while user_choice != '1' and user_choice != '2' and user_choice !='3': 
            print("Invalid input.Please enter 1, 2, or 3.")
            user_choice=input("rock(1), paper(2) or scissors (3): ")
        if user_choice == '1':
            print("You chose rock")
        elif user_choice == '2':
            print("You chose paper")
        elif user_choice == '3':
            print("You chose scissors")
        else:
            print("Chose again")
            
        computer_choice= random.randint(1,3)
        if computer_choice == '1':
            print("Computer chose rock")
        elif computer_choice == '2':
            print("Computer chose paper")
        else:
            print("Computer chose scissors")

        if user_choice == computer_choice:
            print("The same gesture, the game is a draw")
        elif user_choice == '1' and computer_choice =='3':
            print("You win - Rock crushes scissors")
        elif user_choice == '2' and computer_choice =='1':
            print("You win - Paper covers rock")
        elif user_choice == '3' and computer_choice =='2':
            print("You win - Scissors cut paper")
        else:
            print("Computer win!")
       
        times+=1
        print("You played", times)
        try_again = input("Would you like to play again? (y/n): ").lower()
        while try_again != 'y' and try_again != 'n' :
          print("Invalid input. Please enter 'y' for yes or 'n' for no.")
          try_again = input("Would you like to play again? (y/n): ").lower()
        if try_again == 'n':
          print("Thank u")
        
          
                  
        



   
