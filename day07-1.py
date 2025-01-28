import sys
from itertools import product

lines = []
for line in sys.stdin:
    l = line.strip()
    if l == 'EOF':
        break
    lines.append(l)

total = 0

for l in lines:
    if not l:
        continue
    target_part, nums_part = l.split(':')
    target = int(target_part)
    nums = list(map(int, nums_part.split()))
    if not nums:
        continue
    if len(nums) == 1:
        if nums[0] == target:
            total += target
        continue
    valid = False
    n = len(nums)
    for ops in product('+*', repeat=n-1):
        res = nums[0]
        for i in range(n-1):
            if ops[i] == '+':
                res += nums[i+1]
            else:
                res *= nums[i+1]
            if res == target and i == n-2:
                valid = True
                break
        if valid:
            break
    if valid:
        total += target

print(total)