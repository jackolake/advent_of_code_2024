from collections import defaultdict

with open('input/day_12.txt') as f:
    G = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}
ADJS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def run(part1=True):
    coord_to_cluster = dict()  # (x, y) => (cluster)
    cluster_to_plant = dict()  # cluster number => plant
    cluster_to_coords = defaultdict(set)
    cluster_id = 1
    # Gather connected components
    for (x, y), p in G.items():
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
                    if G.get((x_next, y_next)) == p and (x_next, y_next) not in tracked:
                        to_explore.append((x_next, y_next))
                        tracked.add((x_next, y_next))
            cluster_id += 1
    # Calculations
    areas = [len(coords) for coords in cluster_to_coords.values()]
    fences = [{(x, y): {(xa, ya) for (xa, ya) in ADJS if coord_to_cluster.get((x+xa, y+ya)) != cluster_id} for (x, y) in coords}
                 for cluster_id, coords in cluster_to_coords.items()]
    if part1:
        return sum(a * sum([len(fence_directions) for fence_directions in fence_map.values()]) for a, fence_map in zip(areas, fences))
    else:
        sides = []
        for fence_map in fences:
            side = 0
            # For each direction, only count the fence if my neighbour does not have a fence facing the same direction
            for adj in ADJS:
                same_direction_fences = [(x, y) for (x, y), adjs in fence_map.items() if adj in adjs]
                side += sum([1 for (x, y) in same_direction_fences if (x + adj[1], y + adj[0]) not in same_direction_fences])
            sides.append(side)
        return sum(a * s for a, s in zip(areas, sides))
        
# Part 1
part1_answer = run(part1=True)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = run(part1=False)
print(f'Part 2: {part2_answer}')