def get_neighbors(garden, coords):
    x, y = coords
    neighbors = []
    # up
    if y > 0 and garden[y-1][x] != -1:
        neighbors.append((x, y-1))
    # down
    if y < len(garden)-1 and garden[y+1][x] != -1:
        neighbors.append((x, y+1))
    # left
    if x > 0 and garden[y][x-1] != -1:
        neighbors.append((x-1, y))
    # right
    if x < len(garden[y])-1 and garden[y][x+1] != -1:
        neighbors.append((x+1, y))
    return neighbors

def BFS(garden, start):
    explored = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        explored.add(node)
        
        # add neighbors to queue
        for neighbor in get_neighbors(garden, node):
            if neighbor not in explored and neighbor not in queue:
                queue.append(neighbor)
                garden[neighbor[1]][neighbor[0]] = min(garden[node[1]][node[0]] + 1, garden[neighbor[1]][neighbor[0]])

with open('day21/input.txt') as f:
    garden = [[s for s in x.strip()] for x in f.readlines()]
    
    # transform input into a 2D table of numbers
    # S = 0
    # # = -1 (unreachable)
    # . = 9999 (unknown yet)
    
    start_coords = None
    
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j] == '#':
                garden[i][j] = -1
            elif garden[i][j] == '.':
                garden[i][j] = 9999
            else:
                garden[i][j] = 0
                start_coords = (j, i)
                
    # BFS to find the shortest path to each reachable point
    BFS(garden, start_coords)
    
    ## PART 1 ##
    # find the number of tiles that are reachable under or equal 64, not -1 and divisible by 2
    tile_count = 0
    
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            if garden[i][j] != -1 and garden[i][j] <= 64 and garden[i][j] % 2 == 0:
                tile_count += 1
    
    print(f'Part 1: {tile_count}')
    
    ## PART 2 ##
    # scaryyyyyyyyyyyyyyyyyyyy
    
    
    
    