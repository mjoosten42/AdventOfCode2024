def run(x, y, gates):
    defined = { f"x{i:02}": ((x & (1 << i)) >> i) for i in range(64) } | { f"y{i:02}": ((y & (1 << i)) >> i) for i in range(64) }
    z = 0
    cpy = gates.copy()

    while cpy:
        for first, op, second, res in cpy.copy().values():
            if first in defined and second in defined:
                defined[res] = eval(str(defined[first]) + op + str(defined[second]))
                del cpy[res]

                if res.startswith('z'):
                    z = z | ((defined[res]) << int(res[1:3]))

    return z

def dependants(gates, wires):
    for wire in wires:
        yield wire
        
        if wire in gates:
            yield from dependants(gates, [gates[wire][0], gates[wire][2]])

def solve(x, y, gates):
    z = run(x, y, gates)
    
    first_line = []
    second_line = []
    sus = ['z12']

    for i in range(44):
        a = f"x{i:02}"
        b = f"y{i:02}"

        for op in '^&':
            for first, ope, second, res in gates.values():
                if a == first and b == second and op == ope:
                    first_line.append(res)

    first_line.remove('z00')
    first_line.remove('z12')
    
    print(len(first_line))
    print(first_line)

    for gate in first_line:
        first, op, second, res = gates[gate]

        if op == '&':
            for f, o, s, r in gates.values():
                if r[0] == 'z' and r[1].isdigit():
                    second_line.append(r)

x, y = 0, 0
bits = 0
gates = {}

for line in map(str.strip, open(0)):
    if ':' in line:
        n = int(line[1:3])

        if n > bits:
            bits = n

        if 'x' in line:
            x = x | (int(line[5:6]) << n)
        
        if 'y' in line:
            y = y | (int(line[5:6]) << n)

    if '->' in line:
        a = line.replace('AND', '&').replace('XOR', '^').replace('OR', '|')
        
        first = a[0:3]
        op = a[4:5]
        second = a[6:9]
        res = a[13:16]

        if second < first:
            first, second = second, first

        gates[res] = (first, op, second, res)

solve(x, y, gates)

