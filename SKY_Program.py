# write a program to find the no of occurrence in the list
# def count_characters(input_string):
#     # Initialize counters
#     count_s = 0
#     count_k = 0
#     count_y = 0
#
#     # Loop through each character in the string
#     for char in input_string:
#         if char == 's':
#             count_s += 1
#         elif char == 'k':
#             count_k += 1
#         elif char == 'y':
#             count_y += 1
#
#     # Print the results
#     print(f"'s' appears {count_s} times.")
#     print(f"'k' appears {count_k} times.")
#     print(f"'y' appears {count_y} times.")
#
# # Example usage
# input_string = "sky"
# count_characters(input_string)

# # Second Method to achieve
# input_string = "sky"
# my_dict = {}
# # Loop through each character in the string
# for i in input_string:
#     if i in my_dict:
#        # my_dict[i] = my_dict[i] + 1
#        my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# print(f"'String  Sky' as {my_dict} times'\n")
#
# # output in a key value pair one below the other.
# for key, value in my_dict.items():
#     print(f"{key}: {value} times")

# 1. Program to find the smallest number in a given list.
# list1 = [1,2,3,4,4,5,5,6,6]
# min_val =min(list1)
# print(min_val)

# # 2. Write a program to print a specified list after removing [0],[4]&[5] elements.

# my_list = ["red", "green", "white", "black", "pink", "yellow"]
# new_list = my_list.pop(4)
# del my_list[4:6]
# del my_list[0]
# print(my_list)
# print(new_list) # What pop function dose.

# # 3. Write a python program to append a list to the second list
#
# first_list = [1, 2, 3, 4, 5]
# second_list = [6, 7, 8, 9, 10]
# first_list.append(second_list)
# print(first_list)

# # 4. Write a python program to extend a list to the second list
# first_list = [1, 2, 3, 4, 5]
# second_list = [6, 7, 8, 9, 10]
# first_list.extend(second_list)
# print(first_list)

# # 5. write a python program to get unique values from a list

# my_list = [1,2,3,4,5,4,5,4,3,5,6,7,8,6,4]
# my_set = set(my_list)
# unique_list = list(my_set)
# print(unique_list)

# # 6. write a python program to get the frequency of elements in a list
#
# my_list = [1, 2, 1, 3, 2, 1, 3, 1, 2 ,'a' ,'a','b']
# my_dict = {}
#
# for i in my_list:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# print(my_dict)
# for key, value in my_dict.items():
#     print(f"{key}: {value} times")

# # 7. write a program to select odd numbers from a list
#
# m_list = [1,2,3,4,5,6,7,5,4,6,8]
# count_odd = 0
# count_even = 0
# odd_num =[]
# even_num =[]
# for i in m_list:
#     if i % 2 != 0:
#         odd_num.append(i)
#         count_odd += 1
#     else:
#         even_num.append(i)
#         count_even +=1
# print(odd_num)
# print(even_num)
# print(count_odd)
# print(count_even)

# # 8. write a program to split a list every nth element [4]
#
# my_list = [2, 3, 5, 7, 6, 8, 9, 2, 1, 2, 3, 5, 7, 6, 8, 9, 2, 1, 2, 3, 5, 7, 6, 8, 9, 2, 1]
#
#
# inp_val =int(input('Please enter how many digit the split need to happen = '))
# new_list =[]
#
# while True:
#    if len(my_list) <= 0:
#     break
#    else:
#     new_list.append(my_list[0:inp_val])
#     del my_list[0:inp_val]
# print(new_list)

# # 9. write a python program to concatenate 2 lists, and store the value in list 1 and remove duplicates and print in assending order
#
# my_list1 = [2, 3, 5, 7, 6, 8, 9, 2, 1]
# my_list2 = [7, 8, 9, 11, 7, 9, 0, 12, 41]
#
# my_list1.extend(my_list2)
# print(sorted(list(set(my_list1)),reverse=True))

# # 10. write a python program to find the difference between two lists.
#
# my_list1 = [2, 3, 5, 7, 6, 8, 9, 2, 1]
# my_list2 = [7, 8, 9, 11, 7, 9, 0, 12, 41]
# list3 = set(my_list1) ^ set(my_list2)
# print(list(list3))

