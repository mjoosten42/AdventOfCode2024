def debug(fs: list[int]):
	for c in fs:
		if c == -1:
			print('.', end='')
		else:
			print(c, end='')
	print()

input=open(0).read().strip()
fs: list[int] = []
block = 0

for occupied, blocksize in enumerate(input):
	id = occupied // 2

	for j in range(int(blocksize)):
		fs.append(id if not occupied % 2 else -1)

left, right = (0, len(fs) - 1)

while left < right:
	while fs[left] != -1 and left < right:
		left += 1

	while fs[right] == -1 and left < right:
		right -= 1

	fs[left] = fs[right]
	fs[right] = -1

print(sum(i * id if id != -1 else 0 for i, id in enumerate(fs)))