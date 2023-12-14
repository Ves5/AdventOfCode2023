import time

with open('day14/input.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]
    
    ## PART 1 ##
    
    t0 = time.time()
    # iterate over all lines other than the north border
    for i, line in enumerate(lines):
        # iterate lines up towards the north border (shifting boulders line by line)
        for j in range(i, 0, -1):
            # iterate over all boulders in the line
            for k in range(len(line)):
                if lines[j][k] == '.': continue
                # if round boulder, check if it can roll up
                if lines[j][k] == 'O' and lines[j-1][k] == '.':
                    lines[j][k], lines[j-1][k] = lines[j-1][k], lines[j][k]
    
    t1 = time.time()
    # # print the final state
    # for line in lines:
    #     print(''.join(line))
    
    # once all boulders are shifted, count their weight
    load_sum = 0
    
    for i, line in enumerate(lines):
        for char in line:
            if char == 'O': load_sum += len(lines) - i
    
    print(f'Part 1: {load_sum}')
    print(f'Part 1 time: {t1-t0:.3f}s')
    print(f'Part 2 estimated brute force time: {((t1-t0)*4*1000000000/3600):.3f}h')