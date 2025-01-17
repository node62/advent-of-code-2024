#!/usr/bin/env python3

import sys
from collections import Counter

left = []
right = []

while True:
    line = input().strip()
    if line == "EOF":
        break
    if line:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

counter = Counter(right)
score = sum(num * counter[num] for num in left)
print(score)
