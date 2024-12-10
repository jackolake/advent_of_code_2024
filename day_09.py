
init_disk = []
with open('./input/day_09.txt') as f:
    is_file = True
    file_id = 0
    for s in f.read().strip():
        if is_file:
            init_disk.extend(int(s) * [file_id])
            file_id += 1
        else:
            init_disk.extend(int(s) * [None])
        is_file = not is_file
    

def run(disk):
    head, tail = 0, len(disk) - 1
    while head != tail:
        if disk[head] is None:
            if disk[tail] is None:
                tail -= 1
            else:
                disk[head], disk[tail] = disk[tail], disk[head]
        else:
            head += 1
    return sum([i * file_id for i, file_id in enumerate(disk) if file_id is not None])

# Part 1
part1_answer = run(init_disk[:])
print(f'Part 1: {part1_answer}')
