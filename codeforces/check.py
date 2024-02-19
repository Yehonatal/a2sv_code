check = {"OX"}
print(check)
s = 'XO'
if s[::-1] not in check:
    check.add(s)
print(check)
