import os

file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')

rules = {}
data = []


def correct_line(line):
    swapped = False
    i = 0
    while i < len(line):
        if line[i] in rules:
            current_rule = rules[line[i]]
            for j in range(i, len(line)):
                if line[j] in current_rule:
                    swapped = True
                    line[i], line[j] = line[j], line[i]
                    i = -1
                    break
        i+= 1

    if swapped:
        return int(line[len(line)//2])
    return 0

data_parsed = False
for line in file:
    if line == '\n':
        data_parsed = True
        continue
    if not data_parsed:
        if line[3:5] not in rules:
            rules[line[3:5]] = [line[:2]]
        else:
            rules[line[3:5]].append(line[:2])
    else:
        data.append(line.strip().split(','))

result = 0

for input in data:
    result += correct_line(input)

print(result)
