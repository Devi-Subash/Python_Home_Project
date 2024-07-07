'''
this_list = ["apple", "banana", "cherry"]
my_list = ["A", "B", "C", "D" ]
my_tuple = ( 1, 2, 3, 4, 5)
my_set = {"a", "b", "c", "d"}
'''
# print(this_list)
# print(len(this_list))
# this_list.insert(2, my_tuple)  # this will insert
# this_list.append(my_tuple) # this will insert in the last
# mylist.extend(this_list)
# this_list[2] = "orange" # It will override
# new_list = this_list + mylist # concatenation
# this_list[1] = "watermelon"
# this_list.remove("apple")
# del this_list[0]
# this_list.clear()
# this_list.pop(0)
# this_list.pop() # removes the last one from the list
# this_list.sort(reverse=True)
# this_list.reverse()








'''
# 1. Program to find the smallest number in a given list.
my_list = [ 5, 1, 2, 3, 5]
min = my_list[0]
for a in my_list:
    if a < min:
        min = a
print (min)

# 2. Write a program to print a specified list after removing [0],[4]&[5] elements.

my_list = ["red", "green", "white", "black", "pink", "yellow"]
del my_list[4:6]
del my_list[0]

print(my_list)

# 3. Write a python program to append a list to the second list

first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 10]
first_list.append(second_list)
print(first_list)

# 4. write a python program to get unique values from a list

my_list = [1, 2, 1, 3, 2, 1, 3, 1, 2]
my_set = set(my_list)
new_list = list(my_set)
print (new_list)

# 5. write a python program to get the frequency of elements in a list

my_list = [1, 2, 1, 3, 2, 1, 3, 1, 2]
my_dict = {}

for x in my_list:
    if x in my_dict:
        my_dict[x] = my_dict[x]+1
    else:
        my_dict[x] = 1

print(my_dict)

# 6. write a python program to find common items in two list.

first_list = ["red", "blue", "yellow"]
second_list = ["pink", "blue", "orange"]

result_list = set(first_list) & set(second_list)
print(result_list)

# 7. write a program to select odd numbers from a list

my_list = [2, 3, 5, 7, 6, 8, 9, 2, 1]
my_set = set(my_list) # To remove duplicates.
result_list = []
for x in my_set:
    if x % 2 != 0:
        result_list.append(x)

print(result_list)

# 8. write a program to split a list every nth element [4]

my_list = [2, 3, 5, 7, 6, 8, 9, 2, 1, 2, 3, 5, 7, 6, 8, 9, 2, 1, 2, 3, 5, 7, 6, 8, 9, 2, 1]
num = int(input("Enter the nth value, so the list can be split accordingly: "))
chunks = []


while True:
    if len(my_list) <= 0:
        break
    chunks.append(my_list[0:num])
    del my_list[0:num]

print(chunks)

# 9. write a python program to concatenate 2 lists, and store the value in list 1 and remove duplicates and print in assending order

my_list1 = [2, 3, 5, 7, 6, 8, 9, 2, 1]
my_list2 = [7, 8, 9, 11, 7, 9, 0, 12, 41]

my_list1 = my_list1 + my_list2
my_set = set(my_list1)
new_list = list(my_set)
new_list.sort()
print(new_list)

# 10. write a python program to find the difference between two lists.

my_list1 = [2, 3, 5, 7, 6, 8, 9, 2, 1]
my_list2 = [7, 8, 9, 11, 7, 9, 0, 12, 41]

my_new_list = set(my_list1) - set(my_list2)
print(list(my_new_list))

# 11. write a python program to find the prime numbers from a given list 
# **********************************************************************
my_list= [5, 3, 6, 8, 35, 2, 9, 7, 11, 13, 17]
i=0
for i in my_list:
    if my_list[i] % 2 == 0 and my_list[i] % 3 == 0 and my_list[i] % 5 == 0 and my_list[i] == 7:
        print(f"The given number {my_list[i]} is a prime number")
    elif my_list[i] in [2,3,5,7]:
        print(f"The given number {my_list[i]} is a prime number")
    else:
        print(f"The given number {my_list[i]} is not a prime number")

# 12. write a python script to add a key value to a dict

my_dict={"name": "Devi", "age": 39}
print(my_dict)
my_dict["place"] = "reading"
print(my_dict)
my_dict.update({"country":"UK"})
print(my_dict)


# 13. write a python script to concatenate 3 dictionaries
my_dict1={"name": "Devi", "age": 39}
my_dict2={"place": "Reading", "Country": "UK"}
my_dict3={"Skills": "Data", "Work": "Data Engineer"}
new_dict = {}
#new_dict = my_dict1 | my_dict2 | my_dict3
for i in (my_dict1,my_dict2,my_dict3):
    new_dict.update(i)

print(new_dict)

# 14. write a python script to generate and print a dictionarty that contains a number between 1 and n in the form of x,x2

new_dict = {}
num = int(input("Enter the value until which the dictionary needs to be populated: "))
for i in range(1,num+1):
    new_dict.update({i:i*i})
print(new_dict)

# 15. write a python program to sort a given dictionary by key

my_dict = {"red": 234, "blue": 939, "yellow": 567, "pink": 453, "orange": 231}
sorted_dict = {}
my_list = list(my_dict)
sort_list = sorted(my_list)
print(sort_list)
for i in sort_list:
    sorted_dict = {i : my_dict[i]}
    print(sorted_dict)

#*************************************************************
# 16. write a program to get the max and min values from a dic
#*************************************************************

my_dict = {"red": 234, "blue": 939, "yellow": 567, "pink": 453, "orange": 231}
my_list =[]
min_dict = {}
max_dict = {}
for i in my_dict:
    my_list.append(my_dict[i])
my_list = sorted(my_list)
len = len(my_list)
#min_dict = {my_dict[]:my_list[0]}
#max_dict = {my_dict[]:my_list[len-1]}

print(my_list)
print(min_dict)
print(max_dict)

'''

# 17. write a python program to create a dictionary from a string and track the count of letters from the string

user_input = str(input("Enter the string to "))

my_list2 = []
my_list2.extend(user_input)
for i in my_list2:


print(my_list2)