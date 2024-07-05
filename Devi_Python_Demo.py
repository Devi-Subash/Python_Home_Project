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


# 11. write a python program to find the prime numbers from a given list. 

'''