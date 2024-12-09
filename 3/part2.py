import re
import functools

def f(acc, m):
    match m[0][:3]:
        case "mul":
            if acc[0] == 1:
                acc[1] += int(m[1]) * int(m[2])
        case "do(":
            acc[0] = 1
        case "don":
            acc[0] = 0
    
    return acc
            

print(functools.reduce(f, re.findall("(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", open(0).read()), [1, 0])[1])