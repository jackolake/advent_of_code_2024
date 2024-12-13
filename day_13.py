import numpy as np
import re

machines = []
with open('input/day_13.txt') as f:
    for l in f.read().splitlines():
        if l:
            x, y = tuple(map(int, re.findall(r'\d+', l)))
            if l.startswith('Button A'):
                a = (x, y)
            elif l.startswith('Button B'):
                b = (x, y)
            elif l.startswith('Prize'):
                machines.append([a, b, (x, y)])

def run(part2=False):
    ans = 0
    for a, b, prize in machines:
        prize = tuple(map(lambda x: x + 10000000000000, prize)) if part2 else prize
        a_time, b_time = np.linalg.solve(list(zip(*(a, b))), prize)
        a_time, b_time = int(round(a_time)), int(round(b_time))
        if a_time * a[0] + b_time * b[0] == prize[0] and  a_time * a[1] + b_time * b[1] == prize[1]:
            ans += a_time * 3 + b_time
    return ans


# Part 1
part1_answer = run(part2=False)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = run(part2=True)
print(f'Part 2: {part2_answer}')