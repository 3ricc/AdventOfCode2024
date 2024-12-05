import os

file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')

rules = {}
data = []

def check_line(line, index):
    rule = rules[line[index]]
    for i in range(index, len(line)):
        if line[i] in rule:
            return False
    return True


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
    line_valid = True
    for i in range(len(input)):
        if input[i] in rules:
            line_valid = check_line(input, i)
            if not line_valid:
                break

    if line_valid:
        result += int(input[len(input)//2])

print(result)
