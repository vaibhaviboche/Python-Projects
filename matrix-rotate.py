def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
print(rotate([[1]]))
# [[1]]

print(rotate([[1, 2], [3, 4]]))
# [[3, 1], [4, 2]]

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

print(rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]))
# [[0, 1, 0], [0, 0, 1], [0, 1, 0]]

