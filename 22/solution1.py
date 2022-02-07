import re

lines = open('input.txt').read().splitlines()

min_coord = -50
max_coord = 50
reactor = {}

for line in lines:
    on = False
    if line[:2] == 'on':
        on = True

    match = re.findall(r'(x|y|z)=(-?\d+)\.\.(-?\d+)', line[3:])

    xr = (int(match[0][1]), int(match[0][2]))
    yr = (int(match[1][1]), int(match[1][2]))
    zr = (int(match[2][1]), int(match[2][2]))

    for x in range(max(min_coord, xr[0]), min(max_coord, xr[1]) + 1):
        for y in range(max(min_coord, yr[0]), min(max_coord, yr[1]) + 1):
            for z in range(max(min_coord, zr[0]), min(max_coord, zr[1]) + 1):
                if on is True:
                    if (x, y, z) not in reactor:
                        reactor[(x, y, z)] = 1
                else:
                    if (x, y, z) in reactor:
                        del reactor[(x, y, z)]

print(sum(reactor.values()))
