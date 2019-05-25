## Write a Python program to get the difference between a given number and 17, difference cannot be negative

print('''
This program will tell you how far a number is from 17.
''')

num=float(input('Give me a number. Any number: '))

if num > 17:
	diff = num -17
elif num < 17:
	diff = 17 - num
else:
	diff = 0

print('''
The difference between your chosen number and 17 is''', diff)
