from vec import vec

def bfs(map, max, start):
    queue = [start]
    visited = set()
    heads = 0

    while queue:
        node = queue.pop(0)

        if map[node] == 9:
            heads += 1

        for dir in [vec(1, 0), vec(0, 1), vec(-1, 0), vec(0, -1)]:
            next = node + dir
            
            if next.is_inside(max) and next not in visited and next not in queue and map[next] == map[node] + 1:
                queue.append(next)
        
        visited.add(node)

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

print(sum(bfs(map, max, pos) for pos, height in map.items() if height == 0))

