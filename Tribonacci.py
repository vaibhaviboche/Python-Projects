def tribonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    if length <= 3:
        return start_sequence[:length]

    result = start_sequence[:]
    while len(result) < length:
        next_value = result[-1] + result[-2] + result[-3]
        result.append(next_value)
    return result
print(tribonacci_sequence([0, 0, 1], 10))
# Output: [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

print(tribonacci_sequence([123, 456, 789], 8))
# Output: [123, 456, 789, 1368, 2613, 4770, 8751, 16134]
