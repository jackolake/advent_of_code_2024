import networkx as nx

with open('input/day_16.txt') as f:
    D = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}
S = [(x, y) for (x, y), v in D.items() if v == 'S'][0]
E = [(x, y) for (x, y), v in D.items() if v == 'E'][0]
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Parse into graph
G = nx.DiGraph()
for (x, y), v in D.items():
    if v != '#':
        for x_dir, y_dir in MOVES:
            if D[(x + x_dir, y + y_dir)] != '#':
                G.add_edge(((x, y), (x_dir, y_dir)), ((x + x_dir, y + y_dir), (x_dir, y_dir)), cost=1)
            G.add_edge(((x, y), (x_dir, y_dir)), ((x, y), (-y_dir, -x_dir)), cost=1000)     # Clockwise
            G.add_edge(((x, y), (x_dir, y_dir)), ((x, y), (y_dir, x_dir)), cost=1000)       # Anti-Clockwise

# Part 1
dest, part1_answer = None, 1e12
for face in MOVES:
    l = nx.shortest_path_length(G, source=(S, (1, 0)), target=(E, face), weight='cost')
    if l < part1_answer:
        part1_answer, dest = l, (E, face)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = len({n[0] for p in nx.all_shortest_paths(G, source=(S, (1, 0)), target=dest, weight='cost') for n in p})
print(f'Part 2: {part2_answer}')
