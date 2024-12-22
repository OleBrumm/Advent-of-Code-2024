from collections import deque

def read_file():
    with open("input/input_day10.txt", 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    
def parse_input():
    data_str = read_file()
    return data_str

def find_starts(data):
    starts = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '0':
                starts.append((x, y))
    return starts  

def get_score_rating(data, x, y, part_two=False):
    queue = deque([(x, y)])
    visited = set()
    visited_nines = set()
    score_rating = 0
    while queue:
        x, y = queue.popleft()
        if not part_two: # Only checks for visited if not part two
            if (x, y) in visited:
                continue
            visited.add((x, y))
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + direction[0], y + direction[1]
            if 0 <= new_x < len(data[0]) and 0 <= new_y < len(data):
                if int(data[new_y][new_x]) == int(data[y][x]) + 1:
                    queue.append((new_x, new_y))
                    if int(data[new_y][new_x]) == 9:
                        if not part_two: # Only checks for visited nines if not part two
                            if (new_x, new_y) in visited_nines:
                                continue
                            visited_nines.add((new_x, new_y))
                        score_rating += 1
                                                               
    return score_rating

def part_one():
    data = parse_input()
    starts = find_starts(data)
    scores = [get_score_rating(data, x, y) for x, y in starts]
    return sum(scores)

def part_two():
    data = parse_input()
    starts = find_starts(data)
    scores = [get_score_rating(data, x, y, True) for x, y in starts]
    return sum(scores)          
    
def show_solutions():
    title = "--- Day 10: Hoof It ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()