with open('./input/day_06.txt') as f:
    grid = [list(l.strip()) for l in f.read().splitlines()]

# Parse
direction_map = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
guard_direction, stone_locs = (0, -1), set()
rows, cols = len(grid), len(grid[0])
for i, row in enumerate(grid):
    for j, value in enumerate(row):
        if value == '#':
            stone_locs.add((j, i))
        elif value == '^':
            guard_loc, guard_next_loc = (j, i), (j, i-1)

# Part 1
visited = set()
while 0 <= guard_next_loc[0] < cols and 0 <= guard_next_loc[1] < rows:
    visited.add(guard_loc)
    guard_next_loc = (guard_loc[0] +  guard_direction[0], guard_loc[1] + guard_direction[1])
    if guard_next_loc in stone_locs:
        guard_direction = direction_map[guard_direction]
        guard_next_loc = (guard_loc[0] +  guard_direction[0], guard_loc[1] + guard_direction[1])
    guard_loc = guard_next_loc
        
part1_answer = len(visited)
print(f'Part 1: {part1_answer}')