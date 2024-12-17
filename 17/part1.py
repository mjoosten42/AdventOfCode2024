import re

numbers = [int(x) for x in re.findall('\d+', open(0).read())]

a, b, c, program, out = numbers[0], numbers[1], numbers[2], numbers[3:], []

ip = 0
end = len(program)

while ip < end - 1:
    opcode = program[ip]
    literal = program[ip + 1]
    combo = literal if literal < 4 else [a, b, c][literal - 4]
    add = 2

    match opcode:
        case 0:
            a = a // (2 ** combo) 
        case 1:
            b = b ^ literal
        case 2:
            b = combo % 8
        case 3:
            if a and ip != literal:
                ip = literal
                add = 0
        case 4:
            b = b ^ c
        case 5:
            out.append(combo % 8)
        case 6:
            b = a // (2 ** combo)
        case 7:
            c = a // (2 ** combo)

    ip += add


print(','.join(str(n) for n in out))
