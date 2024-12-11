from itertools import combinations

with open('input/day_08.txt') as f:
    G = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}
antennas = {a: [coord for coord, v in G.items() if v == a] for a in set(G.values()) if a.isalnum()}

def run(part2: bool) -> int:
    antinodes = set()
    start, end, step = (-100, 100, 1) if part2 else (-2, 2, 3)
    for coords in antennas.values():
        for (x1, y1), (x2, y2) in combinations(coords, r=2):
            x_delta, y_delta = x2 - x1, y2 - y1
            for i in range(start, end, step):
                x_try, y_try = (x2 + i * x_delta, y2 + i * y_delta)
                if (x_try, y_try) in G:
                    antinodes.add((x_try, y_try))
    return len(antinodes)

# Part 1
part1_answer = run(part2=False)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = run(part2=True)
print(f'Part 2: {part2_answer}')