# # 11. write a python program to find the prime numbers from a given list
# # **********************************************************************
# my_list= [5, 3, 6, 8, 35, 2, 9, 7, 11, 13, 17]
#
# max_num = max(my_list)
# for i in range(0, max_num):
#     if my_list[i] % 2 == 0 or my_list

# # 12. write a python script to add a key value to a dict
# my_dict ={'age': 16 ,'name': 'logi'}
# my_dict['lname'] = 'Kasi'
# my_dict['H.num'] = 9
# my_dict.update({'area':'reading'})
# print(my_dict)

# # 13. write a python script to concatenate 3 dictionaries
# my_dict1 = {"name": "Devi", "age": 39}
# my_dict2 = {"place": "Reading", "Country": "UK"}
# my_dict3 = {"Skills": "Data", "Work": "Data Engineer"}
# #new_dict = my_dict1 | my_dict2 | my_dict3
# #print(new_dict)
# news_dict = {}
#
# for i in (my_dict1,my_dict2,my_dict3):
#     news_dict.update(i)
# print(news_dict)


# # 14. write a python script to generate and print a dictionary that contains a number between 1 and n in the form of x,x2
#
# m_dic = {}
# inp_dic =int(input('Give the input for the creating a dictionary = '))
# for i in range(1,inp_dic):
#     m_dic.update({i :i*i})
# print(m_dic)

# # 15. write a python program to sort a given dictionary by key
#
# my_dict ={'age': 16,'name': 'logi','area': 'early'}
# sorted_dict = dict(sorted(my_dict.items()))
# print(sorted_dict)

# # 16. write a program to get the max and min values and key from a dic
#
# my_dict = {'banana': 3, 'apple': 2, 'orange': 5, 'mango': 1}
# # print(min(my_dict.values()))
# # print(max(my_dict.values()))
#
# min_key = min(my_dict,key = my_dict.get)
# min_val = my_dict[min_key]
# #print(f'The minimum value of the dict {min_key,':',min_val}')
# print(f'The Minimum value of the dict = {min_key} : {min_val}')
#
# max_key = max(my_dict,key=my_dict.get)
# max_val = my_dict[max_key]
# print(f'The Maximum value of the dict = {max_key} : {max_val}')


# # 17. write a python program to create a dictionary from a string and
# # track the count of letters from the string
# new_dic ={}
# str_di = ('I love india man')
# for i in str_di:
#     if i in new_dic:
#         new_dic[i] += 1
#     else:
#         new_dic[i] = 1
# print(new_dic)

# # 18. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# # If the string length is less than 2, return the empty string instead.
# # Sample String : 'w3resource'
# # Expected Result : 'w3ce'
# # Sample String : 'w3w'
# # Expected Result : 'w3w3'
# # Sample String : 'w3'
# # Expected Result : 'w3w3'
# new_str = ''
# given = 'Theworldisgreat'
# str_len = len(given)
#
# if str_len < 2:
#     print('the give string is less than 2 =''')
# else:
#     f_str = given[0:2]
#     l_str = given[-2:]
# print(f_str + l_str)
# print(str_len)


# # 19. Write a Python program to get a single string from two given strings,
# # separated by a space and interchange the first and second string,
# # swap the first two characters of each string.
# # Sample String : 'abc', 'xyz'
# # Expected Result : 'xyc abz'
#
# inp_str1 = input('Give the first string = ')
# inp_str2 = input('Give the first string = ')
#
# print(inp_str2[0:2]+inp_str1[2:],inp_str1[0:2]+inp_str2[2:])

# # 20. Write a Python program to get a string from a given string
# # where all occurrences of its first char have been changed to '$', except the first char itself.
# # Sample String : 'restart'
# # Expected Result : 'resta$t'
#
# str_i = input('Input the string to change the first char second = ')
# var0 =str_i[0]
# var1 = str_i.replace(var0 ,'$')
# print(var0 +var1[1:])

# # 21. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# # If the given string already ends with 'ing', add 'ly' instead.
# # If the string length of the given string is less than 3,
# # leave it unchanged.
# # Sample String : 'abc'
# # Expected Result : 'abcing'
# # Sample String : 'string'
# # Expected Result : 'stringly'
#
# str_1 = input('input a string for formating = ')
# len_str = len(str_1)
# if len_str < 3:
#     print("This string is too short.")
# elif str_1[-3:] == "ing":
#     print(f'The value is {str_1}ly')
# else:
#     print(f'The value is {str_1}ing')

