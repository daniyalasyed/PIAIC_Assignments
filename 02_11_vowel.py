## Write a Python program to test whether a passed letter is a vowel or not.

print('''
This program will tell you whether a specific alphabet is an alphabet or not.''')

alph = input("Give me an alphabet:\t").lower()

if alph == "a":
	print ("\n The alphabet A is a vowel.")
elif alph == "e":
	print ("\n The alphabet E is a vowel.")
elif alph == "i":
	print ("\n The alphabet I is a vowel.")
elif alph == "o":
	print ("\n The alphabet O is a vowel.")
elif alph == "u":
	print ("\n The alphabet U is a vowel.")
else:
	print ("\n Your input is not a vowel.")
