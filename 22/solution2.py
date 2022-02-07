import re
import os

lines = open('input.txt').read().splitlines()

min_coord = -50
max_coord = 50
reactor = {}
cubes = []

for line in lines:
    on = False
    if line[:2] == 'on':
        on = True

    match = re.findall(r'(x|y|z)=(-?\d+)\.\.(-?\d+)', line[3:])

    xr = (int(match[0][1]), int(match[0][2]))
    yr = (int(match[1][1]), int(match[1][2]))
    zr = (int(match[2][1]), int(match[2][2]))

    c = [on, xr[0], xr[1], yr[0], yr[1], zr[0], zr[1]]

    for cube in cubes.copy():
        ax = max(c[1], cube[1])
        bx = min(c[2], cube[2])
        ay = max(c[3], cube[3])
        by = min(c[4], cube[4])
        az = max(c[5], cube[5])
        bz = min(c[6], cube[6])

        if ax <= bx and ay <= by and az <= bz:
            cubes.append((not cube[0], ax, bx, ay, by, az, bz))

    if on is True:
        cubes.append(c)

count = 0
for cube in cubes:
    tmp = (cube[2] - cube[1] + 1) * (cube[4] - cube[3] + 1) * (cube[6] - cube[5] + 1)
    if cube[0] is True:
        count += tmp
    else:
        count -= tmp

print(count)
