import re

def solve(program, numbers):
    out = []
    
    if len(numbers) == 1:
        for i in range(8):
            if next(compute(i, program)) == numbers[0]:
                out.append(i)
    else:
        prev = solve(program, numbers[1:])
        
        for p in prev:
            for i in range(8):
                n = (p << 3) + i
               
                if next(compute(n, program)) == numbers[0]:
                    out.append(n)

    return out

def debug(program):
    ip = 0
    end = len(program)
    
    while ip < end - 1:
        opcode = program[ip]
        literal = program[ip + 1]
        combo = literal

        match combo:
            case 4:
                combo = 'a'
            case 5:
                combo = 'b'
            case 6:
                combo = 'c'

        match opcode:
            case 0:
                print(f"adv: a = a >> {combo}")
            case 1:
                print(f"bxl: b = b ^ {literal}")
            case 2:
                print(f"bst: b = {combo} % 8")
            case 3:
                print(f"jnz: ip = {literal}")
            case 4:
                print(f"bxc: b = b ^ c")
            case 5:
                print(f"out: {combo} % 8") 
            case 6:
                print(f"bdv: b = a >> {combo}")
            case 7:
                print(f"cdv: c = a >> {combo}")

        ip += 2


def compute(a, numbers):
    b, c, program = numbers[1], numbers[2], numbers[3:]
    
    ip = 0
    end = len(program)
    
    while ip < end - 1:
        opcode = program[ip]
        literal = program[ip + 1]
        combo = literal if literal < 4 else [a, b, c][literal - 4]
        add = 2

        match opcode:
            case 0:
                a = a >> combo
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
                yield combo % 8
            case 6:
                b = a >> combo
            case 7:
                c = a >> combo
    
        ip += add

numbers = [int(x) for x in re.findall('\d+', open(0).read())]

print(min(solve(numbers, numbers[3:])))
