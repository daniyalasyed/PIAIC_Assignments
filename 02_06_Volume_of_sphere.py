## Write a Python program to get the volume of a sphere, please take the radius as input from user. V=4 / 3 πr3
from math import pi
print('''
This program will give you the Volume of a sphere from its radius
''')

r = float(input ('Please enter radius: '))

vol = (4/3)*pi*(r**3)

print('''
Volume of the sphere = ''', vol)
