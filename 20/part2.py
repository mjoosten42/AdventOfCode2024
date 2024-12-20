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

cheats = {}
score = { pos: path.index(pos) for pos in path }

for start in path:
    ends = [x for x in start.reachable(20) if x in track and track[x] != '#']

    for end in ends:
        d = end.distance(start)
        saved = score[end] - score[start] - d

        if saved > 0:
            if not saved in cheats:
                cheats[saved] = 0

            cheats[saved] += 1

print(sum(y for x, y in cheats.items() if x >= 100))
