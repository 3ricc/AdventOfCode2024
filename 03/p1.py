import os

file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')

def parsing(line_data, index):
    isValid = True
    j = index + 4

    test_substring = line_data[index:j]

    if test_substring != 'mul(':
        return 0

    num1char = ''
    num2char = ''
    isNum1 = True

    num1 = 0
    num2 = 0

    while isValid:
        if line_data[j].isdigit():
            if isNum1:
                num1char += line_data[j]
            else:
                num2char += line_data[j]
        elif line_data[j] == ',':
            if isNum1:
                num1 = int(num1char)
                num1char = ''
                isNum1 = False
            else:
                return 0
        elif line_data[j] == ')':
            isValid = False
            if not isNum1:
                num2 = int(num2char)
                return num1 * num2
            else:
                return 0
        else:
            return 0
        j += 1

    return 0
    # while isValid:

result = 0


for line in file:
    for i in range(len(line)):
        if line[i] == 'm':
            result += parsing(line, i)

print(result)
