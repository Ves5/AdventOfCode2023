import re

def calculate_distance(time, btn_time):
    return (time - btn_time) * btn_time

with open("day6/input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]
    times = [int(x) for x in re.findall(r"\d+", lines[0])]
    distances =  [int(x) for x in re.findall(r"\d+", lines[1])]
    
    time_dist_pairs = list(zip(times, distances))
    
    ## PART 1 ##
    win_possibilities = 1
        
    for pair in time_dist_pairs:
        wins = 0
        for i in range(1, pair[0]):
            if calculate_distance(pair[0], i) > pair[1]:
                wins += 1
        win_possibilities *= wins
    
    print("Part 1:" + str(win_possibilities))
    
    ## PART 2 ##
    time = int("".join(re.findall(r"\d+", lines[0])))
    distance =  int("".join(re.findall(r"\d+", lines[1])))
    
    win_possibilities = 0
    for i in range(1, time):
        if calculate_distance(time, i) > distance:
            win_possibilities += 1
    
    print("Part 2:" + str(win_possibilities))