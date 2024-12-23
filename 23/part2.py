def bron_kerbosh(graph, r, p, x):
    if not p and not x:
        yield r

    for v in p.copy():
        yield from bron_kerbosh(graph, r | { v }, p.intersection(graph[v]), x.intersection(graph[v]))
        p.remove(v)
        x = x | { v }

def make_graph():
    graph = {}

    for line in open(0):
        first = line[:2]
        second = line[3:5]
        
        graph.setdefault(first, set()).add(second)
        graph.setdefault(second, set()).add(first)

    return graph

graph = make_graph()
best, lan = 0, []

for a in bron_kerbosh(graph, set(), set(graph), set()):
    if len(a) > best:
        best = len(a)
        lan = a

print(','.join(sorted(lan)))
