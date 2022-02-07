lines = open('input.txt').read().splitlines()


def dijkstra(map_dict, start_position, end_position):
    unvisited = set(map_dict.keys())
    node_dict = {start_position: 0}
    current_node = start_position
    while node_dict:
        x, y = current_node
        risk = node_dict[current_node]

        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for next_to in adjacent:
            if next_to not in unvisited:
                continue

            current_risk = node_dict.get(next_to, None)
            new_risk = risk + map_dict[next_to]
            if not current_risk or new_risk < current_risk:
                node_dict[next_to] = new_risk

        unvisited.remove(current_node)
        del node_dict[current_node]

        lowest_risk = min(node_dict.values())
        for position, risk in node_dict.items():
            if risk == lowest_risk:
                current_node = position
                break

        if current_node == end_position:
            return node_dict[end_position]

    return None


risk_level_map = {}
for y, line in enumerate(lines):
    for x, value in enumerate(line):
        risk_level_map[(x, y)] = int(value)

max_x = max(risk_level_map.keys(), key=lambda n: n[1])[1]
max_y = max(risk_level_map.keys(), key=lambda n: n[0])[0]

# make it larger
# x axis
for (x, y), value in risk_level_map.copy().items():
    for i in range(1, 5):
        new_value = value + i
        new_value = new_value if new_value < 10 else (new_value - 9)
        risk_level_map[(x + ((max_x + 1) * i), y)] = new_value

# y axis
for (x, y), value in risk_level_map.copy().items():
    for i in range(1, 5):
        new_value = value + i
        new_value = new_value if new_value < 10 else (new_value - 9)
        risk_level_map[x, (y + ((max_y + 1) * i))] = new_value

start_position = min(risk_level_map.keys())
end_position = max(risk_level_map.keys())

print(dijkstra(start_position, risk_level_map))
