import re

with open('input/day_17.txt') as f:
    for l in f.read().splitlines():
        l = l.strip()
        if l:
            numbers = list(map(int, re.findall(r'\d+', l)))
            if 'A' in l:
                A = numbers[0]
            elif 'B' in l:
                B = numbers[0]
            elif 'C' in l:
                C = numbers[0]
            else:
                OPS = numbers

def run(a, b, c, operations, part2=False):
    inst_pointer = 0
    length = len(operations)
    outputs = []
    while inst_pointer < length:
        op_code, literal = operations[inst_pointer], operations[inst_pointer + 1]
        combo = {4: a, 5: b, 6: c}.get(literal, literal)
        if op_code == 0:
            a = a // (2 ** combo)
        elif op_code == 1:
            b = b ^ literal
        elif op_code == 2:
            b = combo % 8
        elif op_code == 3:
            if a != 0:
                inst_pointer = literal
                continue
        elif op_code == 4:
            b = b ^ c
        elif op_code == 5:
            outputs.append(combo % 8)
            if part2 and outputs[-1] != OPS[len(outputs)-1]:
                return outputs
        elif op_code == 6:
            b = a // (2 ** combo)
        elif op_code == 7:
            c = a // (2 ** combo)
        inst_pointer += 2
    return outputs
# Part 1
part1_answer = run(A, B, C, OPS)
print(f'Part 1: {part1_answer}')

# Part 2
part2_answer = 0
while OPS != run(part2_answer, B, C, OPS, part2=True):
    part2_answer += 1
print(f'Part 2: {part2_answer}')

