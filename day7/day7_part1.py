import operator
import itertools
from itertools import chain, zip_longest

def parse_file(file_path):
    with open(file_path, 'r') as file:
        rows = []
        for line in file:
            row = line.replace('\n', '').replace(':', '').split(' ')
            rows.append(row)
    return rows

ops = {
    '+' : operator.add,
    '*' : operator.mul,
}

def all_combinations(length):
    return [p for p in itertools.product(['+', '*'], repeat=length)]

def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return ops[oper](op1, op2)

def intertwine(l1, l2):
    return [x for x in chain.from_iterable(zip_longest(l1, l2)) if x is not None]


if __name__ == '__main__':
    equations = parse_file('test_input.txt')
    total = 0
    for equation in equations:
        possible_operators = all_combinations(len(equation) - 2)
        target = int(equation[0])
        numbers = equation[1:]
        results = []
        for option in possible_operators:
            results.append(intertwine(numbers, option))
        for result in results:
            while len(result) >= 3:
                temp_sum = 0
                print(f'Expression to evaluate is {result}')
                print("Consider the first operation")
                first_slice = result[:3]
                print(f'First slice {first_slice}')
                print(f"I'm going to evaluate {' '.join(first_slice)} which returns {eval(' '.join(first_slice))}")
                temp_sum += eval(' '.join(first_slice))
                del result[0:3]
                print(f"I removed the slice so that the resulting list is {result}")
                result.insert(0, str(temp_sum))
                print(f"And now I re-added the result of the first slice which is {str(temp_sum)} so that the resulting list is now {result}")
            print(f"I stopped since I reached the end! The final temp_sum is {temp_sum}")
            if temp_sum == target:
                total += temp_sum
                print(f'and we have a match with {temp_sum}')

        print(f"the total is {total}")












