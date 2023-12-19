workflows = {}

def parse_workflow(line: str) -> None:
    workflow_id, workflow = line.strip('}').split('{')
    conditions = workflow.split(',')
    parsed_conditions = []
    for condition in conditions[:-1]:
        category = condition[0]
        operator = condition[1]
        value = int(condition[2:].split(':')[0])
        passed = condition[2:].split(':')[1]
        parsed_conditions.append({"category": category, "operator": operator, "value": value, "passed": passed})
        
    workflows[workflow_id] = {"conditions": parsed_conditions, "fin": conditions[-1]}

def parse_part(line: str) -> dict:
    part = {}
    category_values = line.strip('\{\}').split(',')
    for category_value in category_values:
        category, value = category_value.split('=')
        part[category] = int(value.strip())
    return part

def validate_part(part, workflow: str) -> bool:
    if workflow == 'A':
        return True
    if workflow == 'R':
        return False
    
    workflow_tmp = workflows[workflow]
    for condition in workflow_tmp["conditions"]:
        if condition["operator"] == ">" and part[condition["category"]] > condition["value"]:
            return validate_part(part, condition["passed"])
        elif condition["operator"] == "<" and part[condition["category"]] < condition["value"]:
            return validate_part(part, condition["passed"])
    
    return validate_part(part, workflow_tmp["fin"])

def validate_part_part2(part_range, workflow: str) -> list[list[tuple[int], bool]]:
    if workflow == 'A':
        return [part_range, True]
    if workflow == 'R':
        return [part_range, False]
    
    workflow_tmp = workflows[workflow]
    for condition in workflow_tmp["conditions"]:
        if condition["operator"] == ">" and part_range[condition["category"]][1] > condition["value"]:
            if part_range[condition["category"]][0] > condition["value"]:
                # no need to split part_range on this category
                return validate_part_part2(part_range, condition["passed"])
            # split part_range on this category
            tmp_part_range = part_range.copy()
            tmp_part_range[condition["category"]] = (part_range[condition["category"]][0], condition["value"])
            part_range[condition["category"]] = (condition["value"] + 1, part_range[condition["category"]][1])
            return validate_part_part2(part_range, condition["passed"]) + validate_part_part2(tmp_part_range, workflow)
        if condition["operator"] == "<" and part_range[condition["category"]][0] < condition["value"]:
            if part_range[condition["category"]][1] < condition["value"]:
                # no need to split part_range on this category
                return validate_part_part2(part_range, condition["passed"])
            # split part_range on this category
            tmp_part_range = part_range.copy()
            tmp_part_range[condition["category"]] = (condition["value"], part_range[condition["category"]][1])
            part_range[condition["category"]] = (part_range[condition["category"]][0], condition["value"] - 1)
            return validate_part_part2(part_range, condition["passed"]) + validate_part_part2(tmp_part_range, workflow)
            
    return validate_part_part2(part_range, workflow_tmp["fin"])

with open('day19/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    
    workflow_cond = True
    parts : list[dict] = []
    
    for line in lines:
        if line == '':
            workflow_cond = False
            continue
        if workflow_cond:
            parse_workflow(line)
        else:
            parts.append(parse_part(line))
        
    ## PART 1 ##
    parts_sum = 0
        
    for part in parts:
        if validate_part(part, 'in'):
            parts_sum += sum(part.values())
            
    print(f'Part 1: {parts_sum}')
    
    ## PART 2 ##
    part_range = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
        }
    
    part_ranges = validate_part_part2(part_range, 'in')
    
    part_ranges_sum = 0
    
    for i in range(0, len(part_ranges), 2):
        if part_ranges[i+1]:
            part_ranges_sum += (part_ranges[i]["x"][1] - part_ranges[i]["x"][0] + 1) * (part_ranges[i]["m"][1] - part_ranges[i]["m"][0] + 1) * (part_ranges[i]["a"][1] - part_ranges[i]["a"][0] + 1) * (part_ranges[i]["s"][1] - part_ranges[i]["s"][0] + 1)
    
    print(f'Part 2: {part_ranges_sum}')
    