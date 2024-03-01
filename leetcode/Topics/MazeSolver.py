def Walk(maze, wall, curr, end, seen, path):
    _dir = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]

    if curr[0] < 0 or curr[0] >= len(maze[0]) or curr[1] < 0 or curr[1] >= len(maze):
        return False

    if maze[curr[1]][curr[0]] == wall:
        return False

    if curr[0] == end[0] and curr[1] == end[1]:
        path.append(end)
        return True

    if seen[curr[1]][curr[0]]:
        return False

    seen[curr[1]][curr[0]] = True
    path.append(curr)

    for d in _dir:
        x, y = d
        if Walk(maze, wall, [curr[0]+x, curr[1]+y], end, seen, path):
            return True

    path.pop()
    return False


def MazeSolver(maze, wall, start, end):
    seen = []
    path = []

    for row in maze:
        seen.append([False for _ in range(len(row))])

    Walk(maze, wall, start, end, seen, path)

    return path


maze = [
    "xxxxxxxxxx x",
    "x xxxx   x x",
    "x x  xxx x x",
    "xxx    xxx x",
    "x    x     x",
    "x xxxxxxxxxx",
]
wall = "x"
start = [10, 0]
end = [1, 5]

foundPath = MazeSolver(maze, wall, start, end)

maze = [[x for x in m] for m in maze]
for x, y in foundPath:
    maze[y][x] = "*"

for m in maze:
    print("".join(m))
print()
