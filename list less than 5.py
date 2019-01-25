
'''Take a list,and write a program that prints
out all the elements of the list that are less than 5.'''

numbers = input('Input list of numbers: ')
a = list(map(int,numbers.split()))
l = []
for i in a:
    if i <=5:
        l.append(i)
        print(l)
