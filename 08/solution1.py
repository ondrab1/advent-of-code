lines = open("input.txt").read().splitlines()

data = [[list(filter(None, z.split(' '))) for z in x.split('|')] for x in lines]

instances = 0
for item in data:
    inputs, outputs = item
    for output in outputs:
        if len(output) in [2, 3, 4, 7]:
            instances += 1

print(instances)
