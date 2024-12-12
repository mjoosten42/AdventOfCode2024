def point(to, fro):
    first = 1 + to * 3
    second = 1 + fro * 3

    print(f"{' ' * (first)}^{' ' * (second - first - 1)}^")

def debug(fs, ids):
    id = 0;

    print(fs)
    print(ids)

    for i, digit in enumerate(fs):
        digit = int(digit)

        if i % 2:
            print('.' * digit, end='')
        else:
            print(str(ids[i]) * digit, end='')

            if digit > 0:
                id += 1

    print()

fs = [int(x) for x in open(0).read().strip()]
ids = [0 if i % 2 else i // 2 for i, _ in enumerate(fs)]
id = max(ids)

while id >= 0:
    freeptr = 1
    fileptr = ids.index(id)
    file_size = fs[fileptr]
    
    while freeptr < fileptr:
        free_size = fs[freeptr]

        if free_size >= file_size:
            fs[freeptr] = 0
            fs.insert(freeptr + 1, file_size)
            fs.insert(freeptr + 2, free_size - file_size)

            fs[fileptr + 1] += file_size
            fs[fileptr + 2] = 0

            ids.insert(freeptr + 1, id)
            ids.insert(freeptr + 2, 0)
            ids[fileptr + 2] = 0

            break

        freeptr += 2
    
    id -= 1

total = 0
block = 0

for i, digit in enumerate(fs):
    digit = int(digit)

    if not i % 2:
        for j in range(block, block + digit):
            total += j * ids[i]

        if digit > 0:
            id += 1

    block += digit

print(total)
