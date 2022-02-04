lines = open('input.txt').read().splitlines()

cucumbers_map = {}
for y, line in enumerate(lines):
    for x, value in enumerate(line):
        cucumbers_map[(x, y)] = None if value == '.' else value

max_x = max(cucumbers_map, key=lambda item: item[0])[0]
max_y = max(cucumbers_map, key=lambda item: item[1])[1]

step = 0
while True:
    moves = 0

    next_map = cucumbers_map.copy()

    # east move first
    easts = {k: v for k, v in cucumbers_map.items() if v == '>'}
    for (x, y), value in easts.items():
        next_position = (0 if (x + 1) > max_x else (x + 1), y)
        if next_position in cucumbers_map and cucumbers_map[next_position] is None:
            next_map[(x, y)] = None
            next_map[next_position] = value
            moves += 1

    cucumbers_map = next_map.copy()

    # then south should move
    souths = {k: v for k, v in cucumbers_map.items() if v == 'v'}
    for (x, y), value in souths.items():
        next_position = (x, 0 if (y + 1) > max_y else (y + 1))
        if next_position in cucumbers_map and cucumbers_map[next_position] is None:
            next_map[(x, y)] = None
            next_map[next_position] = value
            moves += 1

    cucumbers_map = next_map

    step += 1

    if moves == 0:
        break

print(step)
