import os

file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')

list1 = []
list2 = []
for line in file:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

simularity = 0
for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            simularity += num1

print(simularity)
