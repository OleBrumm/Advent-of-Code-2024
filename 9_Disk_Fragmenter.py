from collections import deque

def read_file():
    with open("input/input_day9.txt", 'r', encoding='utf-8') as f:
        return f.read().strip()
    
def parse_input():
    data_str = read_file()
    return list(map(int, data_str))

def build_disk_block_moving(data):
    disk = deque()
    file_id = 0
    for i, length in enumerate(data):
        if i % 2 == 0:
            disk.extend([file_id] * length)
            file_id += 1
        else:
            disk.extend([None] * length)
    return disk

def compact_disk_block_moving(disk):
    k = 0
    while k < len(disk):
        if disk[k] is not None:
            k += 1
        else:
            tail = disk.pop()
            if tail is not None:
                disk[k] = tail
                k += 1
            else:
                continue

def build_disk_file_moving(data):
    disk = []
    files = {}
    
    file_id = 0
    pos = 0
    for i in range(len(data)):
        length = data[i]
        if i % 2 == 0:
            disk.extend([file_id] * length)
            files[file_id] = (pos, length)
            file_id += 1
        else:
            disk.extend([None] * length)
        pos += length
    
    return disk, files

def compact_disk_file_moving(disk, files):
    for file_id, (start_pos, size) in sorted(files.items(), reverse=True):
        run = 0
        run_start = 0
        
        for i in range(start_pos):
            if disk[i] is None:
                if run == 0:
                    run_start = i
                run += 1
                if run == size:
                    for j in range(size):
                        disk[run_start + j] = file_id
                        disk[start_pos + j] = None
                    break
            else:
                run = 0
                
def compute_checksum(disk):
    return sum(i * b for i, b in enumerate(disk) if b is not None)
                
def part_one():
    data = parse_input()
    disk = build_disk_block_moving(data)
    compact_disk_block_moving(disk)
    return compute_checksum(disk)

def part_two():
    data = parse_input()
    disk, files = build_disk_file_moving(data)
    compact_disk_file_moving(disk, files)
    return compute_checksum(disk)
            
    
def show_solutions():
    title = "--- Day 9: Disk Fragmenter ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))
    
if __name__ == "__main__":
    show_solutions()
