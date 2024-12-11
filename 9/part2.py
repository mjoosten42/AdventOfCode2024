def filesize(fs: list[int], id, start=0):
	if id not in fs[start:]:
		return (-1, -1)

	index = fs.index(id, start)
	end = index

	while end < len(fs) and fs[end] == id:
		end += 1

	return (index, end - index)


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
max = 0

for occupied, blocksize in enumerate(input):
	max = occupied // 2

	for j in range(int(blocksize)):
		fs.append(max if not occupied % 2 else -1)

for id in range(max, -1, -1):
	print(id)
	file_index, file_size = filesize(fs, id)
	free_index, free_size = (0, 0)

	while free_index >= 0:
		free_index, free_size = filesize(fs, -1, free_index)

		if free_size >= file_size and free_index < file_index:
			for i in range(free_index, free_index + file_size):
				fs[i] = id

			for i in range(file_index, file_index + file_size):
				fs[i] = -1

			break

		free_index += free_size

print(sum(i * id if id != -1 else 0 for i, id in enumerate(fs)))