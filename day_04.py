import re
import numpy as np

with open('./input/day_04.txt') as f:
    m = np.array([list(l.strip()) for l in f.read().splitlines()])

def count_xmas(_: str) -> int:
    return len(re.findall('XMAS', _)) + len(re.findall('SAMX', _))

# Part 1: Horizontal + Vertical + Diagonal (top-left to bottom-right) + Diagonal (Top-right to bottom-left)
part1_answer = sum(count_xmas(''.join(row)) for row in m) + \
                sum(count_xmas(''.join(col)) for col in m.transpose()) + \
                sum(count_xmas(''.join(np.diagonal(m, offset=i))) for i in range(-max(m.shape) + 1, max(m.shape))) + \
                sum(count_xmas(''.join(np.diagonal(np.rot90(m), offset=i))) for i in range(-max(m.shape) + 1, max(m.shape)))
print(f'Part 1: {part1_answer}')

# Part 2
target = set(['M', 'S'])
part2_answer = sum([1 for row in range(1, m.shape[0] - 1) for col in range(1, m.shape[1] - 1)
                    if m[row][col] == 'A' and set([m[row-1][col-1], m[row+1][col+1]]) == target and set([m[row-1][col+1], m[row+1][col-1]]) == target])
print(f'Part 2: {part2_answer}')