from vec import vec
import re

class robot:
	p = vec(0, 0)
	v = vec(0, 0)

	def __init__(self, p, v):
		self.p = p
		self.v = v

	def __repr__(self):
		return f"[{self.p}, {self.v}]"

def debug(robots, max, middle):
	for y in range(max.y):
		for x in range(max.x):
			n = len(list(r for r in robots if r.p == vec(x, y)))
	
			if False: #x == middle.x or y == middle.y:
				print(' ',end='')
			elif n:
				print(n, end='')
			else:
				print('.', end='')
		print()
	print('#' * max.x)

robots = []
max = vec(101, 103)
middle = vec(max.x // 2, max.y // 2)

for line in open(0):
	numbers = list(int(x) for x in re.findall('-?\d+', line))

	robots.append(robot(vec(numbers[0], numbers[1]), vec(numbers[2], numbers[3]))) 

for _ in range(100):
	for r in robots:
		r.p += r.v
		r.p = r.p % max
		r.p += max
		r.p = r.p % max

quadrants = [0, 0, 0, 0]

for r in robots:
    if r.p.x < middle.x and r.p.y < middle.y:
        quadrants[0] += 1
    if r.p.x > middle.x and r.p.y < middle.y:
        quadrants[1] += 1
    if r.p.x < middle.x and r.p.y > middle.y:
        quadrants[2] += 1
    if r.p.x > middle.x and r.p.y > middle.y:
        quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

