from functools import reduce
from itertools import product
from operator import mul, add
import re

with open('./input/day_07.txt') as f:
    calibrations = [tuple(map(int, re.findall('\\d+', l.strip()))) for l in f.read().splitlines()]

def run(valid_operators):
    answer = 0
    for (target, *numbers) in calibrations:
        for operators in product(valid_operators, repeat=len(numbers) - 1):
            op_iter = iter(operators)
            if target == reduce(lambda num1, num2: next(op_iter)(num1, num2), numbers):
                answer += target
                break
    return answer

# Part 1
part1_answer = run(valid_operators=[mul, add])
print(f'Part 1: {part1_answer}')

# Part 2
concat_op = lambda num1, num2: int(str(num1) + str(num2))
part2_answer = run(valid_operators=[mul, add, concat_op])
print(f'Part 2: {part2_answer}')