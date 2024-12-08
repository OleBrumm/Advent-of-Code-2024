def read_file():
    with open("input/input_day7.txt", 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    

def possible_results(numbers, concat=False):
    possible = {numbers[0]}
    for y in numbers[1:]:
        new_possible = set()
        for x in possible:
            new_possible.add(x + y)
            new_possible.add(x * y)
            if concat:
                new_possible.add(int(str(x) + str(y)))
        possible = new_possible
    return possible


def part_one():
    lines = read_file()
    total_sum = 0
    for line in lines:
        parts = line.split(':')
        test_value = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))
        if test_value in possible_results(numbers):
            total_sum += test_value
    return total_sum

def part_two():
    lines = read_file()
    total_sum = 0
    for line in lines:
        parts = line.split(':')
        test_value = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))
        if test_value in possible_results(numbers, True):
            total_sum += test_value
    return total_sum


def show_solutions():
    title = "--- Day 7: Bridge Repair ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()
