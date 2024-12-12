from vec import vec

def bfs(farm, visited, max, start):
    queue = [start]
    area = set()
    total = 0

    while queue:
        node = queue.pop(0)
        nb = node.inside_neighbours(max)
        total += 4 - len(nb) + len([x for x in nb if farm[x] != farm[node]])

        for next in nb:
            if next not in area and next not in visited and next not in queue and farm[next] == farm[node]:
                queue.append(next)

        area.add(node)

    visited.update(area)

    return total * len(area) 

farm: dict[vec, str] = {}
visited = set()
size = 0

for y, line in enumerate(open(0)):
    size = len(line) - 1
    for x, crop in enumerate(line.strip()):
        farm[vec(x, y)] = crop

max = vec(size, size)

total = 0

for y in range(size):
    for x in range(size):
        pos = vec(x, y)

        if pos not in visited:
            total += bfs(farm, visited, max, pos)

print(total)

