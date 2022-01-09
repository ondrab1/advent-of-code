import re
import math

lines = open('input.txt').read().splitlines()

paper = {}
folds = []

for line in lines:
    match = re.search('fold along (.*)=(.*)', line)
    if match:
        axis, point = match.groups()
        folds.append((axis, int(point)))
        continue
    elif line == '':
        continue

    x, y = [int(i) for i in line.split(',')]

    paper[(x, y)] = 1

# take only first fold
folds = [folds[0]]
for axis, point in folds:
    if axis == 'y':
        position = 1
    else:
        position = 0

    max_value = max(paper.keys(), key=lambda item: item[position])[position]
    decrease = math.floor(max_value / point) * point

    for x, y in paper.copy().keys():
        if axis == 'y':
            if y < point:
                continue

            new_x = x
            new_y = abs(y - decrease)
        else:
            if x < point:
                continue

            new_x = abs(x - decrease)
            new_y = y

        paper[(new_x, new_y)] = 1

        del paper[(x, y)]

print(sum(paper.values()))
