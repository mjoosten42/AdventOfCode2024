def pack(changes):
    total = 0

    for i in range(4):
        total |= ((changes[i] + 10) << (i * 8))

    return total

def unpack(n):
    ret = [0, 0, 0, 0]

    for i in range(4):
        ret[i] = ((n & ((1 << 8) - 1) << (i * 8)) >> (i * 8)) - 10

    return ret

def price(n, k):
    prices = [n % 10, *[None] * k]

    for i in range(k):
        n = ((n <<  6) ^ n) & ((1 << 24) - 1)
        n = ((n >>  5) ^ n) & ((1 << 24) - 1)
        n = ((n << 11) ^ n) & ((1 << 24) - 1)
        
        prices[i + 1] = n % 10

    return prices

def solve(monkeys, k):
    prices = [price(monkey, k) for monkey in monkeys]
    changes = [[x[i] - x[i - 1] for i, _ in enumerate(x) if i] for x in prices]
    sequences = { }
    
    for m in range(len(monkeys)):
        sequences[m] = {}

        for i in range(k - 3):
            seq = changes[m][i:i + 4]
            packed = pack(seq)
        
            if packed not in sequences[m]:
                sequences[m][packed] = prices[m][i + 4]

    summed = {}

    for m in range(len(monkeys)):
        for packed in sequences[m]:
            if packed not in summed:
                summed[packed] = 0

            summed[packed] += sequences[m][packed]

    return max(summed.values())

print(solve([int(x.strip()) for x in open(0)], 2000))
