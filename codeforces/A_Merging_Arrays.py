n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


merged = []

left = right = 0
while left < n and right < m:
    if arr1[left] < arr2[right]:
        merged.append(arr1[left])
        left += 1  # for cases where one list gets exhausted
    else:
        merged.append(arr2[right])
        right += 1


merged.extend(arr1[left:])
merged.extend(arr2[right:])

print(*merged)
