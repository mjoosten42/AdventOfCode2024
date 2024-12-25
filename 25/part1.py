locks = []
keys = []

for block in open(0).read().split('\n\n'):
    is_lock = block[0] == '#'
    lines = block.split('\n')
    heights = [0, 0, 0, 0, 0]

    for line in lines[1:6]:
        for j, c in enumerate(line.strip()):
            if c == '#':
                heights[j] += 1

    if is_lock:
        locks.append(heights)
    else:
        keys.append(heights)

total = 0

for lock in locks:
    for key in keys:
        total += all(map(lambda x: x <= 5, map(sum, zip(key, lock))))

print(total)
