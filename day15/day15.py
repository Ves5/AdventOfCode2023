def lens_label(lens):
    current_value = 0
    for l in lens:
        current_value = (current_value + ord(l)) * 17 % 256
    return current_value

with open('day15/input.txt') as f:
    steps = f.readline().split(',')
    
    ## PART 1 ##
    value_sum = 0
    
    for step in steps:
        current_value = 0
        for symbol in step:
            current_value = (current_value + ord(symbol)) * 17 % 256
        value_sum += current_value
    
    print(f'Part 1: {value_sum}')
    
    ## PART 2 ##
    
    # convert to tuples of hash + operation
    steps_tuples = []
    for step in steps:
        if step.find('=') != -1:
            steps_tuples.append((step.split('=')[0], int(step.split('=')[1])))
        else:
            steps_tuples.append((step.split('-')[0], '-'))
            
    boxes = [[] for i in range(256)]
    
    for step in steps_tuples:
        hash_value = lens_label(step[0])
        if step[1] == '-':
            # remove from box if exists
            for lens in boxes[hash_value]:
                if lens[0] == step[0]:
                    boxes[hash_value].remove(lens)
                    break
        else:
            # add to box if not exists
            exists = False
            for i, lens in enumerate(boxes[hash_value]):
                if lens[0] == step[0]:
                    exists = True
                    # swap if exists
                    boxes[hash_value][i] = (step[0], step[1])
                    break
            if not exists:
                boxes[hash_value].append((step[0], step[1]))
                
    # calculate focusing power
    focus_power = 0
    
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focus_power += (i+1) * (j + 1) * lens[1]
            
    print(f'Part 2: {focus_power}')
        