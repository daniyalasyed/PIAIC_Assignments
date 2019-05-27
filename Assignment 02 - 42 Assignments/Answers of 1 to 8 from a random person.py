## 1.Write a Python program which accepts the radius of a circle from the user and compute the area

from math import pi

print("************Radius Of Circle*****************")
radius = float(input("Please Enter the Radius of the circle :"))
area = pi * radius ** 2
print("The Area of Circle is :%.2f"%area)

## 2.Write a Python program to check if a number is positive, negative or zero

num = int(input("Please Enter any number :"))
if num > 0:
    print("Number Is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is equal to 0")

## 3.Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user

def check_div(a,b):
    if (a/b)==1:
        print("Number is Completely divisible by 2nd number")
    else:
        print("Number is Not Completely divisible by 2nd number")

x,y = input("Please Enter two comma separated Numbers :").split(",")
x=int(x)
y=int(y)
check_div(x,y)



## 5.Write a Python program to calculate number of days between two dates

from datetime import date

st_year,st_month,st_day = input("Enter the comma separated Starting year, Month, date :").split(",") 

st_year = int(st_year)
st_month = int(st_month)
st_day = int(st_day)

start = date(st_year,st_month,st_day)

end_year,end_month,end_day = input("Enter the comma separated Ending year, Month, date :").split(",") 

end_year = int(end_year)
end_month = int(end_month)
end_day = int(end_day)

end = date(end_year,end_month,end_day)

days = (end-start).days

print(days)

## 6.Write a Python program to get the volume of a sphere, please take the radius as input from user. V=4 / 3 πr3

from math import pi
print("************Volume Of Sphere*****************")
radius = float(input("Please Enter the Radius of the Sphere :"))
volume = (4/3)*pi*radius**3
print("The Volume of Sphere is :%.2f"%volume)

## 7.Write a Python program to get the difference between a given number and 17, difference cannot be negative

fixed_num = 17
num = int(input("Please Enter any number :"))
difference = 17-num
difference = abs(difference)
print(f"Difference is {difference}")

## 8.Write a Python program to get a new string from a given string where "Is" has been added to the front. If the
 given string already begins with "Is" then return the string unchanged

string = input("Please Enter any String \n")
fix = "Is"
first_two_letters = string[0:2]
first_two_letters = first_two_letters.title()
if string == "":
    print("You have'nt input any thing!...Please Try again")
elif fix == first_two_letters:
    print(f"The unchanged string is \"{string}\"")
else:
    print("The changed string is \""+fix + " " +string+"\"")

