import re

def name2digit(name):
    if name == "zero":
        return "0"
    elif name == "one":
        return "1"
    elif name == "two":
        return "2"
    elif name == "three":
        return "3"
    elif name == "four":
        return "4"
    elif name == "five":
        return "5"
    elif name == "six":
        return "6"
    elif name == "seven":
        return "7"
    elif name == "eight":
        return "8"
    elif name == "nine":
        return "9"

# load input file
with open("day1/input.txt") as f:
    lines = f.readlines()
    
    ## PART 1 ##
    sum = 0
    # cycle through lines
    for line in lines:
        # find first digit in line
        d1 = ""
        d2 = ""
        for i in range(len(line)):
            if line[i].isdigit():
                d1 = line[i]
                break
        # find second digit in line
        for i in range(len(line), 0, -1):
            if line[i-1].isdigit():
                d2 = line[i-1]
                break
    
        # combine digits
        d = int(d1 + d2)
        # add to sum
        sum += d
    
    print("Part 1: " + str(sum))
    
    ## PART 2 ##
    sum = 0
    
    # cycle through lines
    for line in lines:
        # find all matches of digits or words that mean digits, overlapping characters allowed
        matches = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        # check if digit, else convert
        if matches[0].isdigit():
            d1 = matches[0]
        else:
            d1 = name2digit(matches[0])
        
        if matches[-1].isdigit():
            d2 = matches[-1]
        else:
            d2 = name2digit(matches[-1])
        
        d = int(d1 + d2)
        sum += d
        
    print("Part 2: " + str(sum))