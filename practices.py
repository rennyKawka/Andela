# 01 *** My practices ***

# line 19 and 20 I wanted to construt a string for the results

# 02 functions
"""
def say_hi(name):
    print("hello " + name + " " + "welcome To my page")
say_hi(input("enter your name: "))
"""

# 03 '''Finding the squares'''
"""
def square(num):
    return num*num
num = int(input('Enter a value, we calculate its Square: '))
results = square(num)
# errror
# num = square(num)
print("The square of " + str(num) + " is " + str(results))
# print(results)
"""

# 04 If '''finding the maximum value'''
"""
# case1 for maximum value;
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(394, 399, 396))
"""

# 05 '''A simpple calculator'''

num1 = int(input("Enter First number: "))
op = input("Enter operator: ")
num2 = int(input("Enter Second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Invalid operator!!!")

