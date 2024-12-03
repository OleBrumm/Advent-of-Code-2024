import re
from functools import reduce
from operator import mul

def read_file():
    with open("input/input_day3.txt", "r", encoding="utf-8") as file:
        return file.read()
    
def part_one():
    occurrences = re.findall(r'mul\((\d+),(\d+)\)', read_file())
    return sum(reduce(mul, map(int, match)) for match in occurrences)


def part_two():
    instructions = re.split(r'(do\(\)|don\'t\(\))', read_file())
    is_enabled = True 
    total = 0
    for instruction in instructions:
        if instruction == 'do()':
            is_enabled = True
        elif instruction == "don't()":
            is_enabled = False
        else:
            occurrences = re.findall(r'mul\((\d+),(\d+)\)', instruction)
            if is_enabled:
                total += sum(reduce(mul, map(int, match)) for match in occurrences)
    
    return total

def show_solutions():
    title = "--- Day 3: Mull It Over ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    

if __name__ == "__main__":
    show_solutions()