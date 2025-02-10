with open("input.txt") as f:
    a = f.read().split()
b = list(map(int, a))
for _ in range(25):
    c = []
    for n in b:
        if n == 0:
            c.append(1)
        else:
            s = str(n)
            if len(s) % 2 == 0:
                m = len(s) // 2
                c.append(int(s[:m]))
                c.append(int(s[m:]))
            else:
                c.append(n * 2024)
    b = c
print(len(b))

