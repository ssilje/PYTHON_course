print("This line will be printed.")

# hashmarks are comments in Python

print("Type a line and execute the cell")

print()

a = 'A string '
b = 'and another string'
print(a + b + ' are concatenated by "+."')

print()

multiline_string = """You can create multiline strings by
enclosing them in three consecutive
quotes
"""

print(multiline_string)



list_a = [1, 2, 3]

list_b = ['a', 'b', 2.3]

print("Lists can also be concatenated with '+': \nlist_a + list_b =", list_a + list_b)

print()

print("Python 0-based!")

print('Select first element:', list_a[0])
print('Select list of lenght one:', list_a[0:1])


#print(0)
#print(1)
print(2)
print(3)
print(4)
print(5)

print("Python loops through everything that is iterable:")

for element in list_b:
    print(element)
    
print()

string = 'Almost everything is iterable'

for i in string:
    print(i, end=' ')

print()
print()
print('new exercise')
print()

# end=' ' prints a space instead of a newline ('\n')


list_a = [1, 2, 3]
for numbers in list_a:
    print(numbers)

print()

string = 'I am printing the numbers' 

for i in string:
    print(i, end=' ')

print()


print()
print()
print('new exercise')
print()

for i, el in enumerate(list_b):
    print('index:', i, 'element:', el)


print()
print('doing the same with list_a')
print()


for i, el in enumerate(list_a):
    print('index:', i, 'element:', el)

print()
print('importing libraries')
print()


import numpy as np

a = np.array([[1, 2], [3, 4]])
np.mean(a)

np.mean(a, axis=0)
#    array([ 2.,  3.])
#np.mean(a, axis=1)
#    array([ 1.5,  3.5])

print(a)
print()
print()


print('still using the library np')
print()

#np.arange creates evenly spaced values within a given interval
test = np.arange(10)

print(test)

#This created an array with 10 elements. Notice how it starts at 0 and ends at 
test2 = np.arange(10).shape
print(test2)



string = 'syntax for the function np'

for i in string:
    print(i, end=' ')

print()


string= 'aa = np.arange(stop)'
for i in string:
    print(i, end=' ')

print()


string= 'ab = np.arange(start, stop)'

for i in string:
    print(i, end=' ')

print()



string= 'ac = np.arange(start, stop, step)'
for i in string:
    print(i, end=' ')

print()



print('Create an array with elements from 1 to 12')

solution = np.arange(1,13)
print(solution) 



print('create a array from 0 to 5 in steps of 0.5')
solution = np.arange(0,5.5,0.5)
print()

print('solution = np.arange(0,5.5,0.5)')
print(solution)

print()
print('other ways to create an array')

# with a list
a = np.asarray([1, 2, 3])

string = 'print(a.shape)'
for i in string:
    print(i, end=' ')

print()

print(a.shape)


string= 'print(a.size)'
for i in string:
    print(i, end=' ')

print()

print(a.size)


string='print(a.ndim)'
for i in string:
    print(i, end=' ')

print()

print(a.ndim)

string='print(a.dtype)'
for i in string:
    print(i, end=' ')

print()

print(a.dtype)

a


