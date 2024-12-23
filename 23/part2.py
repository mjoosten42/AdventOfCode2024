def remove(graph, node):
    for nb in graph[node]:
        graph[nb].remove(node)
    graph.remove(nodei)

def lansize(graph, node):
    size = 2

    relevant = set(graph[node])

    return size

def make_graph():
    graph = {}

    for line in open(0):
        first = line[:2]
        second = line[3:5]
        
        graph.setdefault(first, set()).add(second)
        graph.setdefault(second, set()).add(first)

    return graph

graph = make_graph()

print(len(graph))

print(lansize(graph, 'kh'))
