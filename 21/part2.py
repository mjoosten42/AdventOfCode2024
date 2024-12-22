from vec import vec
import functools
import math

def to_str(path):
    s = ''

    for i in range(1, len(path)):
        s += (path[i] - path[i - 1]).to_char()

    s += 'A'

    return s

@functools.cache
def bfs(start, end, k):
    pad = dirpad if k else numpad
    sub = end - start
    s = ''

    sign = int(math.copysign(1, sub.x))
    hfirst = [start]
    vfirst = [start]

    for i in range(start.x, end.x, sign):
        hfirst.append(hfirst[-1] + vec(sign, 0))
    
    sign = int(math.copysign(1, sub.y))

    for i in range(start.y, end.y, sign):
        hfirst.append(hfirst[-1] + vec(0, sign))
        vfirst.append(vfirst[-1] + vec(0, sign))
    
    sign = int(math.copysign(1, sub.x))

    for i in range(start.x, end.x, sign):
        vfirst.append(vfirst[-1] + vec(sign, 0))

    if any(map(lambda x: x not in pad, hfirst)):
        hfirst = None

    if any(map(lambda x: x not in pad, vfirst)):
        vfirst = None
    
    if hfirst == vfirst:
        vfirst = None

    paths = []

    if hfirst:
        paths.append(hfirst)

    if vfirst:
        paths.append(vfirst)

    return [*map(to_str, paths)]

@functools.cache
def solve(code, limit, k):
    pad = dirpad if k else numpad
    start = next(x for x in pad if pad[x] == 'A')
    total = len(code)
   
    if k < limit + 1:
        total = 0

        for button in code:
            end = next(x for x in pad if pad[x] == button)
            paths = bfs(start, end, k)
            total += solve(paths[0], limit, k + 1)
            start = end

            print(k * ' ', paths[0])

    return total

codes = [x.strip() for x in open(0)]
numpad = { vec(0, 0): '7', vec(1, 0): '8', vec(2, 0): '9', vec(0, 1): '4', vec(1, 1): '5', vec(2, 1): '6', vec(0, 2): '1', vec(1, 2): '2', vec(2, 2): '3', vec(1, 3): '0', vec(2, 3): 'A' }
dirpad = { vec(1, 0): '^', vec(2, 0): 'A', vec(0, 1): '<', vec(1, 1): 'v', vec(2, 1): '>' }
total = 0

for code in codes:
    num = int(code[:-1])
    length = solve(code, 2, 0)
    complexity = length * num

    total += complexity

    print()
    print(f"{length} * {num} = {complexity}")

print(total)
