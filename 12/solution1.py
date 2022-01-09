from collections import defaultdict

lines = open('input.txt').read().splitlines()

all_paths = []


def generate_paths(map, current_position='start', path=None):
    global all_paths

    if path is None:
        path = []

    path.append(current_position)

    if current_position == 'end':
        all_paths.append(path)
        return

    for cave in map[current_position]:
        if cave == 'start':
            continue

        if cave.islower() and cave in path:
            continue

        generate_paths(map, cave, path.copy())

    return all_paths


# create map
map = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    map[a].add(b)
    map[b].add(a)

print(len(generate_paths(map)))
