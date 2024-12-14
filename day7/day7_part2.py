import itertools
from itertools import chain, zip_longest

def parse_file(file_path):
    with open(file_path, 'r') as file:
        rows = []
        for line in file:
            row = line.replace('\n', '').replace(':', '').split(' ')
            rows.append(row)
    return rows

def all_combinations(length):
    return [p for p in itertools.product(['+', '*'], repeat=length)]

def intertwine(l1, l2):
    return [x for x in chain.from_iterable(zip_longest(l1, l2)) if x is not None]

def find_additional_equations(equations):
    additional_equations = []
    for equation in equations:
        for i in range(1,len(equation)-1):
            local_equation = equation.copy()
            first_element = local_equation.pop(i)
            second_element = local_equation.pop(i)
            smashed = f"{first_element}{second_element}"
            local_equation.insert(i, smashed)
            additional_equations.append(local_equation)
    return additional_equations

def check_equations (equations: list[list[str]]) -> [int, list[list], list[list]]:
    total = []
    equations_left_to_try = equations.copy()
    sorted = []
    for equation in equations:
        possible_operators = all_combinations(len(equation) - 2)
        target = int(equation[0])
        numbers = equation[1:]
        results = []
        for option in possible_operators:
            results.append(intertwine(numbers, option))
        for result in results:
            while len(result) > 1:
                temp_sum = 0
                first_slice = result[:3]
                temp_sum += eval(' '.join(first_slice))
                del result[0:3]
                result.insert(0, str(temp_sum))
            if temp_sum == target:
                equations_left_to_try.remove(equation)
                sorted.append(equation)
                total.append(temp_sum)
                break
    return [sum(total), sorted, equations_left_to_try]

def count_single_values(equations):
    total = 0
    for equation in equations:
        if len(equation) == 2 and equation[0] == equation[1]:
            total += int(equation[1])
    return total


if __name__ == '__main__':
    # parse input file
    equations = parse_file('test_input.txt')
    print(equations)

    # first round
    result = check_equations(equations)
    print(f"The result is {result[0]}")
    print(f"Sorted equations: {result[1]}")
    print(f"Left to try: {result[2]}")

    # second round
    more_stuff = find_additional_equations(result[2])
    print(more_stuff)
    singles = count_single_values(more_stuff)
    print(singles)
    multiples = (list(filter(lambda x: len(x) >2, more_stuff)))
    print(f"Checking on multiples {multiples}")
    additional_equations = check_equations(multiples)
    print(additional_equations[0])
    # print(f"I've found an additional {additional_equations[0]}")
    # result += count_single_values(additional_equations)
    # print(result)
    # result += check_equations(additional_equations)["total_sum"]
    # print(result)
