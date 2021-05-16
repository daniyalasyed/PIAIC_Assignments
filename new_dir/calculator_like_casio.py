'''
I coded this whole thing during class trying to figure out how to make a program 
that behaves like a Casio calculator
'''

def arithmetic_operations(operand1, operand2, operator = "+"):
    if operator == '+':
        print(operand2 + operand1)
    if operator == '*':
        print(operand2 * operand1)
    if operator == '-':
        print(operand2 - operand1)
    if operator == '/':
        print(operand2/operand1)
    if operator == '%':
        print(operand2%operand1)

arithmetic_operations(1, 2, "/") #this executes the function

#c = "45+69"
#
#print(c[0:2])
#
#print(c[3:])
#
#for i in range(len(c)):
#    print(c[i])
#    if c[i] == "+":
#        arithmetic_operations( int(c[0:2]), int(c[3:]), "+")
#        break
    

print('''
Tell this program to execute a simple one-operand calculation involving
+ plus
- minus
* multiply
/ divide, or
% modulus(for remainder)
''')

c = input('''Calculate:\t''')

for i in range(len(c)):
    for operand in ['+', '-', '*', '/', '%']:
        if c[i] == operand:
            arithmetic_operations(int(c[i+1:]), int(c[:i]), operand)
