[init, gates] = [x.split('\n') for x in open(0).read().strip().split('\n\n')]

for line in init:
    exec(line.replace(':', ' ='))

defined = set([x for x in locals() if len(x) == 3])

for i in range(len(gates)):
    gates[i] = gates[i].replace('AND', '&').replace('XOR', '^').replace('OR', '|')
    gates[i] = gates[i][13:] + ' = ' + gates[i][:9]

while gates:
    for gate in gates:
        result = gate[:3]
        first = gate[6:9]
        second = gate[12:]

        if first in defined and second in defined:
            exec(gate)
            defined.add(result)
            gates.remove(gate)

n = 0

for d in defined:
    if d.startswith('z'):
        n |= (eval(d) << int(d[1:3]))

print(n)
