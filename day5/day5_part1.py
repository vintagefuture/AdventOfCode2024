from collections import defaultdict, deque

def parse_text_file(filename):
    with open(filename, 'r') as file:
        sections = file.read().split('\n\n')  # Splitting at the empty line

    first_section = [line for line in sections[0].splitlines()]
    second_section = [line for line in sections[1].splitlines()]

    return first_section, second_section

def parse_input(rules_input, updates_input):
    # Parse the ordering rules
    ordering_rules = defaultdict(list)
    for rule in rules_input:
        x, y = map(int, rule.split('|'))
        ordering_rules[x].append(y)

    # Parse the updates
    updates = [list(map(int, update.split(','))) for update in updates_input]
    print(ordering_rules.items())
    print(updates)
    return ordering_rules, updates

def check_valid_update(update, ordering_rules):
    # We need to check that update follows the ordering rules
    # Create a map of the positions of each page in the update
    position = {page: idx for idx, page in enumerate(update)}
    print(f'Position: {position}')
    for x, y_list in ordering_rules.items():
        if x in position:
            for y in y_list:
                if y in position and position[x] > position[y]:
                    # Rule is violated: x should come before y
                    return False
    return True

def get_middle_page(update):
    mid_idx = len(update) // 2
    return update[mid_idx]

def solve_sleigh_problem(rules_input, updates_input):
    # Step 1: Parse input
    ordering_rules, updates = parse_input(rules_input, updates_input)

    # Step 2: Check which updates are valid
    valid_updates = []
    for update in updates:
        if check_valid_update(update, ordering_rules):
            valid_updates.append(update)

    # Step 3: Find the middle page of each valid update and sum them
    middle_sum = sum(get_middle_page(update) for update in valid_updates)

    return middle_sum

def main():
    rules_input, updates_input = parse_text_file('test_input.txt')
    result = solve_sleigh_problem(rules_input, updates_input)
    print(result)


if __name__ == '__main__':
    main()