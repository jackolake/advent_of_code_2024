with open('./input/day_01.txt') as f:
    number_list_left, number_list_right = zip(*(map(int, l.strip().split()) for l in f.read().splitlines()))

# Part 1
part1_answer = sum(abs(l-r) for l, r in zip(sorted(number_list_left), sorted(number_list_right)))
print(f'Part 1: {part1_answer}')  # 1830467

# Part 2
counter = {n: number_list_right.count(n) for n in number_list_right}
part2_answer = sum(n * counter.get(n, 0) for n in number_list_left)
print(f'Part 2: {part2_answer}')  # 26674158