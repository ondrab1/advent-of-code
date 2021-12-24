import statistics
from collections import defaultdict

lines = open("input.txt").read().splitlines()
lines = {i: x for i, x in enumerate(lines)}

chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

for line_index, line in list(lines.items()):
    opened_brackets = []
    for char in line:
        if char in chars.keys():
            opened_brackets.append(char)
        elif char != chars[opened_brackets.pop()]:
            if line_index in lines:
                del lines[line_index]

completions = defaultdict(list)
for line_index, line in lines.items():
    opened_brackets = []
    for char in line:
        if char in chars.keys():
            opened_brackets.append(char)
        else:
            opened_brackets.pop()

    opened_brackets.reverse()

    for char in opened_brackets:
        completions[line_index].append(chars[char])

scores = []
for chars in completions.values():
    score = 0
    for char in chars:
        score *= 5
        score += points[char]

    scores.append(score)

print(statistics.median(scores))
