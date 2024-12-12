from collections import defaultdict

with open('input/day_12.txt') as f:
    G = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}
ADJS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Part 1
def run(g):
    coord_to_cluster = dict()  # (x, y) => (cluster)
    cluster_to_plant = dict()  # cluster number => plant
    cluster_to_coords = defaultdict(set)
    cluster_id = 1
    for (x, y), p in g.items():
        if (x, y) not in coord_to_cluster:
            to_explore = [(x, y)]
            tracked = set((x,y))
            cluster_to_plant[cluster_id] = p
            while to_explore:
                curr_x, curr_y = to_explore.pop()
                coord_to_cluster[(curr_x, curr_y)] = cluster_id
                cluster_to_coords[cluster_id].add((curr_x, curr_y))
                for x_adj, y_adj in ADJS:
                    x_next, y_next = curr_x + x_adj, curr_y + y_adj
                    if g.get((x_next, y_next)) == p and (x_next, y_next) not in tracked:
                        to_explore.append((x_next, y_next))
                        tracked.add((x_next, y_next))
            cluster_id += 1
    areas = [len(coords) for coords in cluster_to_coords.values()]
    perimeters = [sum(1 for (x, y) in coords for (xa, ya) in ADJS if coord_to_cluster.get((x+xa, y+ya)) != cluster_id) for cluster_id, coords in cluster_to_coords.items()]
    return sum(a * p for a, p in zip(areas, perimeters))
        

part1_answer = run(G.copy())
print(f'Part 1: {part1_answer}')