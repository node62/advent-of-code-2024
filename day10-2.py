def do(i, j):
    if (i, j) in mem:
        return mem[(i, j)]
    if grid[i][j] == 9:
        mem[(i, j)] = 1
        return 1
    s = 0
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == grid[i][j] + 1:
            s += do(ni, nj)
    mem[(i, j)] = s
    return s

with open("input.txt") as f:
    l = [x.strip() for x in f.read().splitlines() if x.strip()]
grid = [list(map(int, list(x))) for x in l]
R = len(grid)
C = len(grid[0])
mem = {}
tot = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == 0:
            tot += do(i, j)
print(tot)
