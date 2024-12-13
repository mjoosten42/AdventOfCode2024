import re
from vec import vec

total = 0

for box in open(0).read().split('\n\n'):
    vecs = list(vec(a, b) for a, b in (list(int(x) for x in re.findall('\d+', line)) for line in box.strip('\n').split('\n')))
    
    for i in range(100):
        for j in range(100):
            pos = vecs[0] * i + vecs[1] * j

            if pos == vecs[2]:
                total += (i * 3 + j)

print(total)

