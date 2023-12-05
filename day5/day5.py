class MapRange:
    def __init__(self, source, destination, length):
        self.source = source
        self.destination = destination
        self.length = length
    
    # check if a number belongs to this map range
    def check_belonging(self, number):
        return self.source <= number < self.source + self.length
    
    # convert number to the mapped number
    def convert(self, number):
        if self.check_belonging(number):
            return self.destination + (number - self.source)
        
class Mapper:
    map_phases = []
    
    def __init__(self):
        pass
    
    # convert number through all mapping phases
    def convert(self, number):
        tmp = number
        for phase in self.map_phases:
            for map_range in phase:
                if map_range.check_belonging(tmp):
                    tmp = map_range.convert(tmp)
                    break
        return tmp
    
    def convert_number_range(self, number, length):
        converted = []
        for i in range(number, number + length):
            tmp = i
            for phase in self.map_phases:
                for map_range in phase:
                    if map_range.check_belonging(tmp):
                        tmp = map_range.convert(tmp)
                        break
        return min(converted)
    
    # load a mapping phase from text
    def load_map_phase(self, maps):
        phase = []
        for map_text in maps:
            phase.append(self.load_map_range(map_text))
        self.map_phases.append(phase)
    
    # load a mapping range from text
    def load_map_range(self, map_text):
        destination, source, length = map_text.split(" ")
        return MapRange(int(source), int(destination), int(length))
    
with open("day5/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    
    seeds = [int(x.strip()) for x in lines[0].split(":")[1].strip().split(" ")]
    
    # load map phases and ranges
    mapper = Mapper()
    maps = []
    
    for line in lines[2:]:
        if line.find("map") != -1:
            maps = []
            continue
        if line == "":
            mapper.load_map_phase(maps)
            continue
        maps.append(line)
    mapper.load_map_phase(maps)
    
    ## PART 1 ##
    locations = []
    
    # convert seeds  
    for seed in seeds:
        locations.append(mapper.convert(seed))
        
    print("Part 1: " + str(min(locations)))
    
    ## PART 2 ##
    ## THE SCUFFED WAY ##
    
    # convert seeds to seed ranges
    # seed_ranges = []
    # for i in range(0, len(seeds), 2):
    #     seed_ranges.append([seeds[i], seeds[i+1]])
    
    # convert seed ranges
    # locations = []
    # for seed_range in seed_ranges:
    #     locations.append(mapper.convert_number_range(seed_range[0], seed_range[1]))
        
    # print("Part 2: " + str(min(locations)))
    
    ### WAY TOO SCUFFED ###
    # but it would be a good parallel execution task!
    
    ## PART 2.5 ##
    ## THE LESS SCUFFED WAY? ##
    
    ## Ideas:
    # 1. consolidating the map phases into one map phase