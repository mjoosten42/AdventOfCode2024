import re
from vec import vec
from line import line

total = 0

for box in open(0).read().split('\n\n'):
    vecs = list(vec(a, b) for a, b in (list(int(x) for x in re.findall('\d+', line)) for line in box.strip('\n').split('\n')))
    target = vecs[2] + vec(10000000000000, 10000000000000)

    # Cramer
    a = (target.x * vecs[1].y - target.y * vecs[1].x) / (vecs[0].x * vecs[1].y - vecs[0].y * vecs[1].x)
    b = (vecs[0].x * target.y - vecs[0].y * target.x) / (vecs[0].x * vecs[1].y - vecs[0].y * vecs[1].x)

    print(a, b)

    if float.is_integer(a) and float.is_integer(b):
        total += (a * 3 + b)

print(int(total))

