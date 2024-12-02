import numpy as np

def parse_file_to_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            row = [int(num) for num in numbers]
            matrix.append(row)
    return matrix


def main():
    # load file into a matrix
    parsed_file = parse_file_to_matrix("day1_input.txt")
    matrix = np.array(parsed_file)

    # sort matrix
    matrix = np.sort(matrix, axis=0)

    total_rows = matrix.shape[0]
    total_sum = 0

    for i in range(total_rows):
        row_difference = abs(matrix[i, 0] - matrix[i, 1])
        total_sum += row_difference

    print(total_sum)

    print(parsed_file)

    c = np.count_nonzero(matrix == 98629)
    print('Total occurrences of "98629" in array: ', c)


if __name__ == "__main__":
    main()
