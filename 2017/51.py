def instruction_jumps():
    instructions = []
    with open('day5.txt') as inputs:
        for line in inputs:
            instructions.append(line)

    # convert to ints
    instructions = list(map(int, instructions))

    i = 0
    outside_instructions = False
    steps = 0
    while not outside_instructions:
        jump_offset = int(instructions[i])
        instructions[i] += 1
        i += jump_offset
        steps += 1

        if i < 0 or i >= len(instructions):
            outside_instructions = True

    return steps

print(instruction_jumps())
