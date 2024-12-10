import pygame

i=open(0).read()
l=i.index('\n')

walls=[]
start_pos=pygame.math.Vector2(0, 0)
start_dir=pygame.math.Vector2(0, 0)

for y in range(l):
    for x in range(l):
        c=i[y * (l + 1) + x]
        match c:
            case '#':
                walls.append(pygame.math.Vector2(x, y))
            case '^' | '>' | 'v' | '^':
                start_pos=pygame.math.Vector2([x, y])
                match c:
                    case '^':
                        start_dir=pygame.math.Vector2([0, -1])
                    case '>':
                        start_dir=pygame.math.Vector2([1, 0])
                    case 'v':
                        start_dir=pygame.math.Vector2([0, 1])
                    case '<':
                        start_dir=pygame.math.Vector2([-1, 0])

obstructions=[]

for y in range(l):
    for x in range(l):
        o=pygame.math.Vector2(x, y)
       
        if o == start_pos or o in walls:
            continue

        walls.append(o)
        visited=[]

        pos=start_pos
        dir=start_dir
        
        while pos.x >= 0 and pos.x < l and pos.y >= 0 and pos.y < l:
            vis=[*(x for (x, y) in visited)]

            if pos in vis:
                if visited[vis.index(pos)][1].angle_to(dir) < 5:
                    print('obstruction: ', o)
                    obstructions.append(o)
                    break
            else:
                visited.append((pos.copy(), dir.copy()))
        
            next = pos + dir
        
            if (walls.count(next)):
                dir.rotate_ip(90)
                next = pos + dir
        
            pos = next

        walls.remove(o)

print(len(obstructions))
