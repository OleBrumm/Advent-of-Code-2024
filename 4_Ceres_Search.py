def read_file():
    with open("input/input_day4.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def is_in_bounds(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def find_word(x, y, dx, dy, word, grid):
    for i, char in enumerate(word):
        nx, ny = x + dx * i, y + dy * i
        if not is_in_bounds(nx, ny, grid) or grid[ny][nx] != char:
            return False
    return True


def part_one():
    grid = read_file()
    count = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),   
        (1, -1),  (1, 0),  (1, 1)   
    ]
    word = "XMAS"

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == word[0]:
                for dx, dy in directions:
                    if find_word(x, y, dx, dy, word, grid):
                        count += 1
    return count


def part_two():
    grid = read_file()
    count = 0
    required_sequences = [["M", "A", "S"], ["S", "A", "M"]]

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == "A" and is_x_mas(x, y, grid, required_sequences):
                count += 1
    return count


def is_x_mas(x, y, grid, sequences):
    diagonals = [
        [grid[y - 1][x - 1], grid[y][x], grid[y + 1][x + 1]],
        [grid[y - 1][x + 1], grid[y][x], grid[y + 1][x - 1]],
    ]
    matches = 0
    for diagonal in diagonals:
        if diagonal in sequences or diagonal[::-1] in sequences:
            matches += 1
    return matches == 2


def show_solutions():
    title = "--- Day 4: Ceres Search ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))


if __name__ == "__main__":
    show_solutions()
