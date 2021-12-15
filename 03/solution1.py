import statistics

lines = open("input.txt").read().splitlines()

data = {}

for line in lines:
    t = 1
    for index, bit in enumerate(line):
        if index not in data.keys():
            data[index] = []

        data[index].append(bit)

most_common_bits = {}

for index, bits in data.items():
    most_common_bits[index] = statistics.mode(bits)

binary = ''.join(str(x) for x in most_common_bits.values())
binary_inverted = binary.replace('1', '2').replace('0', '1').replace('2', '0')

# print(binary, int(binary, 2))
# print(binary_inverted, int(binary_inverted, 2))

print(int(binary, 2) * int(binary_inverted, 2))
