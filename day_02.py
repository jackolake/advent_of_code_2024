from typing import List

with open('./input/day_02.txt') as f:
    reports = [list(map(int, l.strip().split())) for l in f.read().splitlines()]

def correct(seq: List[int]) -> bool:
    diffs = [n1-n2 for n1, n2 in zip(seq[:-1], seq[1:])]
    # Differences = same sign & between 1 to 3
    return len(set([d/abs(d) for d in diffs if d])) == 1 and all([1 <= abs(d) <= 3 for d in diffs])

# Part 1: Check if report is correct
part1_answer = sum([1 for r in reports if correct(r)])
print(f'Part 1: {part1_answer}')

# Part 2: Check if report is correct, or removing 1 mistake becomes correct
part2_answer = sum([1 for r in reports if correct(r) or any(correct(r[:i] + r[i+1:]) for i in range(len(r)))])
print(f'Part 2: {part2_answer}')