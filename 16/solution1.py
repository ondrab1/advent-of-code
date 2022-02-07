from textwrap import wrap

transmission = open('input.txt').read()


def decode_packet(binary_str):
    version = int(binary_str[:3], 2)
    type_id = int(binary_str[3:6], 2)
    packet_size = 6

    result = []

    if type_id == 4:
        for part in wrap(binary_str[6:], 5):
            result.append(part[1:])
            packet_size += 5
            if part[0] == '0':
                break
        result = int(''.join(result), 2)
    else:
        packet_size += 1
        if binary_str[6] == '0':
            length = int(binary_str[7:22], 2)
            next_binary = binary_str[22:]
            packet_size += 15 + length
            i = 0
            while i < length:
                decoded = decode_packet(next_binary[i:])
                result.append(decoded)
                i += decoded[2]
        else:
            sub_amount = int(binary_str[7:18], 2)
            packet_size += 11
            next_binary = binary_str[packet_size:]
            for i in range(sub_amount):
                decoded_sub = decode_packet(next_binary)
                result.append(decoded_sub)
                packet_size += decoded_sub[2]
                next_binary = binary_str[packet_size:]

    return version, type_id, packet_size, result


def sum_versions(result):
    if result[1] == 4:
        return result[0]
    else:
        return result[0] + sum(sum_versions(sub) for sub in result[3])


# convert to binary
binary = bin(int('1'+transmission, 16))[3:]
result = decode_packet(binary)

print(sum_versions(result))
