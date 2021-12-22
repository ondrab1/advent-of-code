from collections import defaultdict

lines = open("input.txt").read().splitlines()

data = [[list(filter(None, z.split(' '))) for z in x.split('|')] for x in lines]

result = 0
for item in data:
    inputs, outputs = item
    decoder = defaultdict(str)

    for value in inputs:
        if len(value) == 2:
            decoder[1] = value
        elif len(value) == 4:
            decoder[4] = value
        elif len(value) == 3:
            decoder[7] = value
        elif len(value) == 7:
            decoder[8] = value

    for value in inputs:
        if len(value) == 6:
            if len(set(value) - set(decoder[1])) == 5:
                decoder[6] = value
            elif len(set(value) - set(decoder[4])) == 2:
                decoder[9] = value
            else:
                decoder[0] = value
        elif len(value) == 5:
            if len(set(value) - set(decoder[1])) == 3:
                decoder[3] = value
            elif len(set(value) - set(decoder[4])) == 2:
                decoder[5] = value
            else:
                decoder[2] = value

    number = []
    for output in outputs:
        for num, decoder_code in decoder.items():
            if set(output) == set(decoder_code):
                number.append(str(num))
                break

    result += int(''.join(number))

print(result)
