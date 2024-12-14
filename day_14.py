import re
from functools import reduce

with open('input/day_14.txt') as f:
    patrols = [tuple(map(int, re.findall(r'\-?\d+', l))) for l in f.read().splitlines()]
X_LIMIT, Y_LIMIT = 101, 103

def run(seconds=100):
    new_pos = [((px + vx * seconds) % X_LIMIT, (py + vy * seconds) % Y_LIMIT) for px, py, vx, vy in patrols]
    uniq_pos = set(new_pos)
    return sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x < X_LIMIT//2 and y < Y_LIMIT//2])\
            * sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x < X_LIMIT//2 and y > Y_LIMIT//2])\
            * sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x > X_LIMIT//2 and y < Y_LIMIT//2])\
            * sum([new_pos.count((x, y)) for (x, y) in uniq_pos if x > X_LIMIT//2 and y > Y_LIMIT//2])


# Part 1
part1_answer = run(100)
print(f'Part 1: {part1_answer}')
