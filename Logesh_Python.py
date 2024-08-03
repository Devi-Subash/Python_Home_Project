import tableutil

'''

# adding two numbers
a = int(10)
b = int(20)
c = a + b
print('The sum of 2 numbers = ', c)

# getting the input from the user
reputation = int(input('how many times you need to add = '))
i = 0
while i <= reputation:
    first_num = int(input('provide the 1st number = '))
    second_num = int(input('provide the 2nd number = '))
    sum_result = first_num + second_num
    print('The sum of given two numbers is =',sum_result)
    i += 1
print('End of the sum')

# Write a program to sort the dictionary by key.

new_dict = {"apple": 3,
            "element": 12,
            "gun": 10,
            "ball": 6}
final_output ={}
item = list(new_dict)
a = sorted(item)
print(a)
for i in a:
    final_output = {i, new_dict[i]}
    print(final_output)

# Write a program min and max value of dict

v_dict ={"Rose": 3, "Bat": 7, "Cat": 2, "Dog": 8}
n_dict ={}
i = 0
n_list = list(v_dict[i])
n_sorted = sorted(n_list)
print(n_sorted)
#for b in n_list:
 #   new_value = list[n_list[b]]
  #  print(new_value)


# write a python program to find the length of a string.

i_string = str(input("Enter the string to find its length = "))

print(len(i_string))
leng = 0
for char in i_string:
    leng += 1
print(leng)



# L3_D18 write a python program to give the below result
# Sample String : 'w3resource'
# # Expected Result : 'w3ce' ----1 logic
# Sample String : 'w3'
# Expected Result : 'w3w3 -----2 logic
# Sample String : 'w32'
# Expected Result : 'w32w ------3rd logic

stng = str(input('Input the string ='))
i = len(stng)
if i < 2:
    print('The given string is too short')
elif i == 2:
    print('The given string value =',stng[:2] + stng[:2])
elif i == 3:
    print('The given string value =', stng[:2] + stng[0])
else:
    print('The given string value =', stng[:2] + stng[-2:])

opt = stng[:2]
opt_1 = stng[-2:]
print("The first and last two letter of the string is ", opt + opt_1)
print(' print the first 2 char twice = ', opt + opt) 

# L4_D21. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# # Sample String : 'abc'
# # Expected Result : 'abcing'
# # Sample String : 'string'
# # Expected Result : 'stringly'
# method 1
inp_str = str(input('Give the input string ='))
leng = len(inp_str)
find = str(inp_str[-3:])
a = str('ing')
if leng >= 3:
   if find == a:
     print('The updated string is',inp_str + 'ly')
   else:
     print('The updated string is',inp_str + 'ing')
else:
    print('Enter the string with minimum 3 char')

    # method 2
inp_str = str(input('Give the input string ='))
leng = len(inp_str)
find = str(inp_str[-3:])
if leng >= 3:
    if inp_str.endswith('ing'):
        print('The updated string is', inp_str + 'ly')
    else:
        print('The updated string is', inp_str + 'ing')
else:
    print('Enter the string with minimum 3 char')



L5_D22# program to translate the string charter
trim_sample ='I am superrrrrr'
print(trim_sample)
decor = trim_sample.maketrans('r','c')
print(trim_sample.translate(decor))


L6_D21# Write a Python program to count the occurrences of each word in a given sentence.
# Write a program to do all upper ,lower, transulate,ltrim,rtrim,endwith,startwith

each_word = 'This world is the BEAUTIFUL world with the Beautiful PEOPLE'
num = len(each_word)
print(num)
print(f"Print the length {num} \nnumber of same word ={ each_word.count('the')}")
print(f" \nAll words are converted in to Upper Case = {each_word.upper()}")




#L7_D21  Write a Python program to remove the nth index character from a nonempty string.

def remove_n_charter(remove_char, i):
    if i >= len(remove_char) or i < 0:
        return "Error :the string is out of range"
    return remove_char[:i] + remove_char[i + 1:]


remove_char = input('Please enter a string = ')
i = int(input('Enter which index char need to be removed = '))

result = remove_n_charter(remove_char, i)
print('The updated given string is =', result)



#L7_D21  Write a Python program to find a minimum and Maximum number in the list,tuple,set and dictnoary


logi_List = [4, 3, 7, 2, 4, 6, 7, 6, 8, 9, 6]
logi_List.sort()
print(logi_List)
print(f"The minimum value is {logi_List[0]} \nThe maximum value is {logi_List[-1]}")


logi1_List = [4, 3, 7, 2, 4, 6, 7, 6, 8, 9, 6]
min_value = logi1_List[0]
for i in logi1_List:
    if i < min_value:
        min_value = i
print(f"The given minum value is {min_value}")


def mini (logi1_list):
    min_value = logi1_List[0]
    max_value = logi1_list[0]
    for i in logi1_List:
        if i < min_value:
            min_value = i
        if i > max_value:
             max_value = i
    print(f"The given Max value is {min_value}")
    print(f"The given minum value is {max_value}")


logi1_List = [4, 3, 7, 4, 6, 7, 6, 8, 9, 6]
mini(logi1_List)



# write a program to delete a[0], a[6], a[7], a[8] values from a list1 and
# add list2 to list1 and make it as new list
# then count the occurance of each variable and store it in a dict using functions

#list_1 = [2, 3, 4, 2, 3, 6, 7, 4, 7, 8, 9, 3, 4, 5, 9, "devi"]
#list_2 = [9, 5, 7, 3, 5, 2, 1, 0]

# write a program to delete a[0], a[6], a[7], a[8] values from a list1
# list_1.remove(2) #remove is used to delete the first occurance

#del_Val = list_1.pop()
#print(del_Val)
#print(list_1)
#del list_1[6:9]
#del list_1[0]
#del list_1[-1]
#del list_1

#print(list_1)

# add list2 to list1 and make it as new list
#list_1.append(list_2)# add the 2nd list as it is with square brackets
#print(list_1)
#lent =len(list_2) +len(list_1)
#print(lent)
#list_2.extend(list_1) # add the 2nd list with the existing list without square brackets
#print(list_2)

# then count the occurance of each variable and store it in a dict using functions
list_1 = [2, 3, 4, 2, 3, 6, 7, 4, 7, 8, 9, 4, 5, 9, 2]
#list_1 = [2, 3, 4, 2, 3, 6, 7, 4]
list_2 = [9, 5, 7, 3, 5, 2, 1, 0,1,2,3,4,45,5,5,6,6,6,7,9]

# my_table  = Table.init_from_tree(your_list_or_dict)
#print(my_table)
,----------------------------------------------------------,
my_dic = {}

for x in list_1:
    if x in my_dic:
        my_dic[x] = my_dic[x] +1
    else:
        my_dic[x] = 1
print (my_dic)
,-----------------------------,
def fun(input):
    my_dict = {}

    for x in list_2:
        if x in my_dict:
            my_dict[x] = my_dict[x] + 1
        else:
            my_dict[x] = 1
    print(my_dict)
fun(list_2)
############################################
txt = "The best things free in life are !So we are great full"
if "free" in txt:

    print(txt.replace('b','B'))
    print(txt.split(","))
    print("Yes, 'free' is present.")
elif 'logi' not in txt:
    print("No, 'logi' is not present.")
print(""" I\'M a \r \n programmer""")


dip = zip(list_1,list_2)
list_pair = list(dip)
print(list_pair)
dic_of_list = dict(list_as_pair)
print("dictonary vale of the list is ",dic_of_list)

# Range
num = range(2,5)
print(num)

# Form a table using the given Data
names = ['Raj', 'Shivam', 'Shreeya', 'Kartik']
marks = [7, 9, 8, 5]
div = ['A', 'A', 'C', 'B']
id = [21, 52, 27, 38]

# printing Aligned Header
print(f"{'Name' : <10}{'Marks' : ^10}{'Division' : ^10}{'ID' : >5}")

# printing values of variables in Aligned manner
for i in range(0,5):
    print(f"{names[i] : <10}{marks[i] : ^10}{div[i] : ^10}{id[i] : >5}")

'''
# # Count the charaters of the String.
# my_dic = {}
# string_count = "google.com"
# for i in string_count:
#     if i in my_dic:
#         my_dic[i] += 1
#     else:
#         my_dic[i] = 1
#
#
# for i in my_dic:
#    # print(i, ":", my_dic[i])
# this_list =['apple', 'k','b','mango','apple ','apple','cherry']
# for x in this_list: #range(len(this_list)) :
#     if x == 'mango':
#         continue
#     print(x)

     # else:
     #     print(this_list[x])
    #print(x)

