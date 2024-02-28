n, m = list(map(int, input().split()))

A = []
B = [[0] * m for _ in range(n)]

for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

ops = []

for r in range(n-1):
    for c in range(m-1):
        if A[r][c] == A[r][c+1] == A[r+1][c] == A[r+1][c+1] == 1:
            B[r][c] = 1
            B[r][c+1] = 1
            B[r+1][c] = 1
            B[r+1][c+1] = 1

            ops.append((r, c))

if A != B:
    print(-1)
else:
    print(len(ops))
    for r, c in ops:
        print(r+1, c+1)
