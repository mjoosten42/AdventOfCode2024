def blink(stone, blinks, cache):
	ret=1

	if blinks > 0:
		if blinks in cache and stone in cache[blinks]:
			return cache[blinks][stone]
	
		if stone == 0:
			ret = blink(1, blinks - 1, cache)
		elif len(str(stone)) % 2 == 0:
			ret = blink(int(str(stone)[:len(str(stone))//2]), blinks - 1, cache) + blink(int(str(stone)[len(str(stone))//2:]), blinks - 1, cache)
		else:
			ret = blink(stone * 2024, blinks - 1, cache)

		if blinks not in cache:
			cache[blinks] = dict()
		
		cache[blinks][stone] = ret


	return ret

stones=[int(x) for x in open(0).read().strip().split()]

total=0
cache=dict()

for stone in stones:
	total += blink(stone, 75, cache)

print(total)