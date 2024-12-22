from functools import cache

def read_file():
    with open("input/input_day11.txt", 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    
def parse_input():
    data_str = read_file()
    return list(map(int, data_str[0].split(' ')))

@cache
def get_new_stones(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_one = int(str(stone)[:len(str(stone)) // 2])
        stone_two = int(str(stone)[len(str(stone)) // 2:])
        return [stone_one, stone_two]
    else:
        return [stone * 2024]

@cache
def get_blinked_stone(stone, n):
    if n == 0:
        return 1
    new_stones = get_new_stones(stone)
    return sum(get_blinked_stone(new_stone, n - 1) for new_stone in new_stones)

def part_one():
    data = parse_input()
    return sum(get_blinked_stone(stone, 25) for stone in data)

def part_two():
    data = parse_input()
    return sum(get_blinked_stone(stone, 75) for stone in data)
            
def show_solutions():
    title = "--- Day 11: Plutonium Pebbles ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()
