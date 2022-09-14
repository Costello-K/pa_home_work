'''
Exercise 1.
Write a Python-script that displays the message “Hello world
'''

print('Hell world')

'''
Exercise 2. 
Rewrite the first script to display three any messages.
'''

print('Welcome')
print('to')
print('Ukraine')

'''
Exercise 3. 
Write a Python-script to reads values for the length and width of a
rectangle and returns the area of the rectangle.
'''

length = int(input('Enter length of the rectangle'))
width = int(input('Enter width of the rectangle'))
print(f'Area of the rectangle = {length * width}')

'''
Exercise 4. 
Write a program that requests the user to enter two numbers and
prints the sum, product, difference and quotient of the two numbers.
'''

first_number = int(input('Enter first number'))
second_number = int(input('Enter second number'))

print(f'Sum = {first_number + second_number}')
print(f'Product = {first_number * second_number}')
print(f'Difference = {first_number - second_number}')
print(f'Quotient = {round(first_number / second_number, 2)}')

'''
Exercise 5. 
Write a program that reads in the radius of a circle and prints the circle’s diameter, 
circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.
'''

PI = 3.14159
radius = int(input('Enter radius of a circle'))
diameter = radius * 2
circumference = diameter * PI
area = circumference * diameter / 4

print(f'Diameter of a circle = {round(diameter, 2)}')
print(f'Circumference of a circle = {round(circumference, 2)}')
print(f'Area of a circle = {round(area, 3)}')
