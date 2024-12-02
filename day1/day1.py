import numpy as np

def parse_file_to_array(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            row = [int(num) for num in numbers]
            matrix.append(row)
    return matrix

def main():
    # load file into a Numpy matrix
    parsed_file = parse_file_to_array("./day1/day1_input.txt")
    matrix = np.array(parsed_file)

    # sort matrix
    matrix = np.sort(matrix, axis=0)

    total_rows = matrix.shape[0]
    total_sum = 0

    for i in range(total_rows):
        row_difference = abs(matrix[i, 0] - matrix[i, 1])
        total_sum += row_difference

    print(f'The total sum of differences is {total_sum}')

    # Extract the first column
    first_column = [i[0] for i in parsed_file]

    # Extract the second column
    second_column = [i[1] for i in parsed_file]

    similarity_score = 0
    for i in first_column:
        print(f'The number {i} appears {second_column.count(i)} in the second column')
        similarity_score += (second_column.count(i) * i)

    # print(first_column)
    print(f'The similarity score is {similarity_score}')


if __name__ == "__main__":
    main()
