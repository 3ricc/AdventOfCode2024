import os

def check_safe(data):
    num1 = int(data[0])
    num2 = int(data[1])
    safe = True
    if abs(num1 - num2) > 3:
        return False
    if num1 > num2:
        for i in range(1, len(data)-1):
            if int(data[i]) < int(data[i+1]):
                safe = False
            if abs(int(data[i]) - int(data[i+1])) > 3 or abs(int(data[i]) - int(data[i+1])) < 1:
                safe = False
    elif num1 < num2:
        for i in range(1, len(data)-1):
            if int(data[i]) > int(data[i+1]):
                safe = False
            if abs(int(data[i]) - int(data[i+1])) > 3 or abs(int(data[i]) - int(data[i+1])) < 1:
                safe = False
    else:
        safe=False

    return safe
    
file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
num_safe = 0

for line in file:
    data = line.split()
    
    safe = check_safe(data)
    
    if safe:
        num_safe+=1
    else:
        for i in range(len(data)):
            new_list = data.copy()
            del new_list[i]
            safe = check_safe(new_list)
            if safe:
                num_safe+=1
                break

print(num_safe)

