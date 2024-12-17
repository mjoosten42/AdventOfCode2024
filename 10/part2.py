from vec import vec

def bfs(map, max, start):
    queue = [[start]]
    heads = 0

    while queue:
        node = queue.pop(0)
        last = node[-1]

        if map[last] == 0:
            heads += 1

        for dir in [vec(1, 0), vec(0, 1), vec(-1, 0), vec(0, -1)]:
            next = last + dir
            
            if next.is_inside(max) and next not in node and map[next] == map[last] - 1:
                queue.append([*node.copy(), next])

    return heads

map = {}
max = vec(0, 0)

for y, line in enumerate(open(0)):
    for x, c in enumerate(line.strip()):
        map[vec(x, y)] = int(c)

        if x > max.x:
            max.x = x
        
        if y > max.y:
            max.y = y

max += vec(1, 1)

print(sum(bfs(map, max, pos) for pos, height in map.items() if height == 9))

