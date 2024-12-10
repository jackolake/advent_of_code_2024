import queue

with open('./input/day_10.txt') as f:
    G = {(x, y): int(v) for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row)}

# Part 1
trailheads = list()
q = queue.Queue()  # Try (coordinates explored, coordinates to explore, reached_9_yet)

def explorable_positions(x, y):
    return [(x + x_adj, y + y_adj) for x_adj, y_adj in [(0, -1), (0, 1), (-1, 0), (1, 0)] if G.get((x + x_adj, y + y_adj)) == G[(x, y)] + 1]

for starting_points in [(x, y) for (x, y), v in G.items() if v == 0]:
    q.put((set([starting_points]), explorable_positions(*starting_points), False))
while not q.empty():
    nodes_explored, nodes_to_explore, reached_9 = q.get()
    if nodes_to_explore:
        x, y = nodes_to_explore.pop()
        if G[(x, y)] == 9:
            reached_9 = True
            q.put((nodes_explored | set([(x, y)]), nodes_to_explore, True))
        else:
            q.put((nodes_explored | set([(x, y)]), list(set(explorable_positions(x, y)) | set(nodes_to_explore)), reached_9))
    elif reached_9:
        trailheads.append(nodes_explored)
part1_answer = sum([1 for trailhead in trailheads for (x, y) in trailhead if G[(x, y)] == 9])
print(f'Part 1: {part1_answer}')