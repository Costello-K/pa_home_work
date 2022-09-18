import math

# 1. Construct an integer from the string "123"

string = '123'
string_to_integer = int(string)
print(string_to_integer)

# 2. Construct a float from the integer 123

integer_to_float = float(string_to_integer)
print(integer_to_float)

# 3. Construct an integer from the float 12.345

float_to_integer = int(12.345)
print(float_to_integer)

# 4. Write a Python-script that detects the last 4 digits of a credit card

card_number = '1234123492349234'
last_digits = card_number[-4:]
print(last_digits)

# 5. Write a Python-script that calculates the sum of the digits of a three-digit number

number = 123
sum_digits = sum([int(i) for i in str(number)])
print(sum_digits)

# 6. Write a program that calculates and displays the area of a triangle if its sides are known

a, b, c = 9, 4, 8
p = (a + b + c)/2
area_triangle = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'{area_triangle:.2f}')

# 7. *Write a Python-script that calculates the sum of the digits of a number

number = 123456789199
sum_digits = sum([int(i) for i in str(number)])
print(sum_digits)

# 8. *Determine the number of digits in a number

number = 9567567467547123456789199
amount_digits = len(str(number))
print(amount_digits)

# 9. *Print the digits in reverse order

number = 1234567
reverse_number = int(str(number)[::-1])
print(reverse_number)
