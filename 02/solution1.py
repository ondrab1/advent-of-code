import re

lines = open("input.txt").read().splitlines()

x = 0
y = 0

for line in lines:
    match = re.search('(\S+)\s+(\d)', line)
    direction, value = match.groups()

    value = int(value)

    if direction == 'forward':
        x += value
    elif direction == 'up':
        y -= value
    elif direction == 'down':
        y += value

print(x * y)
