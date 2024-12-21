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

        if result:
            continue
        
        d = [vec(1, 0), vec(0, -1), vec(0, 1), vec(-1, 0)]
        for n in [x + path[-1] for x in d]:
            if n in pad and n not in path:
                queue.append([*path, n])

def cost(pad, button, cache, k):
    if k == 3:
        return 1
    
    if k not in cache:
        cache[k] = { }

    if button in cache[k]:
        return cache[k][button]

    start = vec(2, 0)
    end = next(x for x in pad if pad[x] == button)
    path = to_str(bfs(pad, start, end))
    total = 0

    for c in path:
        bcost = cost(pad, c, cache, k + 1) + path.index(c)

        cache[k][c] = bcost
        
        total += bcost

    return total

codes = [x.strip() for x in open(0)]
numpad = { vec(0, 0): '7', vec(1, 0): '8', vec(2, 0): '9', vec(0, 1): '4', vec(1, 1): '5', vec(2, 1): '6', vec(0, 2): '1', vec(1, 2): '2', vec(2, 2): '3', vec(1, 3): '0', vec(2, 3): 'A' }
dirpad = { vec(1, 0): '^', vec(2, 0): 'A', vec(0, 1): '<', vec(1, 1): 'v', vec(2, 1): '>' }
total = 0

for code in codes
