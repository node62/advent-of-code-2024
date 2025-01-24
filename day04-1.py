lines = []

print("Enter: ")
while True:
    line = input().strip()
    if line == 'EOF':
        break
    lines.append(line)

grid = lines
count = 0
R = len(grid)
if R == 0:
    print(0)
    exit()
C = len(grid[0])

directions = [(-1,-1), (-1, 0), (-1, 1),
              ( 0,-1),           ( 0, 1),
              ( 1,-1),  (1, 0),  ( 1, 1)]

for i in range(R):
    for j in range(C):
        if grid[i][j] != 'X':
            continue
        for dr, dc in directions:
            ni1, nj1 = i + dr * 1, j + dc * 1
            ni2, nj2 = i + dr * 2, j + dc * 2
            ni3, nj3 = i + dr * 3, j + dc * 3
            if 0 <= ni1 < R and 0 <= nj1 < C and 0 <= ni2 < R and 0 <= nj2 < C and 0 <= ni3 < R and 0 <= nj3 < C:
                if grid[ni1][nj1] == 'M' and grid[ni2][nj2] == 'A' and grid[ni3][nj3] == 'S':
                    count += 1

print(count)