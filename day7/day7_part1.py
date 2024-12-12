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

if __name__ == '__main__':
    main()
