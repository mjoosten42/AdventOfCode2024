import math

def issafe(report):
	sign = math.copysign(1, report[1] - report[0])

	for i in range(len(report) - 1):
		diff = report[i + 1] - report[i]
		if (diff == 0 or abs(diff) > 3 or math.copysign(1, diff) != sign):
			return 0
	
	return 1



reports=map(lambda l: list(map(int, l)), map(str.split, open(0)))

print(sum(map(issafe, reports)))