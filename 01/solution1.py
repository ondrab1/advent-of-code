lines = open("input.txt").read().splitlines()

increases = 0
previous = None
for index, line in enumerate(lines):
    number = int(line)
    if previous is not None and number > previous:
        increases += 1

    previous = number

print(increases)
