# 1. Write a Python program to print the number entered by user only if the
# number entered is negative.

x = int(input('Enter number'))
print(x < 0 and x or '')

# 2. Write a Python program to check if the value a is less than 20 or not.

y = int(input('Enter number'))
print(f'Value{y < 20 and " " or " not "}less than 20')

# 3. Write a Python program to check if a given number is Zero or Not.

z = int(input('Enter number'))
print(f'Given number is{z and " not" or ""} Zero')

# 4. Write a Python program to check if a given number is Even or Odd.

w = int(input('Enter number'))
print(f'Given number is {w % 2 and "Odd" or "Ewen"}')

# 5. Write a Python program to find largest number among three numbers entered by user.

a = int(input('Enter first number'))
b = int(input('Enter second number'))
c = int(input('Enter third number'))
print(f'Largest number = {max(a, b, c)}')
