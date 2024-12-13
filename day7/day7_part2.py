# --- Part Two ---
#
# The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.
#
# The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.
#
# Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:
#
#     156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
#     7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
#     192: 17 8 14 can be made true using 17 || 8 + 14.
#
# Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.
#
# Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?

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

def main():
    equations = parse_file('input.txt')
    total = []
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
                total.append(temp_sum)
                break
    print(f"The total is {sum(total)}")

def transform_equation(equation):
    pass



if __name__ == '__main__':
    equations = parse_file('test_input.txt')
    for equation in equations:
        print(equation)
        for i in range(1,len(equation)-1):
            print(f"{equation[i]}{equation[i+1]}")