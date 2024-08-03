# writing multiple option for String Manipulation
from gtts import gTTS
# text ='
# 1. What is Python and what are its applications? Answer:  '
#
'''
string = 'sky'

print(len(string))
first_chr = string[0] ,string[1],string[2]
print(first_chr)
print('----------------------')
print(*first_chr)
print('----------------------')
print(string.upper())
print(string.lower())
print('----------------------')
first_2char =string[:1]
snd_car = string[-2]
tird_car = string[-1]
print( "", first_2char,"\n",snd_car ,"\n",tird_car)
print('----------------------')
print(string.replace('s','W'))
print('----------------------')
print(string.find('k'))
print('----------------------')
#print(string[::-1])

# list1 = [1,2,3,4,5]

# Define the string
original_string = "SKY is high"

# Reverse the string using slicing
reversed_string = original_string[::-1]

# Print the reversed string
print(reversed_string)

my_list1 = [1,2,3,4,5]
my_list2 = [6,7,8,9,10]
my_list1.extend(my_list2)

print(my_list1)

###### write a program to find the no of occurance in the list
list1 = ['N', 'D', 'L', 'K', 'S', 'K', 'D', 'L', 'L', 'L', 'D']
my_dict = {}
for i in list1:
    if i in my_dict:
        my_dict[i] = my_dict[i] + 1
    else:
        my_dict[i] = 1
print(my_dict)

###### write a program to find the union, in the list
'''
# l1 = ['apple','ball', 'cat','meyaiv']
# l2 = ['apple','car','ball','bike', 'bike']
# s1 = set(l1)
# s2 = set(l2)
# ns = s1 & s2
# na = s1 ^ s2
# print(na)
# print(ns)
# new_a = list(na)
# new_l = list(ns)
# # l1.extend(l2)
# # print(set(l1))
# print(new_l)
# print(new_a)
'''
# list = [1,2,3,4 , (5,"nithya") ,{6, "devi"} ,{"name:logi"}]
#
# print(list)
# print(list[3])

###### find the odd number in the list
odd_num =[1,2,3,4,5,6,7,7,7,8,7,8,8,9,11,13]
ne_li =[]
for i in odd_num:
    if i % 2 !=0:
        ne_li.append(i)
print(ne_li)

###### find the even number in the list

f_list = [1,2,3,4,5,6,7,8,9,10,13,1,4,21]
even_list=[]
for x in f_list:
    if x % 2 == 0:
        even_list.append(x)
print(even_list)

'''

###### write a python program to sort the dictionary by key

my_dict ={'logi':45 ,'nithya':44 }


##example of for loop
# list3 =[1,3,5,6,7,8]
# for i  in list3:
#     if i > 7:
#         print('this is right')
#     else:
#         print('this wrong')


# def v(inp):
#     v ='aeiouAEIOU'
#     find_v =[val for val in inp if val in v]
#     return find_v
#
# inp = input('enter a string to fine Vowel in that - ')
# final =v(inp)
# print(f'The Vowel in the given string is ',final)
#

