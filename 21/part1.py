from vec import vec

def to_str(path):
    s = ''

    for i in range(1, len(path)):
        s += (path[i] - path[i - 1]).to_char()

    s += 'A'

    return s

def bfs(pad, start, end):
    dist = end.distance(start)
    queue = [[start]]
    result = []

    while queue:
        path = queue.pop(0)

        if path[-1] == end:
            result.append(path)
            continue
        
        if len(path) > dist + 1:
            break

        for n in path[-1].neighbours():
            if n in pad and n not in path:
                queue.append([*path, n])

    return result

def solve(numpad, dirpad, start, end, k = 0):
    r = []
    pad = dirpad if k else numpad
    paths = [*map(to_str, bfs(pad, start, end))]

    if k < 2:
        for path in paths:
            start = next(x for x in dirpad if dirpad[x] == 'A')
            s = ['']

            for c in path:
                end = next(x for x in dirpad if dirpad[x] == c)
                new = []

                p = solve(numpad, dirpad, start, end, k + 1)
                
                least = min(map(len, p))
                p = [x for x in p if len(x) == least]

                for t in s:
                    new.append(t + p[0])

                for q in p[1:]:
                    for u in s:
                        new.append(u + q)

                s = new.copy()
                start = end

            r += s
    else:
        r = paths

    return r
    

codes = [x.strip() for x in open(0)]
numpad = { vec(0, 0): '7', vec(1, 0): '8', vec(2, 0): '9', vec(0, 1): '4', vec(1, 1): '5', vec(2, 1): '6', vec(0, 2): '1', vec(1, 2): '2', vec(2, 2): '3', vec(1, 3): '0', vec(2, 3): 'A' }
dirpad = { vec(1, 0): '^', vec(2, 0): 'A', vec(0, 1): '<', vec(1, 1): 'v', vec(2, 1): '>' }
total = 0

for code in codes:
    start = next(x for x in numpad if numpad[x] == 'A')
    s = ''

    for c in code:
        end = next(x for x in numpad if numpad[x] == c)

        p = solve(numpad, dirpad, start, end)
        
        least = min(map(len, p))
        p = [x for x in p if len(x) == least]

        s += p[0]

        start = end

    total += (len(s) * int(code[:-1]))

print(total)
