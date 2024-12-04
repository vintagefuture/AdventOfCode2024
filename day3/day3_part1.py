import re

corrupted_string = ''
total_sum = 0

def multiply(string):
    numbers = re.findall("[0-9]+", string)
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    return number1 * number2

with open("input.txt") as f:
    for line in f:
        corrupted_string += line

results = re.findall("mul\([0-9]+,[0-9]+\)", corrupted_string)

for result in results:
    total_sum += multiply(result)

print(total_sum)