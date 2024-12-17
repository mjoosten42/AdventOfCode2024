import time
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

	def pos(self, seconds, max):
		return (self.p + self.v * seconds) % max

def debug(robots, max, i):
	hall = set(r.pos(i, max) for r in robots)

	for y in range(max.y):
		for x in range(max.x):
			pos = vec(x, y)

			if pos in hall:
				print('#', end='')
			else:
				print('.', end='')
		print()

def solve(robots, max, i):
	hall = set(r.pos(i, max) for r in robots)

	for y in range(max.y):
		for x in range(max.x):
			row = 0
			pos = vec(x, y)

			if pos in hall:
				while pos + vec(row, 0) in hall:
					row += 1

					if row >= 9:
						debug(robots, max, i)
						print(i)
						exit()

robots = set()
max = vec(101, 103)

for line in open(0):
	numbers = list(int(x) for x in re.findall('-?\d+', line))

	robots.add(robot(vec(numbers[0], numbers[1]), vec(numbers[2], numbers[3]))) 

i = 0
while True:
	solve(robots, max, i)

	i += 1

