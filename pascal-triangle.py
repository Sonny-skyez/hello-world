'''
Pascal triangle - and proper code to print it.

Written: 12.11.2018
Author: Chris Brymer
'''

width = 50
height = 10
numbers = [1]
line = ''

for n in numbers:
    line += '%3d ' % (n)
print(line.center(width))

for i in range(height-1):
    newNumbers = [1]
    position = 0
    while position < len(numbers)-1:
        newNumbers.append(numbers[position] + numbers[position+1])
        position += 1

    newNumbers.append(1)
    numbers = newNumbers.copy()
    line = ''
    for n in numbers:
        line += '%3d ' % (n)
        
    print(line.center(width))
