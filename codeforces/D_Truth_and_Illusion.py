t = int(input())

for _ in range(t):
    n = int(input())

    # Creating the Grid
    grid = []
    for i in range(n):
        grid.append(input())

    operation = 0
    for i in range(n):
        for j in range(n):
            arr = [grid[i][j], grid[j][n - i - 1],
                   grid[n - i - 1][n - j - 1], grid[n - j - 1][i]]
            operation += min(arr.count("1"), arr.count("0"))

    print(operation // 4)

""" 
# To rotate 90 degree
def rotate_90(matrix):
    n = len(matrix)
    rotated_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[j][n - i - 1]
    return rotated_matrix


# Accepting the inputs
t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        row = input()
        for j in range(n):
            matrix[i][j] = int(row[j])

    # Generating all matrix
    first_rotated_matrix = rotate_90(matrix)

    # Rotating the already 90 degree rotated matrix.
    second_rotated_matrix = rotate_90(first_rotated_matrix)

    # Rotating the already 90 degree rotated matrix.
    third_rotated_matrix = rotate_90(second_rotated_matrix)

    operation = 0
    for i in range(n):
        for j in range(n):
            # arr = [0 degree, 90 degree, 180 degree, 270 degree]
            arr = [matrix[i][j], first_rotated_matrix[i][j],
                   second_rotated_matrix[i][j], third_rotated_matrix[i][j]]
            operation += min(arr.count(1), arr.count(0))

    # Since we are counting for the same position 4 times
    print(operation // 4)
 """
