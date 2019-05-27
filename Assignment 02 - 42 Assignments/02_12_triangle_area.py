## Write a Python program that will accept the base and height of a 
## triangle and compute the area.

print('''
This program will take inputs of base and heigh of a triangle and output the area.''')

b = float(input("Base?\t"))
print("\n")
h = float(input("Height?\t"))

Area = (b*h)/2

print ('''The Area is ''' + str(Area) + '''.''')
