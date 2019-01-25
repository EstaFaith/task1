''' Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. '''

a = int(input("Input the number: "))
if(a%2 == 0):
    print("The number is EVEN")
else:
    print("The number is ODD")
