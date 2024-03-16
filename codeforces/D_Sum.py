t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    nums = sorted(list(map(int, input().split())))

    for i in range(1, k+1):
        if i % 2 != 0:
            # Remove 2 from the front
            nums = nums[2:]
        else:
            # Remove 1 from the end
            nums = nums[:-1]

    print(sum(nums))
