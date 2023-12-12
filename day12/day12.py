import re
import functools

def check_viable_positions(wildcard_prompt: str, springs) -> int:
    question_index = wildcard_prompt.find('?')
    if question_index == -1:
        # count different instances of repeating hashes
        to_eval = [len(x) for x in re.findall(r'#+', wildcard_prompt)]
        # check if lists are identical between to_eval and order, incluging order of elements
        if len(to_eval) == len(springs) and all([x == y for x, y in zip(to_eval, springs)]):
            return 1
        else:
            return 0
        
    else:
        # replace wildcard with dot and hash
        return check_viable_positions(wildcard_prompt[:question_index] + '.' + wildcard_prompt[question_index+1:], springs) + check_viable_positions(wildcard_prompt[:question_index] + '#' + wildcard_prompt[question_index+1:], springs)

@functools.cache
def hinted_arrangements(prompt:str, springs:tuple[int]) -> int:
    if not prompt:
        return len(springs) == 0
    if not springs:
        return "#" not in prompt
    
    count = 0
    
    if prompt[0] in ".?":
        count += hinted_arrangements(prompt[1:], springs)
    
    if (
        prompt[0] in "#?" 
        and springs[0] <= len(prompt) 
        and "." not in prompt[: springs[0]] 
        and (springs[0] == len(prompt) or prompt[springs[0]] != '#')
    ):
        count += hinted_arrangements(prompt[springs[0] + 1:], springs[1:])
        
    return count

with open('day12/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
    prompts = [line.split(' ')[0] for line in lines]
    orders = [tuple(int(x.strip()) for x in line.split(' ')[1].split(',')) for line in lines]
    
    ## PART 1 ##
    perm_sum = 0
    
    for prompt, springs in zip(prompts, orders):
        # perm_sum += check_viable_positions(prompt, springs)
        perm_sum += hinted_arrangements(prompt, springs)
        
    print(f'Part 1: {perm_sum}')
    
    ## PART 2 ##
    # perm_sum_2 = 0
    
    # for prompt, springs in zip(prompts, orders):
    #     perm_sum_2 += check_viable_positions("?".join([prompt for x in range(5)]), springs*5)
        
    # print(f'Part 2: {perm_sum_2}')
    
    ## PART 2 with code (hints) from reddit ##
    perm_sum_2 = 0
    
    for prompt, springs in zip(prompts, orders):
        perm_sum_2 += hinted_arrangements("?".join([prompt] * 5), springs*5)
        
    print(f'Part 2: {perm_sum_2}')