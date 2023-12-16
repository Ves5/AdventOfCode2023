# import sys
# sys.setrecursionlimit(1500)
import time

class Light:
    direction = 'R'
    position = ((0, 0), 'R')
    visited = set()
    
    def __init__(self, position = (0, 0), direction = 'R', visited = set()) -> None:
        self.position = (position, direction)
        self.direction = direction
        self.visited = visited
        
    def traverse(self, grid: list[list[str]]) -> set[tuple[int, int]]:
        while True:
            if self.direction == 'R':
                self.position = ((self.position[0][0] + 1, self.position[0][1]), 'R')
            elif self.direction == 'L':
                self.position = ((self.position[0][0] - 1, self.position[0][1]), 'L')
            elif self.direction == 'U':
                self.position = ((self.position[0][0], self.position[0][1] - 1), 'U')
            elif self.direction == 'D':
                self.position = ((self.position[0][0], self.position[0][1] + 1), 'D')
                
            if self.position[0][0] < 0 or self.position[0][1] < 0:
                break
            if self.position[0][0] >= len(grid) or self.position[0][1] >= len(grid[0]):
                break
            # if we're crossing the same space twice in different directions it will terminate early, to be weary
            if self.position in self.visited:
                break
            
            self.visited.add(self.position)
            
            if grid[self.position[0][1]][self.position[0][0]] == '|':
                if self.direction == 'U' or self.direction == 'D':
                    # if on pointy end of splitter, continue traversing in the same direction
                    continue
                else:
                    # if on flat end side of splitter, split into two direction 
                    # spawn 2 new lights, one going up and one going down
                    self.visited = self.visited.union(Light(self.position[0], 'U', self.visited).traverse(grid))
                    self.visited = self.visited.union(Light(self.position[0], 'D', self.visited).traverse(grid))
                    break
            elif grid[self.position[0][1]][self.position[0][0]] == '-':
                if self.direction == 'R' or self.direction == 'L':
                    # if on pointy end of splitter, continue traversing in the same direction
                    continue
                else:
                    # if on flat end side of splitter, split into two direction 
                    # spawn 2 new lights, one going left and one going right
                    self.visited = self.visited.union(Light(self.position[0], 'L', self.visited).traverse(grid))
                    self.visited = self.visited.union(Light(self.position[0], 'R', self.visited).traverse(grid))
                    break
                
            elif grid[self.position[0][1]][self.position[0][0]] == '/':
                if self.direction == 'U':
                    self.direction = 'R'
                elif self.direction == 'R':
                    self.direction = 'U'
                elif self.direction == 'D':
                    self.direction = 'L'
                elif self.direction == 'L':
                    self.direction = 'D'
            elif grid[self.position[0][1]][self.position[0][0]] == '\\':
                if self.direction == 'U':
                    self.direction = 'L'
                elif self.direction == 'L': 
                    self.direction = 'U'
                elif self.direction == 'D':
                    self.direction = 'R'
                elif self.direction == 'R':
                    self.direction = 'D'
            
        
        return self.visited

with open('day16/input.txt') as f:
    grid = [[x for x in line.strip()] for line in f.readlines()]
    
    ## PART 1 ##
    
    light = Light((-1, 0))
    
    t1 = time.time()
    visited = set(point[0] for point in light.traverse(grid))
    t2 = time.time()
    
    print(f'Part 1: {len(visited)}')
    print(f'Part 1 time: {t2 - t1}s')
    print(f'Part 2 estimated time: {(len(grid) * 2 + len(grid[0]) * 2) * (t2 - t1)}s')
    
    ## PART 2 Brute Force ##
    energized_tiles = []
    
    t3 = time.time()
    for i in range(len(grid)):
        energized_tiles.append(len(set(point[0] for point in Light((-1, i), 'R', set()).traverse(grid))))
        energized_tiles.append(len(set(point[0] for point in Light((len(grid), i), 'L', set()).traverse(grid))))
    for j in range(len(grid[0])):
        energized_tiles.append(len(set(point[0] for point in Light((j, -1), 'D', set()).traverse(grid))))
        energized_tiles.append(len(set(point[0] for point in Light((j, len(grid[0])), 'U', set()).traverse(grid))))
    t4 = time.time()
    
    print(f'Part 2: {max(energized_tiles)}')
    print(f'Part 2 time: {t4 - t3}s')
            
    