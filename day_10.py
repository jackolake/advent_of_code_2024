with open('./input/day_10.txt') as f:
    G = {(x, y): int(v) for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}

def explorable_positions(x, y):
    return [(x + x_adj, y + y_adj) for x_adj, y_adj in [(0, -1), (0, 1), (-1, 0), (1, 0)] if G.get((x + x_adj, y + y_adj)) == G[(x, y)] + 1]

def run(part1=True):
    trailheads = list()
    stack = []  # [(nodes_explored, nodes_to_explore, reached_9_yet)]
    # Init with height 0 locations
    for starting_points in [(x, y) for (x, y), v in G.items() if v == 0]:
        stack.append((set(), [starting_points], False))
    # Try all paths
    while stack:
        nodes_explored, nodes_to_explore, reached_9 = stack.pop()
        x, y = nodes_to_explore.pop()
        nodes_explored = nodes_explored | set([(x, y)])
        nodes_to_explore = list(set(nodes_to_explore) | set(explorable_positions(x, y)))
        if G[(x, y)] == 9:
            if not (part1 and nodes_to_explore):  # In part 1, trailheads with multiple 9 are possible
                trailheads.append(nodes_explored)
            if nodes_to_explore:
                stack.append((nodes_explored, nodes_to_explore, True))
        elif reached_9 and not nodes_to_explore:
            trailheads.append(nodes_explored)
        else:
            if part1:
                stack.append((nodes_explored, nodes_to_explore, reached_9))
            else:
                for x_try, y_try in nodes_to_explore:
                    stack.append((nodes_explored, [(x_try, y_try)], reached_9))
    return sum([1 for trailhead in trailheads for (x, y) in trailhead if G[(x, y)] == 9])

# Part 1
part1_answer = run(part1=True)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = run(part1=False)
print(f'Part 2: {part2_answer}')