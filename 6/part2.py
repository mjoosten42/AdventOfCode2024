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
obstructions=set()


for y in range(size):
	for x in range(size):
		c=map[y * (size + 1) + x]
		match c:
			case '#':
				walls.add(vec(x, y))
			case '^' | '>' | 'v' | '^':
				pos=vec(x, y)
				dir=vec(c)

start=(pos, dir)

while pos.x >= 0 and pos.x < size and pos.y >= 0 and pos.y < size:
	if pos not in visited:
		visited.add(pos)

	next = pos + dir

	while next in walls:
		dir = dir.rotate()
		next = pos + dir

	pos = next

for obstruction in visited:
	if obstruction != start[0]:
		pos, dir = start
		visited: dict[vec, list[vec]]={}

		while pos.x >= 0 and pos.x < size and pos.y >= 0 and pos.y < size:
			if pos not in visited:
				visited[pos] = [dir]
			else:
				if dir not in visited[pos]:
					visited[pos].append(dir)
				else:
					obstructions.add(obstruction)
					break

			next = pos + dir

			while next in walls or next == obstruction:
				dir = dir.rotate()
				next = pos + dir

			pos = next


if start[0] in obstructions:
	obstructions.remove(start[0])

print(len(obstructions))
