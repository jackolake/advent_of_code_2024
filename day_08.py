from itertools import combinations

with open('input/day_08.txt') as f:
    G = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}
antennas = {a: [coord for coord, v in G.items() if v == a] for a in set(G.values()) if a.isalnum()}
antinodes = set()

for antenna, coords in antennas.items():
    for (x1, y1), (x2, y2) in combinations(coords, r=2):
        x_delta, y_delta = x2 - x1, y2 - y1
        for (x_try, y_try) in [(x1 - x_delta, y1 - y_delta), (x2 + x_delta, y2 + y_delta)]:
            if (x_try, y_try) in G:
                antinodes.add((x_try, y_try))
# Part 1
part1_answer = len(antinodes)
print(f'Part 1: {part1_answer}')
