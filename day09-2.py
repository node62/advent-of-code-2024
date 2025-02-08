with open("input.txt") as f:
    s = f.read().strip()

lst = []
i = 0
j = 0

while i < len(s):
    n = int(s[i])
    if i % 2 == 0:
        lst += [str(j)] * n
        j += 1
    else:
        lst += ["."] * n
    i += 1

mx = j - 1

for fid in range(mx, -1, -1):
    pos = -1
    for i in range(len(lst)):
        if lst[i] == str(fid):
            pos = i
            break
    if pos == -1:
        continue
    cnt = 0
    st = pos

    while st < len(lst) and lst[st] == str(fid):
        cnt += 1
        st += 1

    moved = False
    for i in range(0, pos - cnt + 1):
        if i + cnt - 1 >= pos:
            break
        ok = True
        for k in range(i, i + cnt):
            if lst[k] != ".":
                ok = False
                break
        if ok:
            for k in range(i, i + cnt):
                lst[k] = str(fid)
            for k in range(pos, pos + cnt):
                lst[k] = "."
            moved = True
            break

s = 0
for i, v in enumerate(lst):
    if v != ".":
        s += i * int(v)

print(s)
