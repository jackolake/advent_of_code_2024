from itertools import product
from operator import mul, add
import re

with open('./input/day_07.txt') as f:
    calibrations = [tuple(map(int, re.findall('\\d+', l.strip()))) for l in f.read().splitlines()]

# Part 1
part1_answer = 0
for (c, *test) in calibrations:
    for operators in product((mul, add), repeat=len(test)):
        v = test[0]
        for op, t in zip(operators, test[1:]):
            v = op(v, t)
        if v == c:
            part1_answer += c
            break
print(f'Part 1: {part1_answer}')
