import re
from typing import List

with open('./input/day_03.txt') as f:
    input_text = f.read().strip()

def calc(instructions: List[str]) -> int:
    value, enabled = 0, True
    for instruction in instructions:
        if instruction.startswith("don't"):
            enabled = False
        elif instruction.startswith("do"):
            enabled = True
        elif instruction.startswith('mul') and enabled:
            value += (lambda l: int(l[0]) * int(l[1]))(re.findall('\d+', instruction))
    return value


# Part 1
part1_answer = calc(re.findall('mul\(\d+,\d+\)', input_text))
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = calc(re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", input_text))
print(f'Part 2: {part2_answer}')