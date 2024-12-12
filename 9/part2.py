def point(to, fro):
    first = 1 + to * 3
    second = 1 + fro * 3

    print(f"{' ' * (first)}^{' ' * (second - first - 1)}^")


def debug(fs):
    for i, digit in enumerate(fs):
        digit = int(digit)

        if i % 2:
            print('.' * digit, end='')
        else:
            print(str(i // 2) * digit, end='')

    print()

fs=[int(x) for x in open(0).read().strip()]

debug(fs)

fileptr = len(fs) - (1 - len(fs) % 2) - 1

while fileptr >= 0:
    freeptr = 1
    file_size = fs[fileptr]
    
    while freeptr < len(fs):
        free_size = fs[freeptr]

        if free_size >= file_size:
            print(fs)
            point(freeptr, fileptr)

            fs[freeptr] = 0
        

            break

        freeptr += 2

    fileptr -= 2
    


debug(fs)
