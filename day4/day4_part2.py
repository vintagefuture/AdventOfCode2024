def get_matrix(file):
    matrix = []
    with open(file) as f:
        for line in f:
            row = []
            for i in line:
                if i != '\n':
                    row.append(i)
            matrix.append(row)
    return matrix

def get_diagonals_top_left_to_bottom_right(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    diagonals = []

    # Get diagonals above and including the main diagonal
    for offset in range(cols):
        diagonal = [matrix[i][i + offset] for i in range(min(rows, cols - offset))]
        diagonals.append(diagonal)

    # Get diagonals below the main diagonal
    for offset in range(1, rows):
        diagonal = [matrix[i + offset][i] for i in range(min(cols, rows - offset))]
        diagonals.append(diagonal)

    return diagonals

def get_diagonals_top_right_to_bottom_left(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    diagonals = []

    # Get diagonals above and including the anti-diagonal
    for offset in range(cols):
        diagonal = [matrix[i][cols - 1 - (i + offset)] for i in range(min(rows, cols - offset))]
        diagonals.append(diagonal)

    # Get diagonals below the anti-diagonal
    for offset in range(1, rows):
        diagonal = [matrix[i + offset][cols - 1 - i] for i in range(min(cols, rows - offset))]
        diagonals.append(diagonal)

    return diagonals

def count_xmas(char_lists):
    count = 0
    for char_list in char_lists:
        if char_list == ['M', 'A', 'S']:
            count += 1
    return count

def reverse_lists(lists):
    return [sublist[::-1] for sublist in lists[::-1]]

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def get_mini_matrices(matrix):
    mini_matrices = []
    for i in range(len(matrix)-2):
        for j in range(0, len(matrix)-2):
            mini_matrix = []
            for row in matrix[i:i+3]:
                mini_matrix.append(row[j:j+3])

            mini_matrices.append(mini_matrix)
    return mini_matrices


def main():
    matrix = get_matrix("input.txt")
    mini_matrices = get_mini_matrices(matrix)

    count = 0

    for mini_matrix in mini_matrices:

        # Main diagonal
        main_diagonal = [mini_matrix[i][i] for i in range(len(mini_matrix))]
        reverse_main_diagonal = reverse_lists(main_diagonal)

        # Anti-diagonal
        anti_diagonal = [mini_matrix[i][len(mini_matrix) - 1 - i] for i in range(len(mini_matrix))]
        reverse_anti_diagonal = reverse_lists(anti_diagonal)

        if ((main_diagonal == ['M', 'A', 'S'] or reverse_main_diagonal == ['M', 'A', 'S'])
                and (anti_diagonal == ['M', 'A', 'S'] or reverse_anti_diagonal == ['M', 'A', 'S'])):
            print_matrix(mini_matrix)
            count += 1

    print(count)


if __name__ == '__main__':
    main()

