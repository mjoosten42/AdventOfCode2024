rules, manuals = map(lambda l: list(map(lambda k: [*map(int, k.split(','))], str.split(l))), open(0).read().replace('|', ',').split("\n\n"))

total = 0

for m in manuals:
    for r in rules:
        if r[0] in m and r[1] in m:
            if m.index(r[0]) > m.index(r[1]):
                break
    else:
        total += m[len(m) // 2]

print(total)

