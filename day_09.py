from collections import defaultdict
init_free_spaces = list()                # [(start, size)]
init_files = defaultdict(list)           # (file_id, [(start, size)])


with open('./input/day_09.txt') as f:
    is_file = True
    file_id = 0
    current_position = 0
    for s in f.read().strip():
        if is_file:
            init_files[file_id].append((current_position, int(s)))
            file_id += 1
        else:
            if int(s) > 0:
                init_free_spaces.append((current_position, int(s)))
        current_position += int(s)
        is_file = not is_file
    

def run(files, free_spaces):
    for file_id in list(files.keys())[::-1]:
        for file_idx, (file_start, file_size) in enumerate(files[file_id]):
            shifted = False
            for i, (free_space_position, free_space_size) in enumerate(free_spaces):
                if free_space_position < file_start:   # Move file only if enough free space is on the left
                    if free_space_size == file_size:   # Free space filled completely by the file
                        free_spaces.pop(i)
                        shifted = True
                    elif free_space_size > file_size:  # Free space partially filled by the file
                        free_spaces[i] = (free_space_position + file_size, free_space_size - file_size)
                        shifted = True
                    if shifted:
                        break
            if shifted:
                files[file_id][file_idx] = (free_space_position, file_size)
    return sum([sum(file_id * pos for pos in range(start, start + size)) for file_id, positions in files.items() for start, size in positions])

# Part 1 - Split files into mini files before moving
part1_files = {file_id: [(pos, 1) for pos in range(start + size - 1, start - 1, -1)] for file_id, positions in init_files.items() for start, size in positions}
part1_answer = run(part1_files, init_free_spaces.copy())
print(f'Part 1: {part1_answer}')

# Part 2 - Move complete files
part2_answer = run(init_files.copy(), init_free_spaces.copy())
print(f'Part 2: {part2_answer}')
