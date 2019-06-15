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
        
        ## this is where the program really starts checking if the input number is prime or not
        count = 0
        
        for n in range(2, num):
            ## this range does not include the number itself
            
            if num % n == 0:
                count = count + 1
                ## whenever the COUNTER increases by 1 it means that the input number is divisible by a number in the range
        
        ## so if the counter is 0 then it means that the input number is not divisible by any number in the range
        if count == 0:
            print("This is a prime number")
        
        ##but if the counter is NOT 0 then it IS divisible by at least one number in the range
        else:
            print("This is NOT a prime number")