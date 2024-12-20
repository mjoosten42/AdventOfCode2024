from vec import vec

track = {}

for y, line in enumerate(open(0)):
    for x, c in enumerate(line.strip()):
        track[vec(x, y)] = c

path = [next(p for p in track if track[p] == 'S')]

for p in path:
    n = next(n for n in p.neighbours() if n in track and track[n] != '#' and n not in path)

    path.append(n)

    if track[n] == 'E':
        break

#print(path)

cheats = {}

for start in path:
    ends = set(x for y in start.neighbours() if y in track and track[y] == '#' for x in y.neighbours() if x in track and track[x] != '#' and x != start)

    for end in ends:
        saved = path.index(end) - path.index(start) - 2

        if saved > 0:
            if not saved in cheats:
                cheats[saved] = 0

            cheats[saved] += 1


print(sum(y for x, y in cheats.items() if x >= 100))
