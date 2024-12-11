from functools import cache

with open('input/day_11.txt') as f:
    stones = [int(n) for n in f.read().strip().split()]

@cache
def run(stone: int, blinks_remaining: int) -> int:
    if blinks_remaining == 0:
        return 1
    if stone == 0:
        return run(1, blinks_remaining - 1)
    stone_str = str(stone)
    stone_len = len(stone_str)
    if stone_len % 2 == 0:
        middle_idx = stone_len // 2
        return run(int(stone_str[:middle_idx]), blinks_remaining - 1) + \
                run(int(stone_str[middle_idx:]), blinks_remaining - 1)
    return run(stone * 2024, blinks_remaining - 1)

# Part 1
part1_answer = sum(run(s, blinks_remaining=25) for s in stones)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = sum(run(s, blinks_remaining=75) for s in stones)
print(f'Part 2: {part2_answer}')