import itertools

def dir():
	for i in [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1], [0, -1], [1,-1]]:
		yield i

def gen(grid, point, max):
	for d in dir():
		for i in range(4):
			p = [point[0] + d[0] * i, point[1] + d[1] * i]

			if p[0] >= 0 and p[0] < max[0] and p[1] >= 0 and p[1] < max[1]:
				yield grid[p[1]][p[0]]
			else:
				yield ' '


grid=[*open(0)]

max = [len(grid), len(grid[0]) - 1]

total=0

for j in range(max[1]):
	for i in range(max[0]):
		s = itertools.islice(gen(grid, [i, j], max), 4 * 8)
		
		for n in range(8):
			sl = ''.join(list(itertools.islice(s, 4)))
			
			if (sl == "XMAS"):
				total += 1

print(total)