n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
output = []

j = 0
for i in range(len(arr2)):
    # makes sure to bound it to arr1's length to avoid the pointer dropping off the end
    while j < n and arr1[j] < arr2[i]:
        j += 1
    # any number that comes before is guaranteed to be smaller
    output.append(j)


print(*output)
