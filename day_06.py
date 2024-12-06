from typing import Tuple, Union

with open('./input/day_06.txt') as f:
    G = {(x, y): v for y, row in enumerate(f.read().splitlines()) for x, v in enumerate(row.strip())}
start = min(coord for coord, v in G.items() if v == '^')

def traverse(obstacle: Tuple[int, int] = None) -> Union[None, int]:
    direction_map = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    g = {**G, obstacle: '#'} if obstacle else G
    pos, direction, visited = start, (0, -1), set()
    while pos in g:
        next_pos = tuple(map(sum, zip(pos, direction)))
        facing_wall = (g.get(next_pos) == '#')
        if facing_wall and (pos, direction) in visited:
            return None  # We faced this wall before so a loop is detected
        visited.add((pos, direction))
        if facing_wall:
            direction = direction_map[direction]
        else:
            pos = next_pos
    return len(set(v[0] for v in visited))

# Part 1: Traverse 1 time with original settings 
part1_answer = traverse(None)
print(f'Part 1: {part1_answer}')

# Part 2: Brute Force adding 1 obstacle at a time            
part2_answer = sum([1 for (x, y) in G if G[(x,y)] not in ('#', '^') and traverse(obstacle=(x, y)) is None])
print(f'Part 2: {part2_answer}')