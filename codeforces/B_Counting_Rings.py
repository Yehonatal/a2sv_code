shapes = input()

r = 0
count = 0
for shape in shapes:
    if shape == "O":
        count += 1
    else:
        r = max(r, count)
        count = 0

r = max(r, count)

print(r)
