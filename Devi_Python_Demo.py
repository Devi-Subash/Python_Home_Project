'''
this_list = ["apple", "banana", "cherry"]
my_list = ["A", "B", "C", "D" ]
my_tuple = ( 1, 2, 3, 4, 5)
my_set = {"a", "b", "c", "d"}

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

# 1. Program to find the smallest number in a given list.


def my_function_min (devi_list):
    min_val = devi_list[0]
    for a in devi_list:
        if a < min_val:
            min_val = a
    print([min_val])
    

devi_list = [5, 1, 2, 3, 5]
my_function_min(devi_list)


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
print(my_list)
sort_list = sorted(my_list)
print(sort_list)
for i in sort_list:
    sorted_dict = {i: my_dict[i]}
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


# 17. write a python program to create a dictionary from a string and track the count of letters from the string

user_input = str(input("Enter the string to "))

my_list2 = []
my_list2.extend(user_input)
out_put_dict = {}
for i in my_list2:
    if i in out_put_dict:
        out_put_dict[i] += 1
    else:
        out_put_dict[i] = 1
print(out_put_dict)


# 18. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3w'
# Expected Result : 'w3w3'
# Sample String : 'w3'
# Expected Result : 'w3w3'

input_var = str(input("Enter the string value: "))
l = len(input_var)
if l < 2:
    print("Entered string is too short")
elif l == 2:
    print(input_var[0:2] + input_var[0:2])
elif l == 3:
    print(input_var[0:] + input_var[0])
else:
    # print(input_var[0]+input_var[1]+input_var[l-2]+input_var[l-1])
    print(input_var[0:2]+input_var[-2:])


# 19. Write a Python program to get a single string from two given strings,
# separated by a space and interchange the first and second string,
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'



input_var1 = str(input("Enter the string value: "))
temp1 = input_var1
input_var2 = str(input("Enter the string value: "))
temp2 = input_var2

print(input_var1[0:-1]+input_var2[-1]+" "+input_var2[0:-1]+input_var1[-1])


# 20. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

input_var1 = str(input("Enter the string value:"))
char = input_var1[0]
print(char)
input_var1 =input_var1.replace(char,'$')
print(char+input_var1[1:])



# 21. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

input_var = str(input("Enter the string value: "))
l = len(input_var)
if l < 3:
    print("Entered string is too short")
else:
    if input_var[-3:] == "ing":
        print(input_var+"ly")
    else:
        print(input_var + "ing")


# 22. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is that poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

input_var = "I am not a bad boy" #"I am a good girl"

not_string = input_var.find('not')
good_string = input_var.find("good")
if not_string != -1:
    print(input_var[0:not_string]+input_var[not_string+4:])
elif good_string != -1:
    print((input_var[0:good_string]+"poor"+input_var[good_string+4:]))
else:
    print(input_var)

# 23. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

n = 0
length = 0
add_new_word = "Y"
while add_new_word.upper() == "Y":
    words = str(input("Enter the string value : "))
    add_new_word = str(input("Do you want to add a new word (Y or N) : "))
    length = len(words)
    if n < length:
        n = length
        l_word = words
print("The longest word is ", l_word)
print("The length of the longest word is ", n)


# 24. Write a Python program to count the occurrences of each word in a given sentence.
my_string = "This is my house. I love my house. I live in my house."
num = my_string.count('house')
print(f"The word house is displayed {num}")


# 25. Write a Python program to remove the nth index character from a nonempty string.


words = str(input("Enter the string value : "))
index = int(input("Enter the index value \"nth value\" which needs to be removed: "))
print(words[:index]+words[index+1:])


# 26. Write a Python program to change a given string to a new string where the 1st and last chars have been exchanged.

words = str(input("Enter the string value : "))

print(words[-1]+words[1:-1]+words[0])

# 27. Write a Python program to remove characters that have odd index values in a given string.

words = str(input("Enter the string value : "))
i = 0
result = ""
for i in range(len(words)):
    if i % 2 == 0:
        result = result + words[i]
print(result)


# 28. Write a Python program to count the occurrences of each word in a given sentence.
count = 0
sentence = "extreme tornadoes creates extreme deveastion and destruction for human lives"
my_dict = dict()
words = sentence.split()
print(words)
for char in words:
    print(char)
    if char in my_dict:
        my_dict[char] += 1
        #my_dict = {char, count}
        print(my_dict)
    else:
        my_dict[char] = 1
        #my_dict = {char, count}
        print(my_dict)
print("\n\n*****", my_dict)


# 29. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

my_list = []
string = "Devi"

my_list.extend(string)

print(my_list)
print(*my_list)



# 30. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

my_dict = {}
sample_string = "google.com"
for i in sample_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print (f"The count of {sample_string} is \n{my_dict}")


# 31. Write a Python program to calculate the length of a given string.

string_1 = 'devisubash'

print(len(string_1))


# 32. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


string1 = 'google.com'
final_result = {}

for i in string1:
    if i in final_result:
        final_result[i] += 1
    else:
        final_result[i] = 1

print(f"The count of {string1} is \n{final_result}")

# for item, values in final_result.items():
#     print(item, ':', values)



# 33. Write a Python program to get a string from a given string
# where all occurrences of its first char have been changed to '$',
# except the first char itself.
# Sample String : 'restarter'
# Expected Result : 'resta$te$'


string_1 = 'restarter'
temp = string_1[0]
final_string = ''
for i in string_1:
    if i == temp:
        final_string = string_1.replace(i, '$')
print(temp + final_string[1:])



# 34. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


def fun_longest_word(my_list):
    my_final_list = sorted(my_list, key=len)
    print(my_final_list)
    print((my_final_list[-1],len(my_final_list[-1])))


my_list = ['devi', 'subash', 'snithik']
fun_longest_word(my_list)




# 35. Write a Python program using functions to remove the nth index character using input function.

num_nth = int(input("Enter the nth value: "))
str_input = str(input("Enter the string value :"))
temp = len(str_input)
while temp <= num_nth:
    print("The nth value is wrong.")
    num_nth = int(input("Please renter the nth value: "))

print(str_input[:num_nth-1]+str_input[num_nth:])

'''





















