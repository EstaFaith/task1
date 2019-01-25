'''Take two lists and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.'''

m = input('input list1 of numbers :')
a = list(map(int,m.split()))
n = input('input list2 of numbers :')
b = list(map(int,n.split()))
newlist = []
for element in b:
    if element in a:
        newlist.append(element)
        print(newlist)
