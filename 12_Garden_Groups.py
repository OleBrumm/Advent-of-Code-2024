def read_file():
    with open("input/input_day12.txt", 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    
def parse_input():
    data_str = read_file()
    return data_str

def find_area_and_perimeter(data, i, j, visited):
    char = data[i][j]  
    stack = [(i, j)]
    visited.add((i, j))

    area = 0
    perimeter = 0
    rows = len(data)
    cols = len(data[0])

    while stack:
        x, y = stack.pop()
        area += 1

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < rows and 0 <= ny < cols and data[nx][ny] == char):
                perimeter += 1
            else:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))

    return area, perimeter 

def find_area_and_sides(data, i, j, visited):
    char = data[i][j]  
    stack = [(i, j)]
    visited.add((i, j))

    region_cells = []
    rows = len(data)
    cols = len(data[0])

    while stack:
        x, y = stack.pop()
        region_cells.append((x, y))
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and
                data[nx][ny] == char and 
                (nx, ny) not in visited):
                visited.add((nx, ny))
                stack.append((nx, ny))

    area = len(region_cells)
    
    boundary_edges = []
    for (x, y) in region_cells:
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < rows and 0 <= ny < cols and data[nx][ny] == char):
                boundary_edges.append(((x, y), (nx, ny)))

    boundary_edges = set(boundary_edges)

    sides_set = set()
    for p1, p2 in boundary_edges:
        keep_edge = True
        for ddx, ddy in [(1,0), (0,1)]:
            p1n = (p1[0] + ddx, p1[1] + ddy)
            p2n = (p2[0] + ddx, p2[1] + ddy)
            if (p1n, p2n) in boundary_edges:
                keep_edge = False
                break
        if keep_edge:
            sides_set.add((p1, p2))

    sides = len(sides_set)

    return area, sides
        

def part_one():
    data = parse_input()
    visited = set()
    result = 0
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) not in visited:
                area, perimeter = find_area_and_perimeter(data, i, j, visited)
                result += area * perimeter
    
    return result
        
def part_two():
    data = parse_input()
    visited = set()
    result = 0
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) not in visited:
                area, perimeter = find_area_and_sides(data, i, j, visited)
                result += area * perimeter
    
    return result
            
def show_solutions():
    title = "--- Day 12: Garden Groups ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()