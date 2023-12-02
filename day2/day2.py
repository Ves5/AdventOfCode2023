cube_max = {"r": 12, "g": 13, "b": 14}

with open('day2/input.txt') as f:
    # strip whitespace and newlines
    games = [l.strip() for l in f.readlines()]
    
    ## PART 1 ##
    id_sum = 0
    
    # part 2 sum
    power_sum = 0
    
    # for every game
    for game in games:
        # extract game id
        game_id = int(game.split(":")[0].split(" ")[1])
        # extract game rolls
        game_rolls = game.split(":")[1].split(";")
        # cumulative max cubes for game
        game_max = {"r": 0, "g": 0, "b": 0}
        # for every roll
        for roll in game_rolls:
            # extract all outcomes
            outcomes = roll.split(",")
            # extract outcome and cube colour
            for outcome in outcomes:
                cube_number = int(outcome.strip().split(" ")[0])
                # only first letter of colour
                cube_colour = outcome.strip().split(" ")[1][0]
                # check max
                game_max[cube_colour] = max(game_max[cube_colour], cube_number)
        
        # check if it's within constraints
        if game_max["r"] <= cube_max["r"] and game_max["g"] <= cube_max["g"] and game_max["b"] <= cube_max["b"]:
            id_sum += game_id
            
        ## PART 2 ##
        power_sum += game_max["r"] * game_max["g"] * game_max["b"]
        
    print("Part 1: " + str(id_sum))
    
    print("Part 2: " + str(power_sum))
    