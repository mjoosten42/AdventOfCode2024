from vec import vec
import sys

def search(maze, start, end):
    queue: list[tuple[int, list[vec]]] = [(0, [start])]
    shortest = (sys.maxsize, [])
    score = { pos: sys.maxsize for pos in maze }
    score[start] = 0

    while queue:
        cost, path = queue.pop(0)
        node = path[-1]

        print(len(path), end='\r')

        if node == end and cost <= shortest[0]:
            if cost < shortest[0]:
                shortest = (cost, [])
            shortest[1].append(path)

        for n in node.neighbours():
            if n in maze and maze[n] != '#' and n not in path:
                olddir = vec(1, 0) if len(path) < 2 else node - path[-2]
                add = 1 if olddir == n - node else 1001
                newcost = cost + add

                if newcost < score[n]:
                    score[n] = newcost

                if newcost < score[n] + 2000:
                    queue.append((newcost, [*path.copy(), n]))

    return shortest[1]

maze = {}

for y, line in enumerate(open(0).read().split('\n')):
    for x, c in enumerate(line.strip()):
        maze[vec(x, y)] = c

start = next(k for k, v in maze.items() if v == 'S')
end = next(k for k, v in maze.items() if v == 'E')

paths = search(maze, start, end)
tiles = set([node for path in paths for node in path])

print(len(tiles))
