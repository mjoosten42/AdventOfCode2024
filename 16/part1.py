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
        path.append(pos)

    path.reverse()

    return path

def h(first, second):
    sub = abs(second - first)

    return (sub.x + sub.y)

def debug(maze, path):
    limit = max(maze)

    for y in range(limit.y + 1):
        for x in range(limit.x + 1):
            pos = vec(x, y)

            if pos in path:
                print('X', end='')
            else:
                print(maze[pos], end='')
        print()
    print()

def search(maze: dict[vec, str]):
    start = next(k for k, v in maze.items() if v == 'S')
    end = next(k for k, v in maze.items() if v == 'E')
    limit = max(maze)
    
    openSet = [start]
    cameFrom = {}
    gScore = { start: 0 }
    fScore = { start: h(start, end) }

    while openSet:
        node = min(openSet, key=lambda x: fScore[x])

        if node == end:
            return reconstruct(cameFrom, node)

        openSet.remove(node)

        for n in node.neighbours():
            if n in maze and maze[n] != '#':
                if n not in fScore:
                    fScore[n] = sys.maxsize
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
        
maze = {}

for y, line in enumerate(open(0).read().split('\n')):
    for x, c in enumerate(line.strip()):
        pos = vec(x, y)

        maze[pos] = c

path = search(maze)

print(path_cost(path))
