l,r=zip(*map(str.split, open(0)))

print(sum((r.count(x) * int(x)) for x in l))