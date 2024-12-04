import os

file = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')

directions = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1)
]

def find_word_recursive(data, y, x, phase, direction):
    if x < 0 or y < 0 or y >= len(data) or x >= len(data[0]):
        return 0
    if data[y][x] != find[phase]:
        return 0
    if data[y][x] == find[phase]:
        if phase == 3:
            return 1
        return find_word_recursive(data, y + direction[0], x + direction[1], phase + 1, direction)

occurences = 0

find = ['X', 'M', 'A', 'S']
word_search = []
for line in file:
    word_search.append(list(line.strip()))

for i in range(len(word_search)):
    for j in range(len(word_search[0])):
        if word_search[i][j] == 'X':
            for k in range(len(directions)):
                occurences += find_word_recursive(word_search, i, j, 0, directions[k])

print(occurences)

