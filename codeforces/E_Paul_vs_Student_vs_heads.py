n = int(input())
cityA = list(map(int, input().split()))
m = int(input())
cityB = list(map(int, input().split()))

i, j = 0, 0
size = 0

while i < n and j < m:
    if cityA[i] == cityB[j]:
        size += 1
        i += 1
        j += 1
    elif i < n - 1 and cityA[i] < cityB[j]:
        cityA[i+1] += cityA[i]
        i += 1
    elif j < m - 1:
        cityB[j+1] += cityB[j]
        j += 1
    else:
        break

if size:
    print(size)
else:
    print(-1)


""" 
    11, 2, 3, 5, 7 = 11, 10, 7
    11, 7, 3, 7 = 11, 10, 7

"""
