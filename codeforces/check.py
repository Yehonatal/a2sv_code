def longestMountain(arr):
    # Base case
    if len(arr) < 3:
        return 0

    i = 0
    mx_range = 0

    while i < len(arr) - 1:
        # get to the lowest point
        while i < len(arr) - 1 and arr[i] >= arr[i+1]:
            i += 1
        lowest = i  # the valley

        # get to the peak
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
        peak = i  # the mountain top

        # Decreasing into the valley again until we get a new bump
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1

        if lowest < peak < i:
            # check if the largest range you've got
            mx_range = max(mx_range, i - lowest + 1)

    return mx_range


arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))
