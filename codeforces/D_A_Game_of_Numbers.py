t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))  # Frodo
    mums = list(map(int, input().split()))  # Sam
    nums.sort()
    mums.sort(reverse=True)

    diff = 0
    for i in range(n):
        diff += abs(mums[i-n] - nums[i])  # Find the initial largest diff

    curr = diff
    for i in range(n):
        curr -= abs(mums[i-n] - nums[i])
        curr += abs(mums[i] - nums[i])

        diff = max(diff, curr)  # gets re updated with a larger diff if found

    print(diff)
