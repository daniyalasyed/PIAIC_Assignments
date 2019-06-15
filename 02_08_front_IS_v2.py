## Write a Python program to get a new string from a given string where 
## "Is" has been added to the front. If the given string already begins 
## with "Is" then return the string unchanged.

import re

string = input("Type anything:\t").title()

# ## this is a test string I used to check my code repeatedly after every edit
# string = "Is my hoodie at your house or is it at school?".title()
# print(string)

print("\n")

search_term = "Is "
# search_term = search_term.title()

## this checks whether the search_term is in the string or not
s = re.search(search_term, string)

## this says that if the search term is in the string, then do as follows
if (s):
	## this checks whether the search_term is in the beginning of the string
	if s.start() == 0:
		print(string)
	else:
		## this states that if the search_term is not in the beginning, then put one copy there there and display it
		print(search_term + string)
else:
	## this states that if the search_term is no where to be found in the string, then put it in the beginning and display it
	print(search_term + string)








## Below are a few test runs I had to check to understand how Regex works
## ----------------------------------------------------------------------------------------------------

# ## to check if the search_term is in the string and if it is, then where is it's first instance located
# print("FOR SEARCH")

# s = re.search(search_term, string)
# print(s)

# if (s):
  # print("YES! We have a match!")
  # print("The first instance of the required search-term is located in the position: ", s.start())
# else:
  # print("No match")

# print("\n")

# ## to check how many search_terms are in the string
# print("FOR FINDALL")

# f = re.findall(search_term, string)
# print(f)

# if (f):
  # print("Yes, there is at least one match!")
# else:
  # print("No match")

# print("\n")

# ## the split functions returns a list where the string has been split at each match
# print("FOR SPLIT")

# p = re.split(search_term, string)
# print(p)

# ## You can control the number of occurrences by specifying the "maxsplit" parameter
# p = re.split(search_term, string, 1)
# print(p)

# print("\n")

# ## The sub() function replaces the matches with the text of your choice
# print("FOR SUB")
# sub = "__ "

# b = re.sub(search_term, sub, string)
# print(b)

# ## You can control the number of replacements by specifying the count parameter
# b = re.sub(search_term, sub, string, 1)
# print(b)

# print("\n")

# ## all of this was learned from https://www.w3schools.com/python/python_regex.asp
