with open("input.txt") as f:
    s = f.read().strip()

a = []
i = 0
j = 0

while i < len(s):
    n = int(s[i])
    if i % 2 == 0:
        a += [str(j)] * n
        j += 1
    else:
        a += ["."] * n
    i += 1

while 1:
    try:
        x = a.index(".")
    except:
        break
    y = -1
    while a[y] == ".":
        y -= 1
    y = len(a) + y
    if x >= y:
        break
    a[x] = a[y]
    a[y] = "."

s = 0
for i, v in enumerate(a):
    if v != ".":
        s += i * int(v)

print(s)
