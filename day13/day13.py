def parse_pattern(pattern: list[str]) -> tuple[tuple[int], tuple[int]]:
    # transform grid into a list of tuples counting consecutive dots and hashes
    # one tuple for rows and one tuple for columns
    rows = []
    cols = []
    for row in pattern:
        # count the number of consecutive . and # in each row
        count = []
        tmp = [row[0]]
        for symbol in list(row[1:]):
            if symbol == tmp[0]:
                tmp.append(symbol)
            else:
                count.append(-len(tmp) if tmp[0] == '.' else len(tmp))
                tmp = [symbol]
        count.append(-len(tmp) if tmp[0] == '.' else len(tmp))
        rows.append(tuple(count))
        
    for col in zip(*pattern):
        count = []
        tmp = [col[0]]
        for symbol in list(col[1:]):
            if symbol == tmp[0]:
                tmp.append(symbol)
            else:
                count.append(-len(tmp) if tmp[0] == '.' else len(tmp))
                tmp = [symbol]
        count.append(-len(tmp) if tmp[0] == '.' else len(tmp))
        cols.append(tuple(count))
    
    return tuple(rows), tuple(cols)

def check_pattern_for_mirror_line(rows, columns):
    # check every between line for a mirror image in rows
    r_count = 0
    for i in range(1, len(rows)):
        mirror = True
        for j in range(min(i, len(rows) - i)):
            if rows[i - j - 1] != rows[i + j]:
                mirror = False
                break
        r_count += i if mirror else 0
    # check every between line for a mirror image in columns
    c_count = 0
    for i in range(1, len(columns)):
        mirror = True
        for j in range(min(i, len(columns) - i)):
            if columns[i - j - 1] != columns[i + j]:
                mirror = False
                break
        c_count += i if mirror else 0

    return r_count, c_count

with open('day13/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
    patterns = []
    tmp = []
    for line in lines:
        if line == '':
            patterns.append(parse_pattern(tmp))
            tmp = []
        else:
            tmp.append(line)
    patterns.append(parse_pattern(tmp))
    
    ## PART 1 ##
    # for every pattern, check if there is a mirror image inside it
    # both in columns and rows
    # count all the rows and columns on the left of up from the mirror line
    # multiply the row count by 100 and add the column count
    
    total_count = 0
    
    for rows, columns in patterns:
        r, c = check_pattern_for_mirror_line(rows, columns)
        total_count += r * 100 + c
    
    print(f'Part 1: {total_count}')
    