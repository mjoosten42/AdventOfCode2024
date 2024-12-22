def solve(n, k):
    for i in range(k):
        n = ((n <<  6) ^ n) & ((1 << 24) - 1)
        n = ((n >>  5) ^ n) & ((1 << 24) - 1)
        n = ((n << 11) ^ n) & ((1 << 24) - 1)
    
    return n

print(sum(solve(int(x.strip()), 2000) for x in open(0)))
