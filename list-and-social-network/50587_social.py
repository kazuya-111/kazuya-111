#
# File: nakky007@mymail.unisa.edu.au_social
# Author:Kazuya Nakayama
# SAIBT ID:50587
# Description: Assignment 2- part2 making profiles
# This is my own work as definded by SAIBT's
# Academic Misconduct policy.
#

import profile
# import list_function  # Uncomment this when/if needed



# Function read_file() - For reading file from file: )
def read_file(filename, profile_list):
    #Open file
    infile=open(filename, "r")
    # Create and initialise variable line to "-1"
    line= "-1"
    while line != "":
        line= infile.readline()
        if line != "":
            line=line.strip("\n")
            details=line.split(" ")
            given_name = details[0]
            family_name = details[1]
            email = details[2]
            gender = details[3]
            
            new_profile= profile.Profile() #Create a new file
            new_profile.set_given_name(given_name) 
            new_profile.set_family_name(family_name)
            new_profile.set_email(email)
            new_profile.set_gender(gender)

            line = infile.readline()
            line = line.strip("\n")
            new_profile.set_status(line)

            line= infile.readline()
            line= line.strip("\n")
            num_friends = int(line)
            new_profile.set_number_friends(num_friends)
            friends =[]
            for index in range(num_friends):
                line = infile.readline()
                line= line.strip("\n")
                friends.append(line)

            new_profile.set_friends_list(friends)
            profile_list.append(new_profile)
            

# Function display_summary() - For displaying file: )
def display_summary(profile_list):
    print("="*78)
    print("Profile Summary")
    print("="*78)
    
    for p in profile_list:
        print("-"*78)
        print(f"{p.get_given_name()} {p.get_family_name()} ({p.get_gender()} | {p.get_email()})")
        print(f"- {p.get_status()}")
        num_friends = p.get_number_friends()
        if num_friends == 0:
            print("- No friends yet . . .")
        else:
            friends = p.get_friends_list()
            print(f"- Friends ({p.get_number_friends()}):")
            for email in friends:
                print(f"    {email}")
        
    print("-"*78)
    print("="*78)

# Function write_to_file() - For wirting file to new file: )
def write_to_file(filename, profile_list):
    outfile = open(filename, "w")
    for p in profile_list:
        # out file basic information
        given_name = p.get_given_name()
        family_name = p.get_family_name()
        email = p.get_email()
        gender = p.get_gender()
        outfile.write(f"{given_name} {family_name} {email} {gender}\n")
    
        #wirte the status
        status = p.get_status()
        outfile.write(f"{status}\n")
    
        #write the number of friends
        num_friends = p.get_number_friends()
        outfile.write(f"{num_friends}\n")
    
        #write the friends list
        friends_list = p.get_friends_list()
        for friend in friends_list:
            outfile.write(f"{friend}\n")
    
        #add new line
        outfile.write("\n")
    outfile.close()


# Function find_file() - For finding profile by using email: )
def find_profile(profile_list, email):
    #Loop for finding profile
    for index in range(len(profile_list)):
        if email == profile_list[index].get_email():
            return index
    #if not return -1
    return -1

# Function add_profile() - For adding profile: )
def add_profile(profile_list):
    email = input("Please enter email address: ")
    
    # Check if the email already exists in profile_list
    
    email_exists = True #Represent the truthfulness of condition
    profile_index = find_profile(profile_list,email)
    if profile_index != -1:
        print(f"{email} already exists in profiles.")
        email_exists = False

    # Collecting other profile details
    if email_exists:
        given_name = input("Please enter given name: ")
        family_name = input("Please enter family name: ")
        gender = input("Please enter gender: ")
        status = input("Please enter current status: ")
    
        new_profile= profile.Profile()
        # Setting profile details using the provided functions
        new_profile.set_given_name(given_name)
        new_profile.set_family_name(family_name)
        new_profile.set_gender(gender)
        new_profile.set_status(status)
        new_profile.set_email(email)
        new_profile.set_number_friends(0)

        profile_list.append(new_profile)
        print(f"Successfully added {email} to profiles.")
    
    

# Function remove_profile() - removing friend in the profile_list: )
def remove_profile(profile_list):
    email = input("Please enter email address: ")
    #Found the email from the list
    email_exists = True
    profile_index = find_profile(profile_list,email)
    if profile_index == -1:
        print(f"{email} is not found in profiles.")
        email_exists = False

    #delete profile from the list
    if email_exists:
        for index in range(len(profile_list)):
            profile_list[index].remove_friend(email)
        del profile_list[profile_index]
    
    
        print(f"Successfully removed {email} from profiles.")

    
        
