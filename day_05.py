from functools import cmp_to_key


with open('./input/day_05.txt') as f:
    lines = [l.strip() for l in f.read().splitlines()]
rules = [tuple(map(int, l.split('|'))) for l in lines if '|' in l]
updates = [list(map(int, l.split(','))) for l in lines if ',' in l]

# Utilities
kf = cmp_to_key(lambda n1, n2: -1 if (n1, n2) in rules else 1)
corrected_updates = [sorted(u, key=kf) for u in updates]

# Part 1
part1_answer = sum([u[len(u)//2] for u, c in zip(updates, corrected_updates) if u == c])
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = sum([c[len(c)//2] for u, c in zip(updates, corrected_updates) if u != c])
print(f'Part 2: {part2_answer}')