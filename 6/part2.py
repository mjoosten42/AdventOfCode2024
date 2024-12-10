from vec import vec

i=open(0).read()
l=i.index('\n')

walls=set()
start_pos=vec(0, 0)
start_dir=vec(0, 0)

for y in range(l):
    for x in range(l):
        c=i[y * (l + 1) + x]
        match c:
            case '#':
                walls.add(vec(x, y))
            case '^' | '>' | 'v' | '^':
                start_pos=vec(x, y)
                start_dir=vec(c)

obstructions=[]

pos=start_pos
dir=start_dir

while pos.x >= 0 and pos.x < l and pos.y >= 0 and pos.y < l:
    visited={}
    rot = dir
    cpy = pos
    n = pos + dir

    if n not in walls and n.x >= 0 and n.x < l and n.y >= 0 and n.y < l:
        walls.add(n)
    
        while cpy.x >= 0 and cpy.x < l and cpy.y >= 0 and cpy.y < l:
            if cpy in visited and visited[cpy] == rot:
                obstructions.append(n)
                break
    
            if cpy not in visited:
                visited[cpy] = rot
            
            while cpy + rot in walls:
                rot = rot.rotate()
    
            cpy = cpy + rot
    
        walls.remove(n)
   
    while pos + dir in walls:
        dir = dir.rotate()

    pos = pos + dir

print(len(obstructions))
