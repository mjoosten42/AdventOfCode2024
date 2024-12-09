list1 = []
list2 = []

numbers = map(int, open(0).read().split())

it = iter(numbers)

for i in it:
    list1.append(i)
    i = next(it)
    list2.append(i)

list1 = sorted(list1)
list2 = sorted(list2)

print(sum(map(lambda x: abs(x[0] - x[1]), zip(list1, list2))))



