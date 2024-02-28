def sortPeople(names, heights):
    n = len(heights)

    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if heights[j] > heights[max_index]:
                max_index = j

        # Swap heights
        heights[i], heights[max_index] = heights[max_index], heights[i]
        # Swap names accordingly
        names[i], names[max_index] = names[max_index], names[i]

    return names, heights


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(sortPeople(names, heights))
