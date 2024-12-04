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
    matrix = get_matrix("test_input.txt")
    mini_matrices = get_mini_matrices(matrix)
    top_left_to_bottom_right_diagonals = []
    reverse_top_left_to_bottom_right_diagonals = []
    top_right_to_bottom_left_diagonals = []
    reverse_top_right_to_bottom_left_diagonals = []

    lines = []

    for mini_matrix in mini_matrices:
        print_matrix(mini_matrix)

        # Main diagonal
        main_diagonal = [mini_matrix[i][i] for i in range(len(mini_matrix))]
        lines.append(main_diagonal)
        reverse_main_diagonal = reverse_lists(main_diagonal)
        lines.append(reverse_main_diagonal)
        print("Main diagonal:", main_diagonal)
        print("Reverse Main diagonal:", reverse_main_diagonal)

        # Anti-diagonal
        anti_diagonal = [mini_matrix[i][len(mini_matrix) - 1 - i] for i in range(len(mini_matrix))]
        lines.append(anti_diagonal)
        reverse_anti_diagonal = reverse_lists(anti_diagonal)
        lines.append(reverse_anti_diagonal)
        print("Anti-diagonal:", anti_diagonal)
        print("Reverse Anti-diagonal:", reverse_anti_diagonal)




    count = 0

    for line in lines:
        if line == ['M', 'A', 'S']:
            count += 1



    print(len(mini_matrices))


if __name__ == '__main__':
    main()

