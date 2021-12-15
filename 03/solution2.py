import statistics

lines = open("input.txt").read().splitlines()

data = {}

# oxygen number
oxygen_numbers = list(lines)
bit_position = 0
while len(oxygen_numbers) != 1:
    bit_end_position = bit_position + 1
    # find most common bit
    bits_on_position = []
    for number in oxygen_numbers:
        bits_on_position.append(number[bit_position:bit_end_position])

    # find mode
    multimode = statistics.multimode(bits_on_position)
    if len(multimode) > 1:
        most_common_bit = 1
    else:
        most_common_bit = multimode[0]

    # filter out
    for number in list(oxygen_numbers):
        if number.find(str(most_common_bit), bit_position, bit_end_position) == -1:
            oxygen_numbers.remove(number)

    bit_position += 1

# co2 number
co2_numbers = list(lines)
bit_position = 0
while len(co2_numbers) != 1:
    bit_end_position = bit_position + 1
    # find most common bit
    bits_on_position = []
    for number in co2_numbers:
        bits_on_position.append(number[bit_position:bit_end_position])

    # find mode
    multimode = statistics.multimode(bits_on_position)
    most_common_bit = multimode[0]

    if len(multimode) > 1:
        least_common_bit = 0
    elif most_common_bit == '1':
        least_common_bit = 0
    else:
        least_common_bit = 1

    # filter out
    for number in list(co2_numbers):
        if number.find(str(least_common_bit), bit_position, bit_end_position) == -1:
            co2_numbers.remove(number)

    bit_position += 1


oxygen_number = oxygen_numbers.pop()
co2_number = co2_numbers.pop()

print(int(oxygen_number, 2) * int(co2_number, 2))
