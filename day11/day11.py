class Galaxy:
    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

with open('day11/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    
    grid = [[y for y in x] for x in lines]
    
    # Find all Galaxies
    galaxies = []
    
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if char == '#':
                galaxies.append(Galaxy(i, j))
        
    # Find all columns and rows that are empty (only have '.')
    rows = []
    cols = []
    
    for j, line in enumerate(grid):
        if '#' not in line:
            rows.append(j)
    for i in range(len(grid[0])):
        if '#' not in [x[i] for x in grid]:
            cols.append(i)
    
    ## PART 1 ##
    
    # for every galaxy combination, calculate distance
    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            dist = abs(galaxies[i].x - galaxies[j].x) + abs(galaxies[i].y - galaxies[j].y)
            # if the empty row or column is between the two galaxies, add 1 to the distance for each instance
            for row in rows:
                if row > min(galaxies[i].y, galaxies[j].y) and row < max(galaxies[i].y, galaxies[j].y):
                    dist += 1
            for col in cols:
                if col > min(galaxies[i].x, galaxies[j].x) and col < max(galaxies[i].x, galaxies[j].x):
                    dist += 1
            distances.append(dist)
    
    print(f'Part 1: {sum(distances)}')
    
    ## PART 2 ##
    # empty row/column distance increases from 1 to 1000000
    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            dist = abs(galaxies[i].x - galaxies[j].x) + abs(galaxies[i].y - galaxies[j].y)
            # if the empty row or column is between the two galaxies, add 1 to the distance for each instance
            for row in rows:
                if row > min(galaxies[i].y, galaxies[j].y) and row < max(galaxies[i].y, galaxies[j].y):
                    dist += 999999
            for col in cols:
                if col > min(galaxies[i].x, galaxies[j].x) and col < max(galaxies[i].x, galaxies[j].x):
                    dist += 999999
            distances.append(dist)
            
    print(f'Part 2: {sum(distances)}')