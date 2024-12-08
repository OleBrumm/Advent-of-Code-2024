def read_file():
    with open("input/input_day8.txt", 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    
    
def build_frequency_dict(lines): 
    frequency_dict = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '.':
                continue
            frequency_dict.setdefault(char, []).append((x, y))
    return frequency_dict

def add_antinodes_for_pair(x1, y1, x2, y2, width, height, antinodes):
    x_diff = x2 - x1
    y_diff = y2 - y1

    x3, y3 = x2 + x_diff, y2 + y_diff
    x4, y4 = x1 - x_diff, y1 - y_diff

    if 0 <= x3 < width and 0 <= y3 < height:
        antinodes.add((x3, y3))
    if 0 <= x4 < width and 0 <= y4 < height:
        antinodes.add((x4, y4))
        
def add_extended_antinodes_for_pair(x1, y1, x2, y2, width, height, antinodes):
    x_diff = x2 - x1
    y_diff = y2 - y1
    max_dim = max(width, height)

    for scalar in range(-max_dim, max_dim):
        x3, y3 = x2 + x_diff * scalar, y2 + y_diff * scalar
        x4, y4 = x1 - x_diff * scalar, y1 - y_diff * scalar

        if 0 <= x3 < width and 0 <= y3 < height:
            antinodes.add((x3, y3))
        if 0 <= x4 < width and 0 <= y4 < height:
            antinodes.add((x4, y4))
    
    
def part_one():
    lines = read_file()
    height = len(lines)
    width = len(lines[0])
    
    frequency_dict = build_frequency_dict(lines)
    antinodes = set()
        
    for freq, positions in frequency_dict.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                add_antinodes_for_pair(x1, y1, x2, y2, width, height, antinodes)
                    
    return len(antinodes)
            
def part_two():
    lines = read_file()
    height = len(lines)
    width = len(lines[0])
    
    frequency_dict = build_frequency_dict(lines)
    antinodes = set()
    
    for freq, positions in frequency_dict.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                add_extended_antinodes_for_pair(x1, y1, x2, y2, width, height, antinodes)     
                    
    return len(antinodes)


def show_solutions():
    title = "--- Day 8: Resonant Collinearity ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()
