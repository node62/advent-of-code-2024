import sys
from itertools import combinations
from collections import defaultdict

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
        p1x = 2 * x2 - x1
        p1y = 2 * y2 - y1
        p2x = 2 * x1 - x2
        p2y = 2 * y1 - y2
        if 0 <= p1x < width and 0 <= p1y < height:
            antinodes.add((p1x, p1y))
        if 0 <= p2x < width and 0 <= p2y < height:
            antinodes.add((p2x, p2y))

print(len(antinodes))