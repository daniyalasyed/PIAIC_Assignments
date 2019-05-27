## Write a Python program to get a string which is n (non-negative integer) copies of a given string

print ('''
This program inputs one string and gives you n copies of it as output.
You can define the number n too.
''')

string = input("Type anything:\t") + "\n"

n = abs(int(input('''
And how many copies do you want? 
Enter only positive numbers. 
Negative numbers will be converted to positive numbers.\t
''')))

print (string * n)
