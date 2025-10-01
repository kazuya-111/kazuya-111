#
# File: nakky007@mymail.unisa.edu.au_passwordGenerator.py
# Author:Kazuya Nakayama
# SAIBT ID:50587
# Version: 1.0 current date 30.11.2024
# Description: Assignment 1- \ldots.
# This is my own work as definded by SAIBT's
# Academic Misconduct policy.
import random
user_choice="0"
vaild_choice=["1","2","3","4"]

print("Welcome to the PSP Password Generator")
while user_choice !="4":
    
    print("*** Menu ***")
    print("1 Random")
    print("2 Encrypted word")
    print("3 Using a sentence")
    print("4 Quit")
#enter1
#user_choice upperletter Alphabet and random number
#list add append
    user_choice=input("Choose an option [1,2,3,4]:")
    #Loop not in valid_choice
    while user_choice not in vaild_choice:
        print("Choice must be between 1-4 inclusive.")
        user_choice=input("Choose an option [1,2,3,4]:")
    if user_choice=="1":
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #First letters =[A,B,C]
        password_first3_letters = []  
        #loop and append
        for _ in range(3):
            letter = random.choice(uppercase_letters)
            password_first3_letters.append(letter)
        #second_number of three  =[1,2,3]
        #loop and append
        password_second3_letters = []
        for _ in range(3):
            number=str(random.randint(0,9))
            password_second3_letters.append(number)
        #random_password="" -> ABC123
        random_password=""
        for generate_letters in password_first3_letters + password_second3_letters:
            random_password +=generate_letters
                
        print("Password:", random_password)

    ##enter2
    elif user_choice=="2":
        encrypt=input("Enter a word to encrypt:")
        offset=int(input("Please enter offset value (1 to 94): "))
        ##offset <1 or 94< offset invaild
        while offset < 1 or offset > 94:
            offset=int(input("Invaild offset. Please enter offset value (1 to 94):"))
            
        #="", empty str
        encrypted_password=""
        for new in encrypt:
            ##ord alphabet -> number of ascii
            ascii_encrypt=ord(new)
            new_ascii=ascii_encrypt+offset
            ##subtract 95 if over new_ascii 126
            if new_ascii>126:
                new_ascii -=95
            ##chr number of ascii -> ord
            encrypted_new=chr(new_ascii)
            encrypted_password +=encrypted_new
        
        print("Password:", encrypted_password)

    ##enter3
    elif user_choice=="3":
        user_sentence=input("Enter a sentence to encrypt (eding with .): ")
        #Invaild if not "." by the end
        index_of_last_character = len(user_sentence) - 1
        while user_sentence[index_of_last_character] !=".":
              user_sentence=input("Invalid sentence. Enter a sentence to encrypt (ending with .): ")
              index_of_last_character = len(user_sentence) - 1
        word=user_sentence.split()
        password_letters=""
        for generate in word:
            password_letters += generate[0]
        print("Password:" ,password_letters)
        
            
    ##enter4 display Goodbye
    elif user_choice=="4":
        print("Goodbye")






