
rw1 = input().strip()
rw2 = input().strip()
rw3 = input().strip()

cl1 = rw1[0] + rw2[0] + rw3[0]
cl2 = rw1[1] + rw2[1] + rw3[1]
cl3 = rw1[2] + rw2[2] + rw3[2]
fdi = rw1[0] + rw2[1] + rw3[2]
sdi = rw1[2] + rw2[1] + rw3[0]

board = [rw1, rw2, rw3, fdi, sdi, cl1, cl2, cl3]

single_winner = set()
for rw in board:
    if rw.count(rw[0]) == 3:
        single_winner.add(rw[0])

team_winners = set()
for rw in board:
    unique = list(set(rw))
    if len(unique) == 2:
        s = unique[0] + unique[1]
        if s[::-1] not in team_winners:
            team_winners.add(s)


print(len(single_winner))
print(len(team_winners))
