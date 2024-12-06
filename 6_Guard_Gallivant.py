def read_file():
    with open("input/input_day6.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()
    
def turn_right(direction):
    if direction == "north":
        return "east"
    elif direction == "south":
        return "west"
    elif direction == "west":
        return "north"
    elif direction == "east":
        return "south"
    else:
        raise ValueError("Invalid direction")
    
def find_guard(grid):
    for i in range(len(grid)):
        if '^' in grid[i]:
            return (i, grid[i].index('^'))
    else:
        raise ValueError("Guard not found on map!")
    
def is_within_bounds(position, grid):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])

def take_step(position, direction):
    direction_to_coords = {
        "north": (-1, 0),
        "south": (1, 0),
        "west": (0, -1),
        "east": (0, 1)
    }
    return (position[0] + direction_to_coords[direction][0], position[1] + direction_to_coords[direction][1])

def next_step_clear(position, direction, grid):
    next_pos = take_step(position, direction)
    if not is_within_bounds(next_pos, grid):
        return False, False 
    valids = ['.', '^']
    return True, (grid[next_pos[0]][next_pos[1]] in valids)

def simulate(grid, start_pos, start_dir):
    current_direction = start_dir
    visited_positions = set()
    path = []
    current_pos = start_pos

    while True:
        in_bounds, clear = next_step_clear(current_pos, current_direction, grid)
        if not in_bounds:
            visited_positions.add(current_pos)
            path.append((current_pos, current_direction))
            break
        if clear:
            visited_positions.add(current_pos)
            path.append((current_pos, current_direction))
            current_pos = take_step(current_pos, current_direction)
        else:
            current_direction = turn_right(current_direction)
    return visited_positions, path

def part_one():
    grid = read_file()
    start_pos = find_guard(grid)
    start_dir = "north"
    visited, _ = simulate(grid, start_pos, start_dir)
    return len(visited)

def simulate_for_loop(grid, start_pos, start_dir):
    current_direction = start_dir
    current_pos = start_pos
    seen_states = set()

    while True:
        state = (current_pos, current_direction)
        if state in seen_states:
            return True
        seen_states.add(state)

        in_bounds, clear = next_step_clear(current_pos, current_direction, grid)
        if not in_bounds:
            return False
        if clear:
            current_pos = take_step(current_pos, current_direction)
        else:
            current_direction = turn_right(current_direction)

def part_two():
    grid = read_file()
    start_pos = find_guard(grid)
    start_dir = "north"
    visited, path = simulate(grid, start_pos, start_dir)

    loop_positions = 0
    original_grid = list(grid)
    grid_list = [list(row) for row in original_grid]

    for pos in visited:
        if pos == start_pos:
            continue

        # Place obstacle
        r, c = pos
        original_char = grid_list[r][c]
        if original_char == '#':
            continue
        grid_list[r][c] = '#'

        test_grid = [''.join(row) for row in grid_list]
        if simulate_for_loop(test_grid, start_pos, start_dir):
            loop_positions += 1

        grid_list[r][c] = original_char

    return loop_positions

def show_solutions():
    title = "--- Day 6: Guard Gallivant ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()
