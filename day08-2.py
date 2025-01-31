import sys
from itertools import combinations
from collections import defaultdict
import math

lines = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if line == 'EOF':
        break
    lines.append(line)

if not lines:
    print(0)
    sys.exit()

height = len(lines)
width = len(lines[0]) if height else 0

antennas = []
for y in range(height):
    for x in range(len(lines[y])):
        c = lines[y][x]
        if c != '.':
            antennas.append((x, y))

antennas_by_freq = defaultdict(list)
for x, y in antennas:
    freq = lines[y][x]
    antennas_by_freq[freq].append((x, y))

antinodes = set()

for freq, group in antennas_by_freq.items():
    if len(group) < 2:
        continue
    for a, b in combinations(group, 2):
        x1, y1 = a
        x2, y2 = b
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0 and dy == 0:
            continue
        g = math.gcd(abs(dx), abs(dy))
        step_x = dx // g
        step_y = dy // g
        
        t = 0
        while True:
            current_x = x1 + t * step_x
            current_y = y1 + t * step_y
            if 0 <= current_x < width and 0 <= current_y < height:
                antinodes.add((current_x, current_y))
                t += 1
            else:
                break
        
        t = -1
        while True:
            current_x = x1 + t * step_x
            current_y = y1 + t * step_y
            if 0 <= current_x < width and 0 <= current_y < height:
                antinodes.add((current_x, current_y))
                t -= 1
            else:
                break

print(len(antinodes))