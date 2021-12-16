from collections import defaultdict

lines = open("input.txt").read().splitlines()

data = [tuple(tuple(int(z.strip()) for z in y.split(',')) for y in x.split('->')) for x in lines]

diagram = defaultdict(int)

for (point1, point2) in data:
    x1, y1 = point1
    x2, y2 = point2

    get_step = lambda point: 0 if point[0] == point[1] else (point[1] - point[0]) / abs(point[1] - point[0])
    distance = max(abs(x2 - x1), abs(y2 - y1))

    x_step = get_step((x1, x2))
    y_step = get_step((y1, y2))

    for i in range(distance + 1):
        x = int(x1 + i * x_step)
        y = int(y1 + i * y_step)

        diagram[(x, y)] += 1

overlaps = 0
for point in diagram.values():
    if point > 1:
        overlaps += 1

print(overlaps)
