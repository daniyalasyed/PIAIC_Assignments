## Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
## n1 = dividend
## n2 = divisor 

print('''
This program will tell you whether your a number is completely divisible by another.
''')

n1 = float(input('Which number do you wanna divide? '))
n2 = float(input('Which number you want to divide it by? '))
rem = n1%n2

if rem == 0:
	print('''
	YES, ''' + str(n1) + ''' is completely divisible by ''' + str(n2) + '''.''')
else:
	print('''
	NO, ''' + str(n1) + ''' is NOT completely divisible by ''' + str(n2) + '''.''')
