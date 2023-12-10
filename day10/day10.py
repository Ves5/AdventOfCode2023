# | = NS; - = EW; L = NE; J = NW; 7 = SW; F = SE; . = nothing; S =start
pipes = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
opposite_dirs = {"N": "S", "S": "N", "E": "W", "W": "E"}

class Pipe:
    x = 0
    y = 0
    symbol = ''
    inside = ''
    outside = ''
    
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
        
    def set_inside_outside(self, pipe):
        if self.symbol == '|':
            self.inside = 'W' if pipe.inside.find("W") != -1 else 'E'
            self.outside = 'E' if pipe.inside.find("W") != -1 else 'W'
        elif self.symbol == '-':
            self.inside = 'N' if pipe.inside.find("N") != -1 else 'S'
            self.outside = 'S' if pipe.inside.find("N") != -1 else 'N'
        elif self.symbol == 'L':
            if (pipe.symbol == '|' or pipe.symbol == '7' or pipe.symbol == 'F'):
                self.inside = 'SW' if pipe.inside.find("W") != -1 else 'NE'
                self.outside = 'NE' if pipe.inside.find("W") != -1 else 'SW'
            else:
                self.inside = 'NE' if pipe.inside.find("N") != -1 else 'SW'
                self.outside = 'SW' if pipe.inside.find("N") != -1 else 'NE'
        elif self.symbol == 'J':
            if (pipe.symbol == '|' or pipe.symbol == '7' or pipe.symbol == 'F'):
                self.inside = 'NW' if pipe.inside.find("W") != -1 else 'SE'
                self.outside = 'SE' if pipe.inside.find("W") != -1 else 'NW'
            else:
                self.inside = 'SE' if pipe.inside.find("S") != -1 else 'NW'
                self.outside = 'NW' if pipe.inside.find("S") != -1 else 'SE'
        elif self.symbol == '7':
            if (pipe.symbol == '|' or pipe.symbol == 'L' or pipe.symbol == 'J'):
                self.inside = 'SW' if pipe.inside.find("W") != -1 else 'NE'
                self.outside = 'NE' if pipe.inside.find("W") != -1 else 'SW'
            else:
                self.inside = 'NE' if pipe.inside.find("N") != -1 else 'SW'
                self.outside = 'SW' if pipe.inside.find("N") != -1 else 'NE'
        elif self.symbol == 'F':
            if (pipe.symbol == '|' or pipe.symbol == 'L' or pipe.symbol == 'J'):
                self.inside = 'SE' if pipe.inside.find("E") != -1 else 'NW'
                self.outside = 'NW' if pipe.inside.find("E") != -1 else 'SE'
            else:
                self.inside = 'SE' if pipe.inside.find("S") != -1 else 'NW'
                self.outside = 'NW' if pipe.inside.find("S") != -1 else 'SE'


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
    if grid[start[1] - 1][start[0]] != '.' and pipes[grid[start[1] - 1][start[0]]].find(opposite_dirs['N']) != -1:
        direction = 'N'
        traversed_pipes.append((start[0], start[1] - 1))
    # South
    elif grid[start[1] + 1][start[0]] != '.' and pipes[grid[start[1] + 1][start[0]]].find(opposite_dirs['S']) != -1:
        direction = 'S'
        traversed_pipes.append((start[0], start[1] + 1))
    # East
    elif grid[start[1]][start[0] - 1] != '.' and pipes[grid[start[1]][start[0] - 1]].find(opposite_dirs['W']) != -1:
        direction = 'W'
        traversed_pipes.append((start[0] - 1, start[1]))
    # West
    elif grid[start[1]][start[0] + 1] != '.' and  pipes[grid[start[1]][start[0] + 1]].find(opposite_dirs['E']) != -1:
        direction = 'E'
        traversed_pipes.append((start[0] + 1, start[1]))
    
    dir1 = direction
    
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
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if (j, i) in traversed_pipes:
    #             print(grid[i][j], end='')
    #         else:
    #             print('.', end='')
    #     print()
        
    # idea 1: find a pipe that has definite "insie" and "outside" loop sides and propagate them to all other pipes
    # next for every non-loop coordinate, find closest loop or edge and determine if it's inside or outside the loop
    # a definite pipe like that could me a corner on the most extreme end of loop, in any direction
    
    if dir1 == 'N' or dir1 == 'S':
        direction = dir1 + opposite_dirs[direction]
    
    grid[start[1]][start[0]] = dict((v, k) for k, v in pipes.items())[direction]
    
    # find top-most then left-most corner of traversed_pipes
    start = traversed_pipes[0]
    for pipe in traversed_pipes:
        if pipe[1] < start[1]:
            start = pipe
        elif pipe[1] == start[1] and pipe[0] < start[0]:
            start = pipe
    
    # create proper starting point
    start = Pipe(start[0], start[1], grid[start[1]][start[0]])
    start.inside = 'SE'
    start.outside = 'NW'
    
    start_index = traversed_pipes.index((start.x, start.y))
    
    enhanced_pipes = [start]
    # traverse the loop again, mark the directions of each pipe as outside/inside
    for i in range(1, len(traversed_pipes)):
        index = (i + start_index) % len(traversed_pipes)
        
        # create new pipe class
        pipe = Pipe(traversed_pipes[index][0], traversed_pipes[index][1], grid[traversed_pipes[index][1]][traversed_pipes[index][0]])
        
        # based on previous pipe, determine inside and outside
        prev_pipe = enhanced_pipes[-1]
        pipe.set_inside_outside(prev_pipe)
        enhanced_pipes.append(pipe)
    
    inside_sum = 0
    
    # for every non-loop coordinate find any loop pipe or edge and determine if it's inside or outside
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in traversed_pipes:
                continue
            # iterate in every direction until loop pipe or edge is found
            # go up
            found = False
            for k in range(i, -1, -1):
                # if edge
                if k == 0 or k == len(grid):
                    found = True
                    break
                # if loop pipe
                if (j, k) in traversed_pipes:
                    # check if inside or outside
                    for pipe in enhanced_pipes:
                        if pipe.x == j and pipe.y == k:
                            if pipe.inside.find('S') != -1:
                                inside_sum += 1
                            found = True
                            break
                    break
            if found:
                continue
            # go down
            for k in range(i, len(grid) + 1):
                # if edge
                if k == 0 or k == len(grid):
                    found = True
                    break
                # if loop pipe
                if (j, k) in traversed_pipes:
                    # check if inside or outside
                    for pipe in enhanced_pipes:
                        if pipe.x == j and pipe.y == k:
                            if pipe.inside.find('N') != -1:
                                inside_sum += 1
                            found = True
                            break
                    break
            if found:
                continue
            # go left
            for k in range(j, -1, -1):
                # if edge
                if k == 0 or k == len(grid):
                    found = True
                    break
                # if loop pipe
                if (k, i) in traversed_pipes:
                    # check if inside or outside
                    for pipe in enhanced_pipes:
                        if pipe.x == k and pipe.y == i:
                            if pipe.inside.find('E') != -1:
                                inside_sum += 1
                            found = True
                            break
                    break
            if found:
                continue
            # go right
            for k in range(j, len(grid[i]) + 1):
                # if edge
                if k == 0 or k == len(grid):
                    found = True
                    break
                # if loop pipe
                if (k, i) in traversed_pipes:
                    # check if inside or outside
                    for pipe in enhanced_pipes:
                        if pipe.x == k and pipe.y == i:
                            if pipe.inside.find('W') != -1:
                                inside_sum += 1
                            found = True
                            break
                    break
                
    print(f'Part 2: {inside_sum}')
    
    ## I AM NOT PROUD OF PART 2 ##
            
    