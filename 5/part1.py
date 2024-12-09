i = open(0).read().replace('|', ',').split("\n\n")
rules, manuals = map(lambda l: map(lambda k: [*map(int, k.split(','))], str.split(l)), i)

print(*rules)
print()
print(*manuals)

