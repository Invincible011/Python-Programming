print('Exercise 2 solution')
name = input('Enter your name? ')
print('Hello', name)
print()

print('Exercise 3 solution')
hours = int(input('Enter hours? '))
rate = float(input('Enter rate? '))
pay = float(input('Enter pay? '))
gross_pay = hours * rate * pay
print('gross_pay =', gross_pay)
print()

print('Exercise 4 solution')
width = 17
height = 12.0

print('Width =', width // 2)
print(type(width // 2))

print('Width 2 =', width / 2)
print(type(width / 2))

print('height =', height / 3)
print(type(height / 3))

print('1 + 2 * 5 =', 1 + 2 * 5)
print(type(1 + 2 * 5))
print()

print('Exercise 5 solution')
# Formular = (1.8 * C) + 32 or
# Formular = (9/5 * C) + 32
print('Convert Temperature to Fahrenheit')
c = float(input('Enter degree in Celsius: '))
f = (1.8 * c) + 32
print('Converted temperature in Fahrenheit =', f)

import init