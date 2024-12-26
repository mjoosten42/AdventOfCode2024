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
    tmp = ['kwb', 'jqn', 'rwq', 'tgr', 'z12', 'z13', 'z16', 'z24']

    for i in range(2, 45):
        a = f"x{i:02}"
        b = f"y{i:02}"
        c = f"z{i:02}"

        amin = f"x{i-1:02}"
        bmin = f"y{i-1:02}"

        end = gates[c]

        if end[1] != '^':
            print('No XOR end:', end, c)
            continue

        prf, dvr = gates[end[0]], gates[end[2]]

        if prf[1] == '^':
            prf, dvr = dvr, prf

        if prf[1] == '^' and dvr[1] == '^':
            print('Two XORS:', end, prf, dvr)

        if dvr[0] != a or dvr[2] != b:
            print('Should be for x and y:', end, dvr)

        if prf[0] == a or prf[0] == b or prf[2] == a or prf[2] == b:
            print('Should NOT be for x and y:', end, prf)
            continue

        svv, vpp = gates[prf[0]], gates[prf[2]]

        if svv[1] != '&':
            print('Should be AND:', end, prf, svv)

        if vpp[1] != '&':
            print('Should be AND:', end, prf, vpp)

        if not ((svv[0] == amin and svv[2] == bmin) or (vpp[0] == amin or vpp[2] == bmin)):
            print('One should be from x and y:', end, vpp, svv)
            continue

        if svv[0].startswith(('x', 'y')):
            svv, vpp = vpp, svv

        tcb, ptp = gates[svv[0]], gates[svv[2]]

        if (tcb[1] == '^' and ptp[1] == '^') or (tcb[1] == '^' and ptp[1] == '^'):
            print("Should be from XOR and OR:", end, prf, dvr, svv, tcb, ptp, gates['pgp'])


    print(','.join(sorted(tmp)))

        
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

