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

