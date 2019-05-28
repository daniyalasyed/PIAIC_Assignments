## Write a Python program to get a new string from a given string where 
## "Is" has been added to the front. If the given string already begins 
## with "Is" then return the string unchanged.

string = input("Type anything:\t")

front = "Is"

if string[0:2] == front:
	print (string)
else:
	print (front + " " + string) 
