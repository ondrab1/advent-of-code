import re

lines = open("input.txt").read().splitlines()

x = 0
y = 0
aim = 0

for line in lines:
    match = re.search('(\S+)\s+(\d)', line)
    direction, value = match.groups()

    value = int(value)

    if direction == 'forward':
        x += value
        y += value * aim
    elif direction == 'up':
        # y -= value
        aim -= value
    elif direction == 'down':
        # y += value
        aim += value

print(x * y)
