import copy
import re
import operator

target_area = open('input.txt').read()

match = re.findall(r'(x|y)=(-?\d+)\.\.(-?\d+)', target_area)

x_range = (int(match[0][1]), int(match[0][2]))
y_range = (int(match[1][1]), int(match[1][2]))

initial_velocities = []

for v_x in range(x_range[1] + 1):
    for v_y in range(-100, 100):
        position = (0, 0)
        initial_velocity = (v_x, v_y)
        velocity = copy.copy(initial_velocity)
        while True:
            # new position
            position = tuple(map(operator.add, position, velocity))

            # we hit target area
            if (x_range[0] <= position[0] <= x_range[1]) and (y_range[0] <= position[1] <= y_range[1]):
                initial_velocities.append(initial_velocity)
                break

            # we are out, we will never hit target area
            if position[0] > x_range[1] or position[1] < y_range[0]:
                break

            if velocity[0] > 0:
                x_change = -1
            elif velocity[0] < 0:
                x_change = 1
            else:
                x_change = 0

            # modify velocity
            velocity = tuple(map(operator.add, velocity, (x_change, -1)))

print(len(initial_velocities))
