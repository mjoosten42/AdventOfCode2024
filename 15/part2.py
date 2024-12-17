from vec import vec

def debug(walls, boxes, robot, size):
	for y in range(size):
		for x in range(2 * size):
			pos = vec(x, y)
	
			if pos in walls:
				print('#', end='')
			elif pos in boxes:
				print('[', end='')
			elif pos == robot:
				print('@', end='')
			else:
				if pos - vec(1, 0) in boxes:
					print(']', end='')
				else:
					print('.', end='')
		print()
	print()

all = open(0).read().split('\n\n')

walls = set()
boxes = set()
robot = vec(0, 0)
size = all[0].index('\n')

for y, line in enumerate(all[0].split('\n')):
	for x, c in enumerate(line.strip()):
		pos = vec(2 * x, y)
	
		match c:
			case '#':
				walls.add(pos)
				walls.add(pos + vec(1, 0))
			case 'O':
				boxes.add(pos)
			case '@':
				robot = pos

moves = list(all[1].strip('\n'))

while moves:
	move = vec(moves.pop(0))
	forces = [robot]
	visited = []
	hitboxes = []
	hitwall = False

	while forces:
		f = forces.pop(0)

		if f in visited:
			continue

		next = f + move

		if next in walls:
			hitwall = True
			break

		if next in boxes:
			forces.append(next)
			forces.append(next + vec(1, 0))

		if next - vec(1, 0) in boxes:
			forces.append(next)
			forces.append(next - vec(1, 0))

		visited.append(f)

	if not hitwall:
		visited.reverse()

		for v in visited:
			if v in boxes:
				boxes.add(v + move)
				boxes.remove(v)

		robot += move

total = sum(box.x + 100 * box.y for box in boxes)

print(total)
