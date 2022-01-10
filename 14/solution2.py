from collections import defaultdict

lines = open('input.txt').read().splitlines()

template = ''
insertions = {}
for index, line in enumerate(lines):
    if line == '':
        continue

    if index == 0:
        template = line
        continue

    left, right = line.split('->')

    insertions[left.strip()] = right.strip()

pairs = defaultdict(int)
counts = defaultdict(int)
# start pairs
for pair in [''.join(pair) for pair in zip(template[:-1], template[1:])]:
    pairs[pair] += 1

# start counts
for char in template:
    counts[char] += 1

for step in range(0, 40):
    for pair, count in pairs.copy().items():
        if count > 0 and pair in insertions:
            left, right = tuple(pair)
            pairs[pair] -= 1 * count
            pairs[left + insertions[pair]] += 1 * count
            pairs[insertions[pair] + right] += 1 * count
            counts[insertions[pair]] += 1 * count

print(max(counts.values()) - min(counts.values()))
