import math

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # Finding the most frequent element
    arr.sort()
    max_freq = count = 1
    for i in range(1, n):
        if arr[i - 1] != arr[i]:
            count = 0
        count += 1
        max_freq = max(max_freq, count)

    # calculating the operation
    operation = 0
    while max_freq < n:
        operation += max_freq + 1
        max_freq += max_freq

    # We can evaluate the while loop mathmatically
    k = math.ceil(math.log(n/max_freq, 2))
    operation = k + max_freq*(2 ** k - 1)
    max_freq = max_freq*(2 ** k)

    # Returning the answer
    '''
  If we encounter the maximum frequent element more than n times during        duplication, it is advisable to reduce the number of operations by (max_freq - n), as the excess operations at the end are unnecessary.
  '''
    print(operation - (max_freq - n))
