
rw1 = input().strip()
rw2 = input().strip()
rw3 = input().strip()

fdi = rw1[0] + rw2[1] + rw3[2]
sdi = rw1[2] + rw2[1] + rw3[0]

board = [rw1, rw2, rw3, fdi, sdi]

single_winner = 0
for rw in board:
    if rw.count(rw[0]) == 3:
        single_winner += 1

team_winners = 0
for rw in board:
    unique = list(set(rw))
    if len(unique) == 2 and rw.count(unique[0]) == 2 or rw.count(unique[1]) == 2 or rw.count(unique[2]) == 2:
        team_winners += 1


print(single_winner)
print(team_winners)
