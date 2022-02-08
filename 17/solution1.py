import re
import operator

target_area = open('input.txt').read()

match = re.findall(r'(x|y)=(-?\d+)\.\.(-?\d+)', target_area)

x_range = (int(match[0][1]), int(match[0][2]))
y_range = (int(match[1][1]), int(match[1][2]))

highest_y = 0

for v_x in range(x_range[1] + 1):
    for v_y in range(-100, 100):
        max_y = 0
        position = (0, 0)
        velocity = (v_x, v_y)
        while True:
            # new position
            position = tuple(map(operator.add, position, velocity))

            # save max_y of current velocity
            max_y = max(max_y, position[1])

            # we hit target area
            if (x_range[0] <= position[0] <= x_range[1]) and (y_range[0] <= position[1] <= y_range[0]):
                highest_y = max(highest_y, max_y)
                break

            # we are out, we will never hit target area
            if position[0] > x_range[1] or position[1] < y_range[1]:
                break

            if velocity[0] > 0:
                x_change = -1
            elif velocity[0] < 0:
                x_change = 1
            else:
                x_change = 0

            # modify velocity
            velocity = tuple(map(operator.add, velocity, (x_change, -1)))

print(highest_y)
