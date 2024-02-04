def searchMatrix(matrix, target):
    if len(matrix) == 0:
        return False

    for row in matrix:
        if row[0] <= target <= row[-1]:
            l = 0
            h = len(row) - 1

            while l <= h:
                mid = l + (h - l) // 2

                if row[mid] == target:
                    return True

                if row[mid] > target:
                    h = mid - 1
                elif row[mid] < target:
                    l = mid + 1

            return False


# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 3
# print(searchMatrix(matrix, target))

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(searchMatrix(matrix, target))
