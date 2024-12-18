from vec import vec
from astar import astar

def debug(maze, path, size):
    for y in range(size):
        for x in range(size):
            pos = vec(x, y)
    
            if pos in path:
                print('O', end='')
            else:
                print(maze[vec(x, y)], end='')
        print()

walls = [vec(int(x), int(y)) for [x, y] in [line.strip().split(',') for line in open(0)]]
size = 71
maze = {}

for y in range(size):
    for x in range(size):
        maze[vec(x, y)] = '.'

for i in range(1024):
    maze[walls[i]] = '#'

path = astar(maze, vec(0, 0), vec(size - 1, size - 1))

print(len(path) - 1)

