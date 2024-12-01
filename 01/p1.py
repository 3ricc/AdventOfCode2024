file = open('C:/Users/Epic1/OneDrive/Documents/Repo/AdventOfCode/01/data.txt','r')

list1 = []
list2 = []
for line in file:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

# im a lazy ass mf
list1.sort()
list2.sort()

answer = 0
for i in range(len(list1)):
    answer += abs(list1[i] - list2[i])

print(answer)