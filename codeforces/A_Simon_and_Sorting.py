
t = int(input())

for _ in range(t):
    s = list(input())
    s_ = sorted(s)

    volt = {}
    for i, c in enumerate(s):
        volt[c] = i

    volt_ = {}
    for i, c in enumerate(s_):
        volt_[c] = i

    swap = 0
    for c in s:
        if volt[c] != volt_[c]:
            swap += 1

    print("YES" if swap <= 2 else "NO")
