from queue import Queue
with open('input/day_15.txt') as f:
    lines = [l.strip() for l in f.read().splitlines()]
seperator = lines.index('')
M = [v for row in lines[seperator+1:] for v in row]
D = {'v': (0, 1), '^': (0, -1), '<': (-1, 0), '>': (1, 0)}


def run(g, moves):
    rx, ry = [(x, y) for (x, y), v in g.items() if v == '@'][0]
    for move in moves:
        x_adj, y_adj = D[move]
        visited = set()
        q = Queue()
        q.put((rx, ry))
        while not q.empty():
            x, y = q.get()
            visited.add((x, y))
            if g[(x, y)] in ('[', ']'):
                x_next, y_next = (x + 1 if g[(x, y)] == '[' else x - 1), y
                if (x_next, y_next) not in visited and g[(x_next, y_next)] in ('O', '[', ']'):
                    q.put((x_next, y_next))
            x_next, y_next = x + x_adj, y + y_adj
            if g[(x_next, y_next)] in ('O', '[', ']'):
                if (x_next, y_next) not in visited and g[(x_next, y_next)] in ('O', '[', ']'):
                    q.put((x_next, y_next))
        # If anything in the cluster is facing an obstacle, ignore this move
        if any(g[(x + x_adj, y + y_adj)] == '#' for (x, y) in visited):
            continue
        # Otherwise, shift everything 1 step forward
        g = (g | {(x, y): '.' for (x, y) in visited} | {(x + x_adj, y + y_adj): g[(x, y)] for (x, y) in visited})
        rx, ry = rx + x_adj, ry + y_adj
    return sum([x + y * 100 for (x, y), v in g.items() if v in ('O', '[')])


# Part 1
g1 = {(x, y): v for y, row in enumerate(lines[:seperator])
      for x, v in enumerate(row)}
part1_answer = run(g1, M)
print(f'Part 1: {part1_answer}')

# Part 2
g2 = {(x, y): v for y, row in enumerate(lines[:seperator])
      for x, v in enumerate(row.replace('.', '..').replace('#', '##').replace('O', '[]').replace('@', '@.'))}
part2_answer = run(g2, M)
print(f'Part 2: {part2_answer}')