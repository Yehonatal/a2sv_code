t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))  # Frodo
    mums = list(map(int, input().split()))  # Sam
    nums.sort()
    mums.sort(reverse=True)
    D = 0
    i, j = 0, 0

    while i < n and j < m:
        while i < n and nums[i] < mums[j]:
            D += mums[j] - nums[i]
            i += 1
            j += 1

        if i < n:
            jump = n - i
            j += min(jump, m - j)
            if j < m:
                while j < m and i < n and nums[i] > mums[j]:
                    D += nums[i] - mums[j]
                    i += 1
                    j += 1
            else:
                break

    print(D)
