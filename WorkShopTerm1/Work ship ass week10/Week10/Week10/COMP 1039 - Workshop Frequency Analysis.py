#
# File: psp_workshop_week_10.py
# Author: Trung Kien Than & Kazuya Nakayama
# SAIBT Id: 52721 & 50587
# Version: 1.0 20 December 2024
# Description: Workshop Week 10 - Frequency Analysis
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
# Team Members:
# Member 1: 52721
# Member 2: 50587


# Opens a named text file
infile = open("herodotus.txt", "r")
#infile = open("sense_and_sensibility.txt", "r")
#infile = open("the_wizard_of_oz.txt", "r")

# Read contents of files
string = infile.read()

# Close files
infile.close()

new_string = ""
# CONVERT the contents to uppercase
for letter in string:
    new_string += letter.upper()    
print(new_string)
alphabet = []
letter_counts = [0] * 26
total = 0

for ascii_val in range(65,91,1):
    # print(ascii_val, chr(ascii_val))
    alphabet.append (chr(ascii_val))

# Counts the occurrence of each alphabetic character (treat upper and lower case as the same character).
for index in range(len(alphabet)):
    char = alphabet[index]
    nums = new_string.count(char)
    letter_counts[index] = nums
    
# Calculate total number of alphabetic characters
total = sum(letter_counts)

# total > 0 print frequency stars       
if total > 0:
    for index in range(len(alphabet)):
        char = alphabet[index]
        percentage = (letter_counts[index] / total) * 100
        frequency_stars = "*" * int(percentage)
        print(char + "  " + frequency_stars)
# total < 0 print char " "

else:
    for index in range(len(alphabet)):
        char = alphabet[index]
        print(char + "  ")






