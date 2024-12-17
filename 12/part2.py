from vec import vec

def to_farm(pos):
    return vec((pos.x - 1) // 2, (pos.y - 1) // 2)

def bfs(farm, visited, max, start):
    queue = [start]
    area = set()
    all_fences = []
    sides = 0
    crop = farm[start]

    while queue:
        node = queue.pop(0)
        nb = node.inside_neighbours(max)
        fences = 4 - len(nb)

        for n in node.neighbours():
            sub = n - node
            middle = node * 2 + vec(1, 1)

            if not n.is_inside(max) or farm[n] != farm[node]:
                all_fences.append(middle + sub)

        for next in nb:
            if next not in area and next not in visited and next not in queue and farm[next] == farm[node]:
                queue.append(next)

        area.add(node)

    visited.update(area)

    while all_fences:
        fence = all_fences.pop(0)
        step = vec(2, 0) if fence.y % 2 == 0 else vec(0, 2)
        sides += 1

        crop_step = vec(0, 0)
        for x in fence.inside_neighbours(max * 2 + vec(1, 1)):
            if x.x % 2 and x.y % 2:
                fpos = to_farm(x)
                if fpos in farm and farm[fpos] == crop:
                    crop_step = x - fence
                    break

        first = fence + step
        second = fence - step

        while first.is_inside(max * 2 + vec(1, 1)) and first in all_fences and farm[to_farm(first + crop_step)] == crop:
            all_fences.remove(first)
            first = first + step
        
        while second.is_inside(max * 2 + vec(1, 1)) and second in all_fences and farm[to_farm(second + crop_step)] == crop:
            all_fences.remove(second)
            second = second - step
        
    ret = len(area) * sides

    return ret

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

