def go(i, j):
    if (i, j) in mem:
        return mem[(i, j)]
    if grid[i][j] == 9:
        mem[(i, j)] = {(i, j)}
        return {(i, j)}
    s = set()
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == grid[i][j] + 1:
            s |= go(ni, nj)
    mem[(i, j)] = s
    return s

with open("input.txt") as f:
    data = [x.strip() for x in f.read().splitlines() if x.strip()]
grid = [list(map(int, list(x))) for x in data]
r = len(grid)
c = len(grid[0])
mem = {}
tot = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 0:
            tot += len(go(i, j))
print(tot)
