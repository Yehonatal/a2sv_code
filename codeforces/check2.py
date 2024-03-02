s = ['c', 'b', 'a']

volt = {}
for i, c in enumerate(s):
    volt[c] = i

s_ = sorted(s)
volt_ = {}

for i, c in enumerate(s_):
    volt_[c] = i


print(volt, volt_)
