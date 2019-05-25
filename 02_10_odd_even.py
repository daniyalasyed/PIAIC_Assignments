## Write a Python program to find whether a given number (from 
## the user) is even or odd, print out an appropriate message to the user.

print ('''
Let me help you find out if your number is Even or Odd.
''')

n = int(input("What is the number?\t"))

if n%2 == 0:
	print ('''
	The number ''' + str(n) +''' is EVEN.''')
else:
	print ('''
	The number ''' + str(n) +''' is ODD.''')
