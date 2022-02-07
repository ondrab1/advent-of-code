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

start_position = min(risk_level_map.keys())
end_position = max(risk_level_map.keys())

print(dijkstra(risk_level_map, start_position, end_position))
