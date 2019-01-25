'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number.'''

a = int(input("Please enter the number: "))
for i in range(1,a+1):
    y = a%i
    if y == 0:
        print(i)
