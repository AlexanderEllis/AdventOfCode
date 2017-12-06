
def memory_realloc():
    banks = []
    with open('day6.txt') as file:
        for line in file:
            banks = line.split()

    banks = list(map(int, banks))

    blocks_seen_before = {}

    # realloc max
    # join and add to blocks seen
    counting = False
    really_done = False

    redistributions = 0

    while not really_done:
        index = banks.index(max(banks))
        blocks_to_allocate = banks[index]
        banks[index] = 0
        while blocks_to_allocate is not 0:
            index += 1
            banks[index % len(banks)] += 1
            blocks_to_allocate -= 1

        # check if done already
        banks_as_string = ' '.join(str(x) for x in banks)

        if counting:
            redistributions += 1

        if banks_as_string in blocks_seen_before and counting:
            really_done = True
        elif banks_as_string in blocks_seen_before:
            counting = True
            blocks_seen_before = {}
            blocks_seen_before[banks_as_string] = True
        else:
            blocks_seen_before[banks_as_string] = True
    
    return redistributions

print(memory_realloc())