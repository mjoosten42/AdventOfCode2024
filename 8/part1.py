from vec import vec

file=open(0).read()
size=file.index('\n')
max=vec(size, size)

frequencies: dict[str, set[vec]]=dict()
antinodes = set()

for y in range(size):
	for x in range(size):
		c=file[y * (size + 1) + x]
		if c != '.':
			if c not in frequencies:
				frequencies[c] = set()
			
			frequencies[c].add(vec(x, y))

for antennas in frequencies.values():
	for antenna in antennas:
		for other in [x for x in antennas.copy() if x != antenna]:
			sub = other - antenna
			antinode = antenna - sub

			if antinode.is_inside(max):
				antinodes.add(antinode)

print(len(antinodes))