# # 23. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# # Sample Output:
# # Longest word: Exercises
# # Length of the longest word: 9

# list_1 = ["Devi","Subash","Logesh","Nithya","Snithik"]
#
# print(max(list_1,key=len))
# print(len(max(list_1,key=len)))

# # 24. Write a Python program to count the occurrences of each word in a given sentence.
# new_list =[]
# dic_1 ={}
# my_string = "This is my house. I love my house. I live in my house."
# new_list =my_string.split(' ')
# print(new_list)
# for i in new_list:
#     if i in dic_1:
#         dic_1[i] += 1
#     else:
#         dic_1[i] = 1
# print(f'{dic_1}')#
#
# for key ,value in dic_1.items():
#     print(key ,':',value)

# 24.1 split the char in string.
# string = "hello this is logesh"
# l1 =[]
# char_list = list((string).replace(' ',''))
# #char_list = list((string))
# for i in char_list:
#     l1.append(i)
#     print(l1)
# print(char_list)

# # find the vowels  in a string.
#
# str_1 = input('please enter a sting to find the vowels in it = ')
#
# def value(string):
#     # vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
#     found_V =[]
#     for car in string:
#         if car in string:
#             found_V.append(car)
#     return found_V
#
# final = value(str_1)
# print(final)
# l1 ={}
# for i in final:
#     if i in l1:
#         l1[i] +=1
#         print('yes')
#     else:
#         l1[i] = 1
#         print('no')
# print(l1)

# #24.2 find the vowels  in a string.
# def find_vowel(insert_string):
#     vowel ='aeiouAEIOU'
#     find_vowel =[char for char in insert_string if char in vowel]
#     return find_vowel
#
# input_str ='hello logesh'
# vowel = find_vowel(input_str)
# print(f'vowel in the string are {vowel}')


#24.3  write a python program for the Math FUnction
# def math(val1,val2):
#     #val1 = int(input('enter the 1st value for operation'))
#     #val2 = int(input('enter the 2st value for operation'))
#     mult_val = val1 * val2
#     return mult_val
#
# new = math(6,5)
# print(new)
##################################################################

# def v(inp):
#     v ='aeiouAEIOU'
#     #inp =inp.casefold()
#     find_v =[val for val in inp if val in v]
#     #find_v = [val for val in inp if val in inp]
#     return find_v
#
# inp = input('enter a string to fine Vowel in that - ')
# final =v(inp)
# if final:
#     print(f'The Vowel in the given string is ',final)
# else:
#     print(f'no Vowel in the given string is ')

#
# #occurances
# dir ={}
# for i in final:
#     if i in dir:
#         dir[i] += 1
#     else:
#         dir[i] = 1
# print(dir)
#
# for key ,value in dir.items():
#     print(key ,':', value)

# write a program to find the palindrome in the given sting.

#
# inp_str = input('enter a word to find if it is palindrome = ')
# rev_str = inp_str[:: -1]
# if rev_str != inp_str:
#     print(f'The given word {'\033[1m'} {inp_str} is not a palindrome')
# else:
#     print(f'The given word {inp_str} is a palindrome')

#check_str

# li =[1,2,3,4,5,'aa','bcgd']
# li.remove(3)
# print(li)
# n=li.pop(1)
# print(n)
# print(li)
# del li[1]
# print(li)

# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1

#how do you find the first non-repeating character in a string?
# def first_non_repeating_char(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     for char in s:
#         if char_count[char] == 1:
#             return char
#     return None

# Example
#print(first_non_repeating_char("swiss"))

inp = [1,2,3,4,5,6,7,8,9,10]
even =[]
for i in inp:
  if i % 2 == 0:
    even.append(i)
print(sum(even))
  # else:
  #   sum[i] = 1

  # else:
  #    count +=i

# Employees (EmployeeID, Name, DepartmentID) -sql
#select * from employees where name ='gorge'

def sumvalue(number):
    sum_even = sum([val for val in number if val % 2 == 0])
    return sum_even
num = (1,2,3,4,5,6,7,8,9,10)
print(sumvalue(num))


num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum_even = sum([val for val in num if val % 2 == 0])
print(sum_even)