from vec import vec
import sys

def bfs(pad, start, end):
    queue = [[start]]
    paths = []

    while queue:
        path = queue.pop(0)
        last = path[-1]

        if last == end:
            paths.append(path)
        
        if paths:
            continue

        for n in last.neighbours():
            if n in pad and n not in path:
                queue.append([*path, n])

    return paths

def to_str(path):
    s = ''

    for i in range(1, len(path)):
        s += (path[i] - path[i - 1]).to_char()

    return s

def create_padmap(pad):
    padMap = {}

    for first_button in pad.values():
        padMap[first_button] = {}

        for second_button in pad.values():
            start = next(x for x in pad if pad[x] == first_button)
            end = next(x for x in pad if pad[x] == second_button)

            padMap[first_button][second_button] = [*map(to_str, bfs(pad, start, end))]

    return padMap

def buildSeq(keys, index, prevKey, currPath, padMap):
    if index == len(keys):
        yield currPath
        return
  
    for path in padMap[prevKey][keys[index]]:
        yield from buildSeq(keys, index + 1, keys[index], currPath + path + 'A', padMap)

def split(code):
    while 'A' in code:
        i = code.index('A')

        yield code[:i + 1]

        code = code[i + 1:]

def shortestSeq(keys, depth, cache):
    total = 0

    if not depth:
        return len(keys)

    if depth in cache and keys in cache[depth]:
        return cache[depth][keys]

    for subKey in split(keys):
        seqList = list(buildSeq(subKey, 0, 'A', '', dirpadMap))

        least = sys.maxsize

        for seq in seqList:
            l = shortestSeq(seq, depth - 1, cache)

            if l < least:
                least = l

        total += least

    if depth not in cache:
        cache[depth] = {}

    cache[depth][keys] = total

    return total

def solve(codes, depth):
    cache = { }
    total = 0

    for code in codes:
        num = int(code[:-1])

        numSeqList = list(buildSeq(code, 0, 'A', '', numpadMap))

        least = sys.maxsize

        for seq in numSeqList:
            l = shortestSeq(seq, depth, cache)

            if l < least:
                least = l

        total += (least * num)

    return total

codes = [x.strip() for x in open(0)]
numpad = { vec(0, 0): '7', vec(1, 0): '8', vec(2, 0): '9', vec(0, 1): '4', vec(1, 1): '5', vec(2, 1): '6', vec(0, 2): '1', vec(1, 2): '2', vec(2, 2): '3', vec(1, 3): '0', vec(2, 3): 'A' }
dirpad = { vec(1, 0): '^', vec(2, 0): 'A', vec(0, 1): '<', vec(1, 1): 'v', vec(2, 1): '>' }

numpadMap = create_padmap(numpad)
dirpadMap = create_padmap(dirpad)

print(solve(codes, 25))


