class MapRange:
    start = 0
    stop = 0
    offset = 0
    
    def __init__(self, source, destination, length):
        self.source = source
        self.destination = destination
        self.length = length
        self.start = source
        self.stop = source + length - 1
        self.offset = self.destination - self.source
        
    
    # check if a number belongs to this map range
    def check_belonging(self, number):
        return self.source <= number < self.source + self.length
    
    # convert number to the mapped number
    def convert(self, number):
        if self.check_belonging(number):
            return self.destination + (number - self.source)
        
    def start_stop_tuple(self):
        return (self.source, self.source + self.length - 1)
    
class NumberRange:
    start = 0
    stop = 0
    phase = 0
    
    def __init__(self, start, stop, phase):
        self.start = start
        self.stop = stop
        self.phase = phase
        
    def min(self):
        return self.start
    
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
    
    def convert_number_ranges(self, ranges):
        tmp = ranges
        for i in range(len(self.map_phases)):
            for map_range in self.map_phases[i]:
                for j in range(len(tmp)):
                    if tmp[j].phase > i:
                        continue
                    if map_range.start > tmp[j].stop or map_range.stop < tmp[j].start:
                        continue
                    else:
                        if tmp[j].start < map_range.start <= tmp[j].stop:
                            tmp.append(NumberRange(tmp[j].start, map_range.start - 1, i))
                            tmp[j] = NumberRange(map_range.start, tmp[j].stop, i)
                        if tmp[j].start <= map_range.stop < tmp[j].stop:
                            tmp.append(NumberRange(map_range.stop + 1, tmp[j].stop, i))
                            tmp[j] = NumberRange(tmp[j].start, map_range.stop, i)
                        if tmp[j].start >= map_range.start and tmp[j].stop <= map_range.stop:
                            tmp[j] = NumberRange(map_range.offset + tmp[j].start, map_range.offset + tmp[j].stop, i+1)
        return tmp 
    
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
    
    # turn seeds into number ranges of (start, stop)
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append(NumberRange(seeds[i], seeds[i] + seeds[i+1] - 1, 0))
        
    loc_ranges = mapper.convert_number_ranges(seed_ranges)
    
    print("Part 2: " + str(min([x.min() for x in loc_ranges])))