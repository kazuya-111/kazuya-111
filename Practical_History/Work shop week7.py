#
# File: Workshop week7.py
# Author: Kazuya Nakayama and Kien
# SAIBT ID: 50587/ nakky007@mymail.unisa.edu.au
# Description: Work shop week7.
# This is my own work as defined by SAIBT's
# Academic Misconduct policy.
#Write a program that:
#• Creates an empty list called items
#• Loops asking the user to enter an item until they enter
#“STOP”.
#• The loop should:
#• Add the item to the list
#• Print out how many items have been entered
#• If the user enters an item already in the list, it should
#display an error message and ask again until a user enters
#a valid name
#• Prints out all items nicely formatted (with names (given
#and family) starting with a capital letter and rest lower
#case)

items=[]
count=0
user_input=input("Enter an item ('STOP' to quit):")

while user_input != "STOP":
  ##  user_input=input("Enter an item ('STOP' to quit):")
  ##  for character in user_input:
    user_input=user_input.capitalize() 
    if user_input in items:
        print(" Error:", user_input, "already entered.")
    else:
        items.append(user_input) 

        print(count,".",items)


   ## print(count,".",items)
        count +=1
        print("You have", count , "items")
    user_input=input("Enter an item ('STOP' to quit):")

index=1
for item in items:
    print(index, "." , item)
    index +=1
    
        
