import pygame

i=open(0).read()
l=i.index('\n')

walls=[]
pos=pygame.math.Vector2(0, 0)
pos=pygame.math.Vector2(0, 0)
visited=[]

for y in range(l):
    for x in range(l):
        c=i[y * (l + 1) + x]
        match c:
            case '#':
                walls.append([x, y])
            case '^' | '>' | 'v' | '^':
                pos=pygame.math.Vector2([x, y])
                match c:
                    case '^':
                        dir=pygame.math.Vector2([0, -1])
                    case '>':
                        dir=pygame.math.Vector2([1, 0])
                    case 'v':
                        dir=pygame.math.Vector2([0, 1])
                    case '<':
                        dir=pygame.math.Vector2([-1, 0])

while pos.x >= 0 and pos.x < l and pos.y >= 0 and pos.y < l:
    if pos not in visited:
        visited.append(pos)

    next = pos + dir

    if (walls.count(next)):
        dir.rotate_ip(90)
        next = pos + dir

    pos = next

print(len(visited))
