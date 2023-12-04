with open('day4/input.txt') as file:
    cards = [line.strip() for line in file.readlines()]
    
    ## PART 1 ##
    points_sum = 0
    
    ## PART 2 ##
    card_count = {}
    for i in range(len(cards)):
        card_count[i+1] = 1
    
    for card in cards:
        card_id = int(card.split(':')[0].split(' ')[-1].strip())
        
        card_content = card.split(':')[1].strip()
        
        # get all winning numbers as strings
        winning_set = set(card_content.split('|')[0].strip().split(' '))
        if '' in winning_set:
            winning_set.remove('')
        # convert them to numbers
        winning_set = set([int(x) for x in winning_set])
        
        # get all guessed numbers as strings
        guessed_set = set(card_content.split('|')[1].strip().split(' '))
        if '' in guessed_set:
            guessed_set.remove('')
        # convert them to numbers
        guessed_set = set([int(x) for x in guessed_set])
        
        # get the intersection of the two sets
        intersection = winning_set.intersection(guessed_set)
        
        if len(intersection) > 0:
            points_sum += pow(2, len(intersection) - 1)
            
        ## PART 2 ##
        for i in range(len(intersection)):
            card_count[card_id + i + 1] += card_count[card_id]
        
    print(f'Part 1: {str(points_sum)}')
    
    ## PART 2 ##
    card_sum = 0
    for card in card_count:
        card_sum += card_count[card]
    
    print(f'Part 2: {str(card_sum)}')