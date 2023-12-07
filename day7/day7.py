# CARD ORDER: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
# HAND ORDER: 5S, 4S, FH, 3S 2P, 1P, HC

card_value = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
hand_value = {"5S": 7, "4S": 6, "FH": 5, "3S": 4, "2P": 3, "1P": 2, "HC": 1}

card_value_part2 = {"A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}

def assign_hand_value(hand):
    cards = {}
    # count cards in hand
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    
    ## assign hand value
    # 5 of a kind = 5S
    if len(cards) == 1:
        return hand_value["5S"]
    # 4 of a kind = 4S
    if len(cards) == 2 and 4 in cards.values():
        return hand_value["4S"]
    # full house = FH
    if len(cards) == 2 and 3 in cards.values() and 2 in cards.values():
        return hand_value["FH"]
    # 3 of a kind = 3S
    if len(cards) == 3 and 3 in cards.values() and 2 not in cards.values():
        return hand_value["3S"]
    # 2 pairs = 2P
    if len(cards) == 3 and list(cards.values()).count(2) == 2:
        return hand_value["2P"]
    # 1 pair = 1P
    if len(cards) == 4 and 3 not in cards.values() and list(cards.values()).count(2) == 1:
        return hand_value["1P"]
    # high card = HC
    return hand_value["HC"]
    
def assign_hand_value_part2(hand):
    cards = {}
    # count cards in hand
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    
    # separate jokers from other cards
    jokers = 0
    if "J" in cards:
        jokers = cards["J"]
        cards["J"] = 0
    ## assign hand value
    # 5 of a kind = 5S
    if 5 in cards.values() or (jokers + max(cards.values())) == 5:
        return hand_value["5S"]
    # 4 of a kind = 4S
    if 4 in cards.values() or (jokers + max(cards.values())) == 4:
        return hand_value["4S"]
    # full house = FH
    if (3 in cards.values() and 2 in cards.values()) or (jokers == 1 and list(cards.values()).count(2) == 2):
        return hand_value["FH"]
    # 3 of a kind = 3S
    if 3 in cards.values() and 2 not in cards.values() or (jokers + max(cards.values())) == 3:
        return hand_value["3S"]
    # 2 pairs = 2P
    if list(cards.values()).count(2) == 2:
        return hand_value["2P"]
    # 1 pair = 1P
    if (3 not in cards.values() and list(cards.values()).count(2) == 1) or (jokers + max(cards.values())) == 2:
        return hand_value["1P"]
    # high card = HC
    return hand_value["HC"]    

def compare_hands(hand1, hand2):
    # compare hand values:
    if hand1[1] > hand2[1]:
        return 1
    elif hand1[1] < hand2[1]:
        return -1
    else:
        # equal hand values, compare cards
        for i in range(len(hand1[0])):
            if card_value[hand1[0][i]] > card_value[hand2[0][i]]:
                return 1
            elif card_value[hand1[0][i]] < card_value[hand2[0][i]]:
                return -1
    return 0

def compare_hands_part2(hand1, hand2):
    # compare hand values:
    if hand1[1] > hand2[1]:
        return 1
    elif hand1[1] < hand2[1]:
        return -1
    else:
        # equal hand values, compare cards
        for i in range(len(hand1[0])):
            if card_value_part2[hand1[0][i]] > card_value_part2[hand2[0][i]]:
                return 1
            elif card_value_part2[hand1[0][i]] < card_value_part2[hand2[0][i]]:
                return -1
    return 0

with open('day7/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    
    cards_bid_pairs = [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]
    
    ## PART 1 ##
    hand_value_bid = []
    for cards, bid in cards_bid_pairs:
        hand_value_bid.append((cards, assign_hand_value(cards), bid))
    
    # bubble sort for the rescue
    for i in range(len(hand_value_bid)):
        for j in range(i+1, len(hand_value_bid)):
            # if first hand is lower value than hand 2, swap
            if compare_hands(hand_value_bid[i], hand_value_bid[j]) < 0:
                hand_value_bid[i], hand_value_bid[j] = hand_value_bid[j], hand_value_bid[i]
    
    # count bids multipliers
    bid_sum = 0

    for i in range(len(hand_value_bid)):
        bid_sum += hand_value_bid[-(i+1)][2] * (i+1)
        
    print(f'Part 1: {bid_sum}')
    
    ## PART 2 ##
    hand_value_bid = []
    for cards, bid in cards_bid_pairs:
        hand_value_bid.append((cards, assign_hand_value_part2(cards), bid))
    
    # bubble sort for the rescue
    for i in range(len(hand_value_bid)):
        for j in range(i+1, len(hand_value_bid)):
            # if first hand is lower value than hand 2, swap
            if compare_hands_part2(hand_value_bid[i], hand_value_bid[j]) < 0:
                hand_value_bid[i], hand_value_bid[j] = hand_value_bid[j], hand_value_bid[i]
    
    # count bids multipliers
    bid_sum = 0

    for i in range(len(hand_value_bid)):
        bid_sum += hand_value_bid[-(i+1)][2] * (i+1)
        
    print(f'Part 2: {bid_sum}')