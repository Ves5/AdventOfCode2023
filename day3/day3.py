import re

# class to store number coordinates and number of digits
class Number:
    def __init__(self, number, x, y) -> None:
        self.number = int(number)
        self.x = [x + i for i in range(len(number))]
        self.y = y
        self.length = len(number)
        
    def getValue(self) -> int:
        return self.number
    
    def __str__(self) -> str:
        return f'{self.number} at ({self.x}, {self.y})'

# class to store symbol coordinates
class Symbol:
    def __init__(self, symbol, x, y) -> None:
        self.symbol = symbol
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f'{self.symbol} at ({self.x}, {self.y})'

# find all symbols in a grid
def find_all_symbol_coords(grid) -> list[Symbol]:
    symbols = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if re.search(r'[^0-9.]', grid[i][j]):
                symbols.append(Symbol(grid[i][j], j, i))
    return symbols

def find_all_number_coords(grid) -> list[Number]:
    numbers = []
    for i in range(len(grid)):
        matches = re.finditer(r'[0-9]+', grid[i])
        for match in matches:
            numbers.append(Number(match.group(), match.start(), i))
    return numbers

def check_adjecency(symbol, number):
    if symbol.y == number.y or symbol.y == number.y + 1 or symbol.y == number.y - 1:
        for num_x in number.x:
            if symbol.x == num_x or symbol.x == num_x + 1 or symbol.x == num_x - 1:
                return True
    return False

def find_all_gear_candidates(grid) -> list[Symbol]:
    candidates = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                candidates.append(Symbol(grid[i][j], j, i))
    return candidates

with open('day3/input.txt') as f:
    grid = [line.strip() for line in f]
    
    ## PART 1 ##
    number_sum = 0
    
    # find all coordinates of symbols
    symbols = find_all_symbol_coords(grid)
    
    # find all coordinates of numbers
    numbers = find_all_number_coords(grid)
    
    # sum all number parts that are adjecent to symbols
    for symbol in symbols:
        for number in numbers:
            if check_adjecency(symbol, number):
                number_sum += number.getValue()

    print(f'Part 1: {number_sum}')
    
    ## PART 2 ##
    gear_sum = 0
    
    # find all coordinates of gear candidates
    candidates = find_all_gear_candidates(grid)
    
    # find all gears
    # gears are gear candidates that have exactly 2 number parts adjacent
    
    for candidate in candidates:
        adjecents = []
        for number in numbers:
            if check_adjecency(candidate, number):
                adjecents.append(number)
        if len(adjecents) == 2:
            gear_sum += adjecents[0].getValue() * adjecents[1].getValue()
    
    print(f'Part 2: {gear_sum}')