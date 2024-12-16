from vec import vec
import sys

def reconstruct(cameFrom, pos):
    queue = [pos]
    tiles = set()

    while queue:
        pos = queue.pop(0)

        tiles.add(pos)

        if pos in cameFrom:
            queue.extend(cameFrom[pos])

    return tiles

def h(first, second):
    sub = abs(second - first)

    return (sub.x + sub.y)

def debug_tiles(maze, tiles):
    limit = max(maze)

    for y in range(limit.y + 1):
        for x in range(limit.x + 1):
            pos = vec(x, y)

            if pos in tiles:
                print('O', end='')
            else:
                print(maze[pos], end='')
        print()
    print()

def debug_cost(maze, gScore):
    limit = max(maze)

    for y in range(limit.y + 1):
        for x in range(limit.x + 1):
            pos = vec(x, y)

            if pos in gScore:
                print(f" {gScore[pos]:5} ", end='')
            else:
                print(f" {maze[pos] * 5} ", end='')
        print()
        print()
    print()

def search(maze: dict[vec, str], start, end):
    openSet = [start]
    cameFrom: dict[vec, list[vec]] = {}
    gScore = { start: 0 }
    fScore = { start: h(start, end) }

    while openSet:
        node = min(openSet, key=lambda x: fScore[x])

        openSet.remove(node)

        for n in node.neighbours():
            if n in maze and maze[n] != '#':
                if n not in fScore:
                    gScore[n] = sys.maxsize
                
                cost = 1
    
                if n - node != (vec(1, 0) if node not in cameFrom else node - cameFrom[node][0]):
                    cost += 1000

                tentative_gScore = gScore[node] + cost

                if tentative_gScore == gScore[n] + 1000:
                    if n not in cameFrom:
                        cameFrom[n] = []
                    cameFrom[n].append(node)

                if tentative_gScore < gScore[n]:
                    if n not in cameFrom:
                        cameFrom[n] = []
                    cameFrom[n].append(node)
                    gScore[n] = tentative_gScore
                    fScore[n] = tentative_gScore + h(n, end)

                    if n not in openSet:
                        openSet.append(n)

    return (reconstruct(cameFrom, end), gScore)
maze = {}

for y, line in enumerate(open(0).read().split('\n')):
    for x, c in enumerate(line.strip()):
        maze[vec(x, y)] = c

start = next(k for k, v in maze.items() if v == 'S')
end = next(k for k, v in maze.items() if v == 'E')

tiles, gScore = search(maze, start, end)
debug_cost(maze, gScore)
debug_tiles(maze, tiles)

print(len(tiles))
