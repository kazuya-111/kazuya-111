#
# File: nakky007@mymail.unisa.edu.au_list_function
# Author:Kazuya Nakayama
# SAIBT ID:50587
# Description: Assignment 2- part1
# This is my own work as definded by SAIBT's
# Academic Misconduct policy.
#

#Sample list
str_list1 = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
str_list2 = ['r', 'e', 'd']
empty = []

#\n=new line
print("\nStart Testing!")


#caluculate length of list without len()function
def length(my_list):
    #number of count= measure
    measure = 0

    # count the list of elements by using for loop.
    for item in my_list:
        measure = measure + 1

    #if not return disiplay none
    return measure

#Display length
print("\nlength Test")
print("str_list1 length:", length(str_list1))

print("List empty length:",length(empty))


# The my_list is sperated "," using sep=",".sep add between element.
def to_string(my_list, sep=', '):
    #empty str can remove []
    string = ''
    #def length() convert number of index.Putting index.
    for index in range(length(my_list)):
        #index not () -1 add element+"," as a string.
        if index != length(my_list)-1:
            string += str(my_list[index]) + sep
        #index == -1(end of element) add element as a string.
        else:
            string += str(my_list[index])
    #return result
    return string

#Display result
print("\nto_string Test")
print("List is:",to_string(str_list1))
print("List is:",to_string(str_list1,sep="-"))
print("List is:",to_string(empty))




# Function count() - place your own comments here...  : )
#count the value in my_list
def count(my_list, value):
    #times=number of count
    times = 0
    #for loop  my_list of elements to val.
    for val in my_list:
        #if val == value count +1
        if val == value:
            times += 1
    #result return
    return times

#Display result
print("\ncount Test")
print("Number of i is",count(str_list1,"i"))
print("Number of a is",count(str_list2,"a"))
print("Number of z is",count(empty,"z"))

# Function find() - place your own comments here...  : )
# find the value of index position.
def find(my_list, value):
    i = -1
    #for loop my_list number of index to index.
    for index in range(length(my_list)):
        #if find the value(The spcified character) return index
        if my_list[index] == value:
            #display number
            return index
    #else result return i, display -1
    return i

print("\nfind Test")
print("g", "location is",find(str_list1,"g"))
print("a", "location is",find(str_list2,"z"))


#sample list
str_list3 = ['one','three','four', 'five', 'six']
str_list4 = ["i", "t"]

#add value specified index in the list.
def insert_value(my_list, value, insert_position):
    #empty list
    new_list = []

    #specified position is outside the range of the list.
    if insert_position > length(my_list):
        #be adjusted to the end.
        insert_position = length(my_list)
    elif insert_position < 0:
        #be adjusted to beginning.
        insert_position = 0

    #for loop
    for index in range(length(my_list)):
        #value add to new list
        if index == insert_position:
            new_list.append(value)
        new_list.append(my_list[index])
    #add value end of list
    if insert_position == length(my_list):
        new_list.append(value)
        
    return new_list

#Display test
print("\ninsert_value Test")
print(insert_value(str_list3,"two",1))
print(insert_value(str_list4,"p",0))
new_list4=insert_value(str_list4,"p",0)
print(insert_value(new_list4,"s",-1))
latest_list4=insert_value(new_list4,"s",-1)
print(insert_value(latest_list4,"s",7))



# Function remove_value() - place your own comments here...  : )
#remove element from list
str_list5=["r","i","n","g"]
def remove_value(my_list, remove_position):
    #empty list
    new_list = []

    #be adjust to the begin
    if remove_position < 0:
        remove_position = 0

    #be adjust to the end
    elif remove_position > length(my_list):
        remove_position = length(my_list) - 1

    for index in range(length(my_list)):
        if index != remove_position:
            new_list.append(my_list[index])

    return new_list
#Display
print("\nremove_value Test")
new_list=remove_value(str_list5, 2)
print(new_list)
new_list2=remove_value(str_list5, -1)
print(new_list2)
new_list3=remove_value(str_list5, 10)
print(new_list3)


#\n=new line
print("\n----------")


num_list1 = [1, 7, 2, 3, 7, 7]

print("\nlength Test")
print("List length:", length(num_list1))

print("\nto_string Test")
print('List is:', to_string(num_list1))
print('List is:', to_string(num_list1, sep=' - '))

print("\ncount Test")
print(count(num_list1, 7))

print("\nfind Test")
print(find(num_list1, 7))

print("\ninsert_value Test")
num_list2 = [1, 3, 4, 5, 6]
num_list2 = insert_value(num_list2, 2, 1)
print(num_list2)

print("\nremove_value Test")
num_list3 = [1, 3, 4, 5, 6]
num_list3 = remove_value(num_list3, 1)
print(num_list3)

print("\nEnd Testing!\n")











    




