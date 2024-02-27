def findDiagonalOrder(mat):
    volt = {}

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            s = r + c
            if s not in volt:
                volt[s] = [mat[r][c]]
            else:
                volt[s].append(mat[r][c])

    res = []

    for zone, elem in volt.items():
        if zone % 2 == 0:
            res.extend(elem[::-1])
        else:
            res.extend(elem)

    return res


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findDiagonalOrder(mat))  # Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
mat = [[1, 2], [3, 4]]
print(findDiagonalOrder(mat))  # Output: [1, 2, 3, 4]
