import statistics

line = open("input.txt").read()
data = [int(x) for x in line.split(',')]

new_position = statistics.median_low(data)

total_fuel = 0

for position in data:
    total_fuel += abs(position - new_position)

print(total_fuel)
