print('''
This program checks if the number you input is a prime or not.

Please note that if you enter a decimal number it will be truncated to the nearest integer.
''')

num = float(input('Enter any number:\t'))

print('\n')

if num < 0:
    print ('Negative numbers are not prime numbers.')
else:
    num = int(num)
    if num == 0:
        print ('0 is neither a composite nor a prime number.')
    elif num == 1:
        print ('1 is neither a composite nor a prime number.')
    else:
        count = 0
        for n in range(2, num):
            
            if num % n == 0:
                count = count + 1
            
        if count == 0:
            print("This is a prime number")
        else:
            print("This is not a prime number")