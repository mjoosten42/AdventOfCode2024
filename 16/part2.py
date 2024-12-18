from vec import vec
import sys

def reconstruct(cameFrom, pos):
    path = [pos]

    while pos in cameFrom:
        pos = cameFrom[pos]
        path.insert(0, pos)

    return path

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
    cameFrom: dict[vec, vec] = {}
    gScore = { start: 0 }
    fScore = { start: h(start, end) }

    while openSet:
        node = min(openSet, key=lambda x: fScore[x])

        openSet.remove(node)

        if node == end:
            return reconstruct(cameFrom, node), gScore

        for n in node.neighbours():
            if n in maze and maze[n] != '#':
                if n not in fScore:
                    gScore[n] = sys.maxsize
                
                cost = 1
    
                if n - node != (vec(1, 0) if node not in cameFrom else node - cameFrom[node]):
                    cost += 1000

                tentative_gScore = gScore[node] + cost

                if tentative_gScore < gScore[n]:
                    cameFrom[n] = node
                    gScore[n] = tentative_gScore
                    fScore[n] = tentative_gScore + h(n, end)

                    if n not in openSet:
                        openSet.append(n)

    return None, None

maze = {}

for y, line in enumerate(open(0).read().split('\n')):
    for x, c in enumerate(line.strip()):
        maze[vec(x, y)] = c

start = next(k for k, v in maze.items() if v == 'S')
end = next(k for k, v in maze.items() if v == 'E')

path, gScore = search(maze, start, end)

tiles = set(path)

for i, node in enumerate(path):
    print(f"{100 * i // len(path)}%", end='\r')

    if node != start and node != end:
        maze[node] = '#'

        p, score = search(maze, start, end)

        if score and end in score and score[end] == gScore[end]:
            tiles.update(p)

        maze[node] = '.'

debug_tiles(maze, tiles)

print(len(tiles))
