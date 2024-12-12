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
        target = equation[0]
        numbers = equation[1:]
        results = []
        for option in possible_operators:
            results.append(' '.join(intertwine(numbers, option)))
        for result in results:
            print(str(result))
            if eval(result) == target:
                total += eval(result)

    print(total)

