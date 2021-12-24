flashes = 0


def update_adjacent_values(x, y, data):
    global flashes

    if data[y][x] != 10:
        data[y][x] += 1

    if data[y][x] > 9:
        data[y][x] = 0
        flashes += 1

        for x_increment, y_increment in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + x_increment, y + y_increment

            if ny in data and nx in data[ny]:
                if data[ny][nx] != 0 and data[ny][nx] != 10:
                    data = update_adjacent_values(nx, ny, data)

    return data


lines = open("input.txt").read().splitlines()
lines = {i: {i2: int(x2) for i2, x2 in enumerate(x)} for i, x in enumerate(lines)}

step = 0
values_sum = None
while values_sum != 0:
    for y, row in list(lines.items()):
        for x, value in row.items():
            lines[y][x] += 1

    for y, row in list(lines.items()):
        for x, value in row.items():
            if value > 9:
                update_adjacent_values(x, y, lines)

    values_sum = 0
    for line in lines.values():
        values_sum += sum(line.values())

    step += 1

print(step)
