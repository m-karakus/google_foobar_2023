def xor_of_sequence(first, last):
    if first % 2 == 0:  # if the first number in the sequence is even
        xor_pattern = [last, 1, last + 1, 0]
    else:  # if the first number in the sequence is odd
        xor_pattern = [first, first ^ last, first - 1, (first - 1) ^ last]

    return xor_pattern[(last - first) % 4]  # the XOR pattern repeats every 4 numbers


def solution(start, length):
    max_id = 2000000000
    range_boundary = start + length * length

    if range_boundary > max_id or start < 0 or length < 0:
        return None

    security_checksum = 0

    for security_id in range(0, length):  # treat each 'row' as a sequence of numbers
        first = start + (length * security_id)  # the first number in the row / sequence
        last = first + (length - security_id) - 1  # the last number in the row / sequence

        security_checksum ^= xor_of_sequence(first, last)  # update the checksum with the XOR for each row

    return security_checksum

if __name__ == "__main__":
    print(solution(17, 4))
    print(solution(0, 3))