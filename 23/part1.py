def is_lan(graph, node):
    for conn in graph[node]:
        for after in graph[conn]:
            if node in graph[after]:
                yield sorted([node, conn, after])

graph = {}

for line in open(0):
    first = line[:2]
    second = line[3:5]

    if first not in graph:
        graph[first] = []

    if second not in graph:
        graph[second] = []

    graph[first].append(second)
    graph[second].append(first)

lans = []

for node in graph:
    for lan in is_lan(graph, node):
        if lan not in lans:
            lans.append(lan)

lans.sort()

print(sum(1 for lan in lans if any(map(lambda x: x.startswith('t'), lan))))

