import networkx as nx

with open('input/day_18.txt') as f:
    ROCKS = [tuple(map(int, l.split(','))) for l in f.read().splitlines()]
S, E = (0, 0), (70, 70)

# Graph with no rocks
G = nx.DiGraph()
for y in range(E[1] + 1):
    for x in range(E[0] + 1):
        for (x_adj, y_adj) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x_next, y_next = x + x_adj, y + y_adj
            if 0 <= x_next <= E[0] and 0 <= y_next <= E[1]:
                G.add_edge((x, y), (x_next, y_next))
                G.add_edge((x_next, y_next), (x, y))

def run(part1=True):
    g = G.copy()
    for i, rock in enumerate(ROCKS):
        for edge in list(g.in_edges(rock)) + list(g.out_edges(rock)):
            g.remove_edge(*edge)
        if part1 and i == 1024 - 1:
            return nx.shortest_path_length(g, S, E)
        else:
            if not nx.has_path(g, S, E):
                return rock

# Part 1
part1_answer = run(part1=True)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = run(part1=False)
print(f'Part 2: {part2_answer}')