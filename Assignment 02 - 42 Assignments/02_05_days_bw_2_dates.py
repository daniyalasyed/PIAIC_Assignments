## Write a Python program to calculate number of days between two dates

from datetime import date

print('''
This program will input two dates and output the number of days between them.

First, please enter the Year, Month, and Day number of the 1st date below.
''')

y1 = int(input ("Enter ONLY the Year of the 1st date:\t"))
print("\n")
m1 = int(input ("Enter ONLY the Month NUMBER of the 1st date:\t"))
print("\n")
d1 = int(input ("Enter ONLY the Day number of the 1st date:\t"))

bgn = date(y1, m1, d1)

print ('''
Now, you will enter the 2nd date's details below.
''')

y2 = int(input ("Enter ONLY the Year of the 2nd date:\t"))
print("\n")
m2= int(input ("Enter ONLY the Month NUMBER of the 2nd date:\t"))
print("\n")
d2 = int(input ("Enter ONLY the Day number of the 2nd date:\t"))

end = date(y2, m2, d2)

diff = (end-bgn).days

print ('''
The difference between the two dates is ''' + str(diff) + ''' days.
''')
