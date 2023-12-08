
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    return a // gcd(a, b) * b

with open('day8/input.txt') as f:
    lines = f.readlines()
    
    moves = lines[0].strip()
    node_routes = {}
    
    for line in lines[2:]:
        line = line.strip()
        node = line.split('=')[0].strip()
        routes = line.split('=')[1].strip().strip('()').split(', ')
        node_routes[node] = {"L": routes[0], "R": routes[1]}
        
    ## PART 1 ##
    node = 'AAA'
    no_visited = 0
    
    while (node != 'ZZZ'):
        # choose direction based on moves list (wrapping)
        move_index = no_visited % len(moves)
        node = node_routes[node][moves[move_index]]
        no_visited += 1
    
    print(f"Part 1: {no_visited}")
    
    ## PART 2 ##
    # find all starting nodes (node name ends with an A)
    # starting_nodes = []
    # for node in node_routes:
    #     if node[2] == 'A':
    #         starting_nodes.append(node)
    
    # no_moves = 0
    # current_nodes = starting_nodes
    # while True:
    #     # finish looping when all nodes end with Z at the same time
    #     finish_line = 0
    #     for node in current_nodes:
    #         if node[2] == 'Z':
    #             finish_line += 1
    #     if finish_line == len(current_nodes):
    #         break
        
    #     # route all nodes to next node, even if some are on their finish node
    #     next_nodes = []
    #     move_index = no_moves % len(moves)
    #     for node in current_nodes:
    #         next_nodes.append(node_routes[node][moves[move_index]])
    #     current_nodes = next_nodes
    #     no_moves += 1
        
    # print(f"Part 2: {no_moves}")
    
    ### TAKES TO LONG TO RUN ###
    
    ## Attempt 2 ##
    # find all starting nodes (node name ends with an A)
    starting_nodes = []
    for node in node_routes:
        if node[2] == 'A':
            starting_nodes.append(node)
            
    # find the minimal distance to finish node for each starting node
    distances = []
    for node in starting_nodes:
        current_node = node
        no_visited = 0
        while (current_node[2] != 'Z'):
            # choose direction based on moves list (wrapping)
            move_index = no_visited % len(moves)
            current_node = node_routes[current_node][moves[move_index]]
            no_visited += 1
        distances.append(no_visited)

    # find least common multiple of all distances
    lcm_value = 1
    for distance in distances:
        lcm_value = lcm(lcm_value, distance)
    
    print(f"Part 2: {lcm_value}")