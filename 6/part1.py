from vec import vec

def debug(size, map, visited):
	for y in range(size):
		for x in range(size):
			if vec(x, y) in visited:
				print('X', end='')
			else:
				print(map[y * (size + 1) + x], end='')
		print()

map=open(0).read()
size=map.index('\n')

pos=vec(0, 0)
dir=vec(0, 0)
visited=set()
walls=set()

for y in range(size):
	for x in range(size):
		c=map[y * (size + 1) + x]
		match c:
			case '#':
				walls.add(vec(x, y))
			case '^' | '>' | 'v' | '^':
				pos=vec(x, y)
				dir=vec(c)

while pos.x >= 0 and pos.x < size and pos.y >= 0 and pos.y < size:
	if pos not in visited:
		visited.add(pos)

	next = pos + dir

	while next in walls:
		dir = dir.rotate()
		next = pos + dir

	pos = next

print(len(visited))
