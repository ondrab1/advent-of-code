from collections import defaultdict

line = open("input.txt").read()

data = [int(x) for x in line.split(',')]
data = {x: data.count(x) for x in set(data)}

total_days = 256

for day in range(total_days):
    new_data = defaultdict(int)
    for num, count in data.items():
        if num == 0:
            num = 7
            new_data[8] += count

        new_data[num - 1] += count

    data = new_data

print(sum(data.values()))
