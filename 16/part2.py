from vec import vec
import sys

def path_cost(path):
    dir = vec(1, 0)
    cost = -1
    pos = path[0] - dir

    for node in path:
        cost += 1

        if node - pos != dir:
            cost += 1000
            dir = node - pos

        pos = node

    return cost

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

def tiles(maze, mainpath, gScore):
    start = next(k for k, v in maze.items() if v == 'S')
    end = next(k for k, v in maze.items() if v == 'E')
    paths = [[start]]
    tiles = set(mainpath)

    for node in mainpath:
        branches = [n for n in node.neighbours() if n in gScore and gScore[n] > gScore[node] and n not in mainpath]

        for branch in branches:
            paths = [[branch]]

            while paths:
                path = paths.pop(0)
                last = path[-1]

                for n in last.neighbours():
                    if n in tiles:
                        if gScore[last] - gScore[n] == 999:
                            tiles.update(path)
                            break;
                        

                    if n in gScore and gScore[n] > gScore[last]:
                        paths.append([*path, n])

    return tiles

def search(maze: dict[vec, str]):
    start = next(k for k, v in maze.items() if v == 'S')
    end = next(k for k, v in maze.items() if v == 'E')
    
    openSet = [start]
    cameFrom: dict[vec, vec] = {}
    gScore = { start: 0 }
    fScore = { start: h(start, end) }
    ret = None

    while openSet:
        node = min(openSet, key=lambda x: fScore[x])

        if node == end and ret == None:
            ret = (reconstruct(cameFrom, node), gScore)

        openSet.remove(node)

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
    
    return ret

maze = {}

for y, line in enumerate(open(0).read().split('\n')):
    for x, c in enumerate(line.strip()):
        maze[vec(x, y)] = c


path, gScore = search(maze)
debug_cost(maze, gScore)

tiles = tiles(maze, path, gScore)
debug_tiles(maze, tiles)

print(len(tiles))
