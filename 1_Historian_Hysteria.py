from collections import Counter

def read_file():
    with open("input/input_day1.txt", 'r', encoding='utf-8') as f:
        pairs = [line.strip().split() for line in f.read().splitlines()]
    return pairs

def create_lists():
    pairs = read_file()
    left = [int(pair[0]) for pair in pairs]
    right = [int(pair[1]) for pair in pairs]
    return sorted(left), sorted(right)

def part_one():
    left, right = create_lists()
    diff = [abs(l - r) for l, r in zip(left, right)]
    return sum(diff)

def part_two():
    left, right = create_lists()
    left_counts = Counter(left)
    right_counts = Counter(right)
    return sum([num * left_counts[num] * right_counts[num] for num in left_counts if num in right_counts])

def show_solutions():
    title = "--- Day 1: Historian Hysteria ---"
    print(title)
    print(f'Part one: {str(part_one())}'.center(len(title)))
    print(f'Part two: {str(part_two())}'.center(len(title)))

if __name__ == '__main__':
    show_solutions()