# Function update_profile() - For updating profile : )
def update_profile():
    email = input("Please enter email address: ")
    is_found = False

    for profile in profile_list:
        if profile.get_email() == email:
            is_found = True
    
    if not is_found:
        print(f"{email} is not found in profiles.")       

    else:
        for profile in profile_list:
            profile_email = profile.get_email()
            if email == profile_email:
                action = input(f"Update {profile.get_given_name()} {profile.get_family_name()} [status|add_friend|remove_friend]: ")

                if action == "status":
                    new_status = input("Please enter new status: ")
                    profile.set_status(new_status)
                    print(f"Updated status for {profile.get_given_name()} {profile.get_family_name()}:")
                    
                    print(f"{profile.get_given_name()} {profile.get_family_name()} ({profile.get_gender()} | {profile.get_email()})")
                    print(f" - {profile.get_status()}")
                    print(f" - Friends ({profile.get_number_friends()}):")
                    friends_list = profile.get_friends_list()
                    for friend in friends_list:
                        print(f"     {friend}")

                elif action == "add_friend":
                    new_friend = input("Please enter email address of new friend: ")
                    profile_index = find_profile(profile_list,new_friend)
                    email_exists = False
                    if profile_index == -1:
                        print(f"{new_friend} is not found in profiles.")
                        email_exists = True

                    if not email_exists:
                        friend_not_found = profile.add_friend(new_friend)
                        if friend_not_found:
                            print(f"Added {new_friend} updated profile is:")
                    
                            print(f"{profile.get_given_name()} {profile.get_family_name()} ({profile.get_gender()} | {profile.get_email()})")
                            print(f" - {profile.get_status()}")
                            print(f" - Friends ({profile.get_number_friends()}):")
                            friends_list = profile.get_friends_list()
                            for friend in friends_list:
                                print(f"     {friend}")

                        else:
                            print(f"{new_friend} is already friend")
 
                elif action == "remove_friend":
                    previous_friend = input("Please enter email address of friend to remove: ")
                    
                    friends = profile.get_friends_list()
                    friend_not_found = True
                    for friend in friends:
                        if friend == previous_friend:
                            profile.remove_friend(previous_friend)
                            friend_not_found = False
                    if friend_not_found:
                        print(f"{previous_friend} is not {profile.get_given_name()} 's friend.")
                        
                    else:
        
                        print(f"Removed {previous_friend} updated profile is:")
                        print(f"{profile.get_given_name()} {profile.get_family_name()} ({profile.get_gender()} | {profile.get_email()})")
                        print(f"- {profile.get_status()}")
                        print(f"- Friends ({profile.get_number_friends()}):")
                        friends_list = profile.get_friends_list()
                        for friend in friends_list:
                            print(f"    {friend}")
                    
                else:
                    print("Not a valid command, please try again.")

import os

def read_file(filename, profile_list):
    script_dir = os.path.dirname(__file__)   # このスクリプトがあるフォルダ
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as infile:
            for line in infile:
                profile_list.append(line.strip())
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

   
profile_list=[]

read_file('profiles.txt', profile_list)

        
choice_list=["summary","add","remove","search","update","quit"]

choice=input(" Please enter choice [summary|add|remove|search|update|quit]: ")

#Not valid user input
while choice not in choice_list:
    print("Not a valid command- please try again.")
    choice=input(" Please enter choice [summary|add|remove|search|update|quit]: ")

while choice != "quit":

    if choice=="summary":
        display_summary(profile_list)
        
    elif choice=="add":
        add_profile(profile_list)
        
    elif choice=="remove":
        remove_profile(profile_list)
        
    elif choice=="search":
        email = input("Please enter the email address: ")
        index = find_profile(profile_list, email)
        if index != -1:
            profile = profile_list[index]
            print(f"{profile.get_given_name()}{profile.get_family_name()} ({profile.get_gender()} | {profile.get_email()}) ")
            print(f"- {profile.get_status()}")
            friends = profile.get_friends_list()
            print(f"- Friends ({profile.get_number_friends()}):")
            for email in friends:
                print(f"    {email}")

        else:
            print(f"{email} is not found in profiles.")
        
        
    elif choice=="update":
        update_profile()

    choice=input("Please enter choice [summary|add|remove|search|update|quit]: ")

    while choice not in choice_list:
        print("Not a valid command- please try again.")
        choice=input(" Please enter choice [summary|add|remove|search|update|quit]: ")
  
write_to_file('new_profiles.txt', profile_list)
print("\n\n-- Program terminated --") 

