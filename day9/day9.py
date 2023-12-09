def next_number(series):
    # count list of differences
    diff = []
    for i in range(len(series)-1):
        diff.append(series[i+1] - series[i])
    # check for end condition (all 0)
    condition = set(diff)
    if len(condition) == 1 and 0 in condition:
        return diff[-1] + series[-1]
    else:
        return next_number(diff) + series[-1]
    
def previous_number(series):
    # count list of differences
    diff = []
    for i in range(len(series)-1):
        diff.append(series[i+1] - series[i])
    # check for end condition (all 0)
    condition = set(diff)
    if len(condition) == 1 and 0 in condition:
        return series[0] - diff[0]
    else:
        return series[0] - previous_number(diff)
        
with open("day9/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    series = [[int(x) for x in line.split(" ")] for line in lines]
    
    ## PART 1 ##
    next_sum = 0
    
    # find all next numbers for each series
    for serie in series:
        next_sum += next_number(serie)
    
    print(f"Part 1: {next_sum}")
    
    ## PART 2 ##
    prev_sum = 0
    
    # find all previous numbers for each series
    for serie in series:
        prev_sum += previous_number(serie)
        
    print(f"Part 2: {prev_sum}")
    