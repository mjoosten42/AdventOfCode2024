rules, manuals = map(lambda l: list(map(lambda k: [*map(int, k.split(','))], str.split(l))), open(0).read().replace('|', ',').split("\n\n"))

total = 0

for m in manuals:
    wrong = False
    i = 0

    while i < len(rules):
        r = rules[i]

        if r[0] in m and r[1] in m:
            id = [m.index(r[0]), m.index(r[1])]
            if id[0] > id[1]:
                m[id[0]], m[id[1]] = m[id[1]], m[id[0]]
                i = -1
                wrong = True

        i += 1

    total += m[len(m) // 2] * wrong

print(total)

