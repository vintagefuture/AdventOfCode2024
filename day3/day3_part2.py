import re

multiplication_total = 0

with open('input.txt') as f:
    instructions = re.findall(r'(?:do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\))', f.read())


def multiply(x, y):
    return x * y


include = True
print(instructions)
for instruction in instructions:
    if instruction == 'do()':
        include = True
    elif instruction == 'don\'t()':
        include = False
    elif include:
        print(instruction[4:-1].split(','))
        multiplication_total += multiply(*map(int, instruction[4:-1].split(',')))


instruction = ['mul(229,919)', 'mul(187,600)', 'mul(430,339)']

