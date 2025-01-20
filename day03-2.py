import re
import sys

data = ""
for line in sys.stdin:
    if line.strip() == "EOF":
        break
    data += line

pattern_mul = re.compile(r"mul\((\d+),(\d+)\)")
pattern_do = re.compile(r"do\(\)")
pattern_dont = re.compile(r"don't\(\)")

enabled = True
result = 0

for match in re.finditer(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", data):
    instruction = match.group()

    if pattern_do.fullmatch(instruction):
        enabled = True
    elif pattern_dont.fullmatch(instruction):
        enabled = False
    elif pattern_mul.fullmatch(instruction) and enabled:
        x, y = map(int, pattern_mul.match(instruction).groups())
        result += x * y

print(result)