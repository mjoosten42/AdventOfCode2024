import random

input=map(lambda l: list(int(x.strip(':')) for x in l), map(str.split, open(0)))

total=0

for e in input:
    nb = e.pop(0)
    for n in range(1000):
        l=len(e)
        s=''
        for j in range(l - 1):
            s += '('
        for (i, elem) in enumerate(e):
                
            s += str(elem)
   
            if i > 0:
                s += ')'

            if i < l - 1:
                if random.randint(0, 1):
                    s += '+'
                else:
                    s += '*'
   

        res = eval(s)
        if res == nb:
            total += nb
            break

print(total)

