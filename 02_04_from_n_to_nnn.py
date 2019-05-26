## Write a Python program that accepts an integer (n) and computes the value of (n + n*n + n*n*n)

print('''
This program will take a number (n) and give back (n + n*n + n*n*n)
''')

n = int(input('Choose the value of n: '))

#print (n)
#print(n*n)
#print(n*n*n)

n1 = n
#print(n1)

n2 = n*n
#print(n2)

n3 = n*n*n
#print(n3)

print('''
Output: ''', n1+n2+n3) 
