import math
import statistics

line = open("input.txt").read()
data = [int(x) for x in line.split(',')]

new_position = math.floor(statistics.mean(data))

total_fuel = 0


def get_used_fuel(n):
    fuel = 0
    for i in range(n):
        fuel += (1 + i)

    return fuel


for position in data:
    diff = abs(position - new_position)
    total_fuel += get_used_fuel(diff)

print(total_fuel)
