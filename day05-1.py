import sys

print("Enter: ")

lines = []
for line in sys.stdin:
    line = line.strip()
    if line == 'EOF':
        break
    if line:
        lines.append(line)

rules, updates = [], []
is_rule = True
for line in lines:
    if is_rule and ',' in line:
        is_rule = False
    if is_rule:
        rules.append(line)
    else:
        updates.append(line)

rule_pairs = [tuple(map(int, r.split('|'))) for r in rules]
update_lists = [list(map(int, u.split(','))) for u in updates]

total = 0
for lst in update_lists:
    pos = {p: i for i, p in enumerate(lst)}
    valid = True
    for x, y in rule_pairs:
        if x in pos and y in pos and pos[x] >= pos[y]:
            valid = False
            break
    if valid:
        total += lst[(len(lst) - 1) // 2]

print(total)