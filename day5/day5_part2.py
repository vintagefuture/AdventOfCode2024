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

    return ordering_rules, updates


def check_valid_update(update, ordering_rules):
    # We need to check that update follows the ordering rules
    # Create a map of the positions of each page in the update
    position = {page: idx for idx, page in enumerate(update)}

    for x, y_list in ordering_rules.items():
        if x in position:
            for y in y_list:
                if y in position and position[x] > position[y]:
                    # Rule is violated: x should come before y
                    return False
    return True


def topological_sort(update, ordering_rules):
    # Perform topological sort on the pages in the update using the ordering rules
    # 1. Build a graph for this update
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Only include the rules that apply to this update
    for page in update:
        graph[page] = []
        in_degree[page] = 0

    for x, y_list in ordering_rules.items():
        if x in update:
            for y in y_list:
                if y in update:
                    graph[x].append(y)
                    in_degree[y] += 1

    # 2. Kahn's algorithm to perform topological sort
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current_page = queue.popleft()
        sorted_pages.append(current_page)

        for neighbor in graph[current_page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages


def get_middle_page(update):
    mid_idx = len(update) // 2
    return update[mid_idx]


def solve_sleigh_problem_with_fixes(rules_input, updates_input):
    # Step 1: Parse input
    ordering_rules, updates = parse_input(rules_input, updates_input)

    # Step 2: Check which updates are valid and fix those that aren't
    fixed_updates = []

    for update in updates:
        if not check_valid_update(update, ordering_rules):
            # Reorder the update using topological sort
            sorted_update = topological_sort(update, ordering_rules)
            fixed_updates.append(sorted_update)

    # Step 3: Find the middle page of each fixed update and sum them
    middle_sum = sum(get_middle_page(update) for update in fixed_updates)

    return middle_sum


# Example input based on the problem statement
rules_input, updates_input = parse_text_file('input.txt')

# Solve the problem
result = solve_sleigh_problem_with_fixes(rules_input, updates_input)
print(result)
