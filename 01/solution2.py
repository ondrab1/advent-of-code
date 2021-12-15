lines = open("input.txt").read().splitlines()

lines = [int(x) for x in lines]

increases = 0
previous = None
for index, line in enumerate(lines):
    if index < 2:
        continue

    numbers = lines[(index - 2):(index + 1)]

    number = sum(numbers)
    if previous is not None and number > previous:
        increases += 1

    previous = number

print(increases)
