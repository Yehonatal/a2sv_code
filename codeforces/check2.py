def maxArea(height):
    left, right = 0, len(height) - 1

    container = 0
    walls = 0
    while left < right:
        while height[left] <= height[left + 1]:
            left += 1
        wall1 = height[left]

        while height[right] < height[right - 1]:
            right -= 1
        wall2 = height[right]

        walls = max(walls, max(wall1, wall2) - abs(wall1-wall2))

        left += 1
        right -= 1
        container = max(container, walls**2)

    return container


# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49
# print(maxArea(height))
# height = [1, 6, 9, 2, 5, 4, 9, 3, 2]  # 36
# print(maxArea(height))
# height = [1, 6, 9, 2, 5, 4, 9, 3, 5]  # 36
# print(maxArea(height))
height = [1, 1, 1, 1, 8, 2, 3, 4, 9, 2]  # 32
print(maxArea(height))
