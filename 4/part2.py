t=[*open(0)]
l=len(t)

total=0

for y in range(1, l - 1):
	for x in range(1, l - 1):
		if t[y][x] == 'A':
			str=''.join([t[y - 1][x - 1], t[y - 1][x + 1], t[y + 1][x + 1], t[y + 1][x - 1]])

			match str:
				case "MMSS" | "SMMS" | "SSMM" | "MSSM":
					total += 1

print(total)