# | = NS; - = EW; L = NE; J = NW; 7 = SW; F = SE; . = nothing; S =start
pipes = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
opposite_dirs = {"N": "S", "S": "N", "E": "W", "W": "E"}

with open('day10/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    
    grid = [[y for y in x] for x in lines]
    
    start = (-1, -1)
    # Find the starting point
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (j, i)
                break
        if start != (-1, -1):
            break
    
    # find starting direction
    traversed_pipes = []
    direction = ''
    # North
    if pipes[grid[start[1] - 1][start[0]]].find(opposite_dirs['N']) != -1:
        direction = 'N'
        traversed_pipes.append((start[0], start[1] - 1))
    # South
    elif pipes[grid[start[1] + 1][start[0]]].find(opposite_dirs['S']) != -1:
        direction = 'S'
        traversed_pipes.append((start[0], start[1] + 1))
    # East
    elif pipes[grid[start[1]][start[0] - 1]].find(opposite_dirs['W']) != -1:
        direction = 'W'
        traversed_pipes.append((start[0] - 1, start[1]))
    # West
    elif pipes[grid[start[1]][start[0] + 1]].find(opposite_dirs['E']) != -1:
        direction = 'E'
        traversed_pipes.append((start[0] + 1, start[1]))
    
    # Traverse the loop till you reach start again
    while traversed_pipes[-1] != start:
        pipe = grid[traversed_pipes[-1][1]][traversed_pipes[-1][0]]
        direction = pipes[pipe].strip(opposite_dirs[direction])
        
        if direction == "N":
            traversed_pipes.append((traversed_pipes[-1][0], traversed_pipes[-1][1] - 1))
        elif direction == "S":
            traversed_pipes.append((traversed_pipes[-1][0], traversed_pipes[-1][1] + 1))
        elif direction == "E":
            traversed_pipes.append((traversed_pipes[-1][0] + 1, traversed_pipes[-1][1]))
        elif direction == "W":
            traversed_pipes.append((traversed_pipes[-1][0] - 1, traversed_pipes[-1][1]))
        
    ## PART 1 ##
        
    print(f'Part 1: {(len(traversed_pipes) + 1) // 2}')
    
    ## PART 2 ##
    
    # loop visualisation
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in traversed_pipes:
                print(grid[i][j], end='')
            else:
                print('.', end='')
        print()