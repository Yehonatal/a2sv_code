# men, elves, dwarves, orcs, wolves
powers = list(map(int, input().split()))
armies = list(map(int, input().split()))

power_hash = []

for i in range(len(armies)):
    power_hash.append([armies[i], powers[i]])

# team 1, bilbos side = m, e, d
team1 = sum([army * power for army, power in power_hash[:3]])
team2 = sum([army * power for army, power in power_hash[3:]])


if team1 > team2:
    print('WIN')
elif team1 == team2:
    print("DRAW")
else:
    print("LOSE")
