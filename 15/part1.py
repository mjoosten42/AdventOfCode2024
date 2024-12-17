from vec import vec

def debug(walls, boxes, robot, size):
	for y in range(size):
		for x in range(size):
			pos = vec(x, y)
	
			if pos in walls:
				print('#', end='')
			elif pos in boxes:
				print('O', end='')
			elif pos == robot:
				print('@', end='')
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
		pos = vec(x, y)
	
		match c:
			case '#':
				walls.add(pos)
			case 'O':
				boxes.add(pos)
			case '@':
				robot = pos

moves = list(all[1].strip('\n'))

while moves:
	move = vec(moves.pop(0))
	next = robot + move

	while next in boxes and next not in walls:
		next = next + move

	if next in walls:
		continue

	boxes.add(next)
	boxes.remove(robot + move)
	robot = robot + move

total = sum(box.x + 100 * box.y for box in boxes)

print(total)
