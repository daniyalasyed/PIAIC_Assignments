## Write a Python program to check if a number is positive, negative or zero

num= float(input('''Give me a number 
and I'll tell you 
whether its 
Positive, 
Negative 
or Zero: '''))

if num > 0:
	print('''
	POSITIVE''')
elif num < 0:
	print('''
	NEGATIVE''')
else:
	print('''
	ZERO''')
