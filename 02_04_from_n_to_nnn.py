## Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)

print('''
This program will take a number (n) and give back (n + nn + nnn)
''')

n = input('Choose the value of n: ')

#print (n)
#print(n + n)
#print(n + n + n)

n1 = int(n)
#print(n1)

n2 = int(n + n)
#print(n2)

n3 = int(n + n + n)
#print(n3)

print('''
Output: ''', n1+n2+n3) 
