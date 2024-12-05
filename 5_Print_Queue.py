def read_file():
    with open("input/input_day5.txt", 'r', encoding='utf-8') as f:
        return f.read().split('\n\n')
    
    
def is_correct_order(update, rules):
    for rule in rules:
        page_x, page_y = rule
        if page_x in update and page_y in update:
            if update.index(page_x) > update.index(page_y):
                return False
    return True
    

def follows_rule(update, rule):
    page_x, page_y = rule
    if page_x in update and page_y in update:
        if update.index(page_x) > update.index(page_y):
            return False
    return True


def swap_by_rule(update, rule):
    page_x, page_y = rule
    index_x, index_y = update.index(page_x), update.index(page_y)
    update[index_x], update[index_y] = update[index_y], update[index_x]
    return update
    

def switch_incorrect(update, rules):
    i = 0
    while i < len(rules):
        rule = rules[i]
        page_x, page_y = rule
        if page_x in update and page_y in update:
            if update.index(page_x) > update.index(page_y):
                update = swap_by_rule(update, rule)
                i = 0
            else:
                i += 1
        else:
            i += 1
    return update
        
def part_one():
    (rules, updates) = read_file()
    rules = [rule.split('|') for rule in rules.split('\n')]
    updates = [update.split(',') for update in updates.strip().split('\n')]

    middle_page_num_sum = 0
    for update in updates:
        if is_correct_order(update, rules):
            middle_index = len(update) // 2
            middle_page_num_sum += int(update[middle_index])
    return middle_page_num_sum


def part_two():
    (rules, updates) = read_file()
    rules = [rule.split('|') for rule in rules.split('\n')]
    updates = [update.split(',') for update in updates.strip().split('\n')]

    middle_page_num_sum = 0
    for update in updates:
        if is_correct_order(update, rules):
            continue
        else:
            update = switch_incorrect(update, rules)
        middle_index = len(update) // 2
        middle_page_num_sum += int(update[middle_index]) 
    return middle_page_num_sum
        

def show_solutions():
    title = "--- Day 5: Print Queue ---"
    print(title)
    print(f"Part one: {part_one()}".center(len(title)))
    print(f"Part two: {part_two()}".center(len(title)))

if __name__ == "__main__":
    show_solutions()