def read_file():
    with open("input/input_day2.txt", "r", encoding="utf-8") as file:
        lines = [list(map(int, line.strip().split())) for line in file]
    return lines


def part_one():
    return sum(check_line(line) for line in read_file())


def part_two():
    return sum(any(check_line(line[:i] + line[i + 1:]) for i in range(len(line) + 1)) for line in read_file())


def check_line(line):
    return (
            all(0 < line[i + 1] - line[i] <= 3 for i in range(len(line) - 1)) or
            all(-3 <= line[i + 1] - line[i] < 0 for i in range(len(line) - 1))
    )


def show_solutions():
    title = "--- Day 2: Red-Nosed Reports ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))


if __name__ == "__main__":
    show_solutions()
