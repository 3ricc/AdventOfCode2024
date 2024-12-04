import os

file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')

directions=[
    (-1, 1),
    (-1, -1),
    (1, 1),
    (1, -1),
]

def find_word(data, y, x):
    if x < 0 or y < 0 or y >= len(data) - 1 or x >= len(data[0]) - 1:
        return 0
    if data[y-1][x-1] == data[y-1][x+1] and (data[y-1][x-1] == 'M' or data[y-1][x-1] == 'S'):
        if data[y+1][x-1] == data[y+1][x+1] and (data[y+1][x-1] == 'M' or data[y+1][x-1] == 'S') and data[y+1][x-1] != data[y-1][x-1]:
            return 1
    elif data[y-1][x-1] == data[y+1][x-1] and (data[y-1][x-1] == 'M' or data[y-1][x-1] == 'S'):
        if data[y-1][x+1] == data[y+1][x+1] and (data[y-1][x+1] == 'M' or data[y-1][x+1] == 'S') and data[y-1][x+1] != data[y-1][x-1]:
            return 1
    return 0


occurences = 0

find = [['M','.','S'],
        ['.','A','.'],
        ['M','.','S'],]
word_search = []
for line in file:
    word_search.append(list(line.strip()))

for i in range(len(word_search)):
    for j in range(len(word_search[0])):
        if word_search[i][j] == 'A':
            occurences += find_word(word_search, i, j)

print(occurences)

