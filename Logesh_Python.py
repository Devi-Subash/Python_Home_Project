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
'''
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