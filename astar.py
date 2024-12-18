import sys
from vec import vec

def reconstruct(cameFrom, pos):
    path = [pos]
    
    while pos in cameFrom:
        pos = cameFrom[pos]
        path.append(pos)

    path.reverse()

    return path

def h(first, second):
    tmp = abs(second - first)

    return tmp.x + tmp.y

def astar(maze: dict[vec, str], start: vec, end: vec):
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
                
                tentative_gScore = gScore[node] + 1

                if tentative_gScore < gScore[n]:
                    cameFrom[n] = node
                    gScore[n] = tentative_gScore
                    fScore[n] = tentative_gScore + h(n, end)

                    if n not in openSet:
                        openSet.append(n)
        

