print("Enter: ")
data = []
while True:
    line = input()
    if line == "EOF":
        break
    data.append(line)

grid = data
rows = len(grid)
if rows == 0:
    print(0)
    exit()

cols = len(grid[0])
start = None
start_dir = 0
for i in range(rows):
    for j in range(cols):
        c = grid[i][j]
        if c in '^>v<':
            start = (i, j)
            if c == '^':
                start_dir = 0
            elif c == '>':
                start_dir = 1
            elif c == 'v':
                start_dir = 2
            else:
                start_dir = 3
            break
    if start:
        break

direction_map = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_pos = start
current_dir = start_dir
visited = set()
visited.add(current_pos)

while True:
    dr, dc = direction_map[current_dir]
    next_row = current_pos[0] + dr
    next_col = current_pos[1] + dc

    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == '#':
        current_dir = (current_dir + 1) % 4
    else:
        new_pos = (next_row, next_col)
        if 0 <= next_row < rows and 0 <= next_col < cols:
            visited.add(new_pos)
            current_pos = new_pos
        else:
            break

print(len(visited))