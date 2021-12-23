lines = open("input.txt").read().splitlines()

data = {y: {x: int(value) for x, value in enumerate(item)} for y, item in enumerate(lines)}


def get_basin(value, coords, data):
    basin = {}
    points = {coords: value}

    while points:
        for point, value in list(points.items()):
            x, y = point

            basin[point] = value
            points.pop(point)

            # to left
            for ix in range(x - 1, -1, -1):
                if data[y][ix] == 9 or (ix, y) in basin:
                    break

                points[(ix, y)] = data[y][ix]

            # to right
            for ix in range(x + 1, len(data[0])):
                if data[y][ix] == 9 or (ix, y) in basin:
                    break

                points[(ix, y)] = data[y][ix]

            # up
            for iy in range(y - 1, -1, -1):
                if data[iy][x] == 9 or (x, iy) in basin:
                    break

                points[(x, iy)] = data[iy][x]

            # down
            for iy in range(y + 1, len(data)):
                if data[iy][x] == 9 or (x, iy) in basin:
                    break

                points[(x, iy)] = data[iy][x]

    return basin


low_points = {}
for y, row in data.items():
    for x, value in row.items():
        valid_value = True
        for i in [1, -1]:
            if (y + i) in data and not (data[y + i][x] > value):
                valid_value = False

            if (x + i) in data[y] and not (data[y][x + i] > value):
                valid_value = False

        if valid_value:
            low_points[(x, y)] = value

basin_sizes = []
for coords, value in low_points.items():
    basin = get_basin(value, coords, data)
    basin_sizes.append(len(basin))

largest_basins = sorted(basin_sizes, reverse=True)[:3]

result = 1
for value in largest_basins:
    result *= value

print(result)
