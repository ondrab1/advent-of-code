lines = open("input.txt").read().splitlines()

data = {y: {x: int(value) for x, value in enumerate(item)} for y, item in enumerate(lines)}

low_points = []
for y, row in data.items():
    for x, value in row.items():
        valid_value = True
        for i in [1, -1]:
            if (y + i) in data and not (data[y + i][x] > value):
                valid_value = False

            if (x + i) in data[y] and not (data[y][x + i] > value):
                valid_value = False

        if valid_value:
            low_points.append(value)

result = 0
for point in low_points:
    result += (point + 1)

print(result)
