with open('day18/input.txt') as f:
    lines = [line.strip().split() for line in f.readlines()]
    
    points = [(0,0)]
    for line in lines:
        if line[0] == "R":
            points.append((points[-1][0] + int(line[1]), points[-1][1]))
        elif line[0] == "U":
            points.append((points[-1][0], points[-1][1] - int(line[1])))
        elif line[0] == "L":
            points.append((points[-1][0] - int(line[1]), points[-1][1]))
        elif line[0] == "D":
            points.append((points[-1][0], points[-1][1] + int(line[1])))
            
    # visualize the points and the path with # as path and points and . as empty space
    # min_x = min([point[0] for point in points])
    # max_x = max([point[0] for point in points])
    # min_y = min([point[1] for point in points])
    # max_y = max([point[1] for point in points])
    # grid = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]
    
    # for point in points:
    #     grid[point[1]-min_y][point[0]-min_x] = '#'
    
    # # mark path with #
    # for i, point in enumerate(points):
    #     if i == 0:
    #         continue
    #     elif point[0] == points[i-1][0]:
    #         if point[1] < points[i-1][1]:
    #             for j in range(point[1], points[i-1][1]+1):
    #                 grid[j-min_y][point[0]-min_x] = '#'
    #         else:
    #             for j in range(points[i-1][1], point[1]+1):
    #                 grid[j-min_y][point[0]-min_x] = '#'
    #     elif point[1] == points[i-1][1]:
    #         if point[0] < points[i-1][0]:
    #             for j in range(point[0], points[i-1][0]+1):
    #                 grid[point[1]-min_y][j-min_x] = '#'
    #         else:
    #             for j in range(points[i-1][0], point[0]+1):
    #                 grid[point[1]-min_y][j-min_x] = '#'

    # print('\n'.join([''.join(row) for row in grid]))
    # print(('\n'.join([''.join(row) for row in grid])).count("#"))
    
            
    ## PART 1 ##
    shoelace_sum = 0
    distance_sum = 0
    
    for i, point in enumerate(points):
        shoelace_sum += point[0] * points[(i+1)%len(points)][1] - point[1] * points[(i+1)%len(points)][0]
        distance_sum += abs(point[0] - points[(i+1)%len(points)][0]) + abs(point[1] - points[(i+1)%len(points)][1])
        
    area = abs(shoelace_sum)//2
    pick_inner = area - (distance_sum//2) + 1 # should be 24 for tinput
        
    # print(f'Distance sum: {distance_sum}')
    # print(f'Inner area: {pick_inner}')
    print(f'Part 1: {pick_inner + distance_sum}')
    
    ## PART 2 ##
    # extract distance and direction from hexadecimal numbers provided
    # then repeat the same as part 1
    
    for line in lines:
        code = line[-1].strip('(#)')
        if code[-1] == '0':
            line[0] = 'R'
        elif code[-1] == '1':
            line[0] = 'D'
        elif code[-1] == '2':
            line[0] = 'L'
        elif code[-1] == '3':
            line[0] = 'U'
        # convert hex to decimal
        line[1] = int(code[:-1], 16)
        
    points = [(0,0)]
    for line in lines:
        if line[0] == "R":
            points.append((points[-1][0] + int(line[1]), points[-1][1]))
        elif line[0] == "U":
            points.append((points[-1][0], points[-1][1] - int(line[1])))
        elif line[0] == "L":
            points.append((points[-1][0] - int(line[1]), points[-1][1]))
        elif line[0] == "D":
            points.append((points[-1][0], points[-1][1] + int(line[1])))
    
    shoelace_sum = 0
    distance_sum = 0
    
    for i, point in enumerate(points):
        shoelace_sum += point[0] * points[(i+1)%len(points)][1] - point[1] * points[(i+1)%len(points)][0]
        distance_sum += abs(point[0] - points[(i+1)%len(points)][0]) + abs(point[1] - points[(i+1)%len(points)][1])
        
    area = abs(shoelace_sum)//2
    pick_inner = area - (distance_sum//2) + 1 # should be 24 for tinput
        
    # print(f'Distance sum: {distance_sum}')
    # print(f'Inner area: {pick_inner}')
    print(f'Part 2: {pick_inner + distance_sum}')