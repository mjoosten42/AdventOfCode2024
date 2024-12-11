def can_make(numbers):
	match len(numbers):
		case 1:
			return [numbers[0]]
		case 2:
			return [numbers[0] * numbers[1], numbers[0] + numbers[1], int(str(numbers[0]) + str(numbers[1]))]
		case _:
			next = can_make(numbers[:-1])
			first = [numbers[-1] * n for n in next]
			second = [numbers[-1] + n for n in next]
			third = [int(str(n) + str(numbers[-1])) for n in next]

			return first + second + third
		
input=map(lambda l: list(int(x.strip(':')) for x in l), map(str.split, open(0)))

total=0

for equation in input:
	first = equation.pop(0)
	numbers = can_make(equation)	

	if first in numbers:
		total += first

print(total)
