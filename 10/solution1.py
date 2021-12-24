from collections import defaultdict

lines = open("input.txt").read().splitlines()

chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

corrupted = defaultdict(int)
for line_index, line in enumerate(lines):
    opened_brackets = []
    for char in line:
        if char in chars.keys():
            opened_brackets.append(char)
        elif char != chars[opened_brackets.pop()]:
            corrupted[char] += 1

result = []
for char, count in corrupted.items():
    result.append(points[char] * count)

print(sum(result))
