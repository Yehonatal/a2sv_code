def trimMean(arr):
    arr.sort()  # To make cutting off the 5% easier

    n = len(arr)
    cut_off = int((5/100) * n)  # (5/100) * n, get the cutting off points
    # remove the 5% of the element from the front and back
    arr = arr[cut_off:-cut_off]

    # Get the sum and divide it with the size, The new arr without the 5$
    return sum(arr) / len(arr)


arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
print(trimMean(arr))
