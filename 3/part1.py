import re

print(sum(map(lambda l: int(l[0]) * int(l[1]), re.findall("mul\((\d{1,3}),(\d{1,3})\)", open(0).read()))))