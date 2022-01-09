from collections import defaultdict

lines = open('input.txt').read().splitlines()

all_paths = []


def generate_paths(map, current_position='start', path=None, repeatable=True):
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

        if cave.isupper() or cave not in path:
            generate_paths(map, cave, path.copy(), repeatable)
        elif cave.islower() and repeatable:
            generate_paths(map, cave, path.copy(), False)

    return all_paths


# create map
map = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    map[a].add(b)
    map[b].add(a)

print(len(generate_paths(map)))
