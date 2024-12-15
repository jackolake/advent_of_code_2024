with open('input/day_15.txt') as f:
    lines = [l.strip() for l in f.read().splitlines()]
seperator = lines.index('')
M = [v for row in lines[seperator+1:] for v in row]
D = {'v': (0, 1), '^': (0, -1), '<': (-1, 0), '>': (1, 0)}


def run(g, moves):
    rx, ry = [(x, y) for (x, y), v in g.items() if v == '@'][0]
    for move in moves:
        x_adj, y_adj = D[move]
        x, y = rx + x_adj, ry + y_adj
        while g[(x, y)] == 'O':  # Fast-forward outside of stone region
            x, y = x + x_adj, y + y_adj
        if g[(x, y)] == '.':
            g[(x, y)] = g[(x - x_adj, y - y_adj)]
            g[(rx, ry)] = '.'
            g[(rx + x_adj, ry + y_adj)] = '@'
            rx, ry = rx + x_adj, ry + y_adj
    return sum([x + y * 100 for (x, y), v in g.items() if v == 'O'])


# Part 1
g1 = {(x, y): v for y, row in enumerate(lines[:seperator])
      for x, v in enumerate(row)}
part1_answer = run(g1, M)
print(f'Part 1: {part1_answer}')
