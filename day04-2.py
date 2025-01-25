import sys

print("Enter: ")

lines = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if line == 'EOF':
        break
    lines.append(line)

grid = lines
count = 0
R = len(grid)
if R == 0:
    print(0)
    sys.exit()
C = len(grid[0])

for i in range(R):
    for j in range(C):
        if grid[i][j] != 'A':
            continue
        valid_main = False
        if i-1 >= 0 and j-1 >= 0 and i+1 < R and j+1 < C:
            s = grid[i-1][j-1] + 'A' + grid[i+1][j+1]
            if s in ('MAS', 'SAM'):
                valid_main = True
        valid_anti = False
        if i-1 >= 0 and j+1 < C and i+1 < R and j-1 >= 0:
            s = grid[i-1][j+1] + 'A' + grid[i+1][j-1]
            if s in ('MAS', 'SAM'):
                valid_anti = True
        if valid_main and valid_anti:
            count += 1

print(count)