# this_list.pop()
# print(this_list)
# this_list.append('orrange')
# this_list.extend(['kiwi'])
# this_list.insert(3,'mango')
# this_list.remove('apple')
# this_list[1] ='orange'

#print(this_list)
# if 'mango' not in this_list:
#     print('yes not in this_list')


#
# tuple = (3, 4, 5, 2, 3, 4, 2, 5, 2, 4, 3 , 2, 3, 4, 2, 2, 3, 4, 5, 2)
# my_dict = { }
# for j in tuple:
#     if j in my_dict:
#         my_dict[j] += j #
#     else:
#         my_dict = 1
# print(my_dict[j])

#                    For and break loop
# for i in range(7):
#     if  i == 3 :
#         break
#     print(i)
# else:
#     print('Iteration is finished')

# a = ['banana','apple','stabary','mango']
# b = ['1','2','3']
# for x in a:
#     for y in b:
#         print(x , y)

#    program for looping with range
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
# start_index = 1
# end_index = 4
# for x in range(start_index,end_index):
#     print(fruits[x])
# print("Items from index", start_index, "to", end_index - 1, ":")
# for i in range(start_index, end_index):
#     print(fruits[i])


# add fruits in set
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

# # write a function which counts the number of unique triplets
# # (substrings of length three) in a string and
# # return this integer value
#
# list_new = ["AAA", "AAA", "ABC", "ADC", "ACE", "ABC"]
# list_dup = set(list_new)
# print(f'The unique value of the string is {len(list_dup)}')
# duplicates = set()
# seen = set()
# for item in list_new:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)
# print(f'The duplicate value of the string is {duplicates}')
#
# string_1 = "AAAAGHBFTA"
# substring = "AYA"
# positions = []
#
# temp = string_1.find(substring)
# if temp != -1:
#     print(f'The sub string of {substring} of string {string_1} is present')
# else:
#     print(f'The sub string of {substring} of string {string_1} is NOT present')

#How to insert a element in a list

# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(2,'orange')
# print(fruits)

#Example of Finding Substring Occurrences:
text = "Hello, World! Welcome to this World!"
count =text.count('World')
print(count)

#Example of Finding Substring Occurrences:

