from functools import cache

patterns = []
with open('input/day_19.txt') as f:
    for l in f.read().splitlines():
        l = l.strip()
        if ',' in l:
            towels = [t.strip() for t in l.split(',')]
        elif l:
            patterns.append(l)

@cache
def is_possible(pattern) -> bool:
    return pattern in towels or any(is_possible(pattern[len(towel):]) for towel in towels if pattern.startswith(towel))
part1_answer = sum([1 for p in patterns if is_possible(p)])
print(f'Part 1: {part1_answer}')

@cache
def ways(pattern) -> int:
    return sum([ways(pattern[len(towel):]) for towel in towels if pattern.startswith(towel)]) if pattern else 1
part2_answer = sum([ways(p) for p in patterns])
print(f'Part 2: {part2_answer}')