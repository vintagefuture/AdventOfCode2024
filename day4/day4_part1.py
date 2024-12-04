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
        for j in range(len(char_list) - 3):  # Ensure there's enough length for 'XMAS'
            if char_list[j:j + 4] == ['X', 'M', 'A', 'S']:
                count += 1
    return count

def reverse_lists(lists):
    return [sublist[::-1] for sublist in lists[::-1]]


def main():
    matrix = get_matrix("input.txt")
    rows = [row for row in matrix]
    reversed_rows = reverse_lists(rows)
    columns = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    reversed_columns = reverse_lists(columns)
    top_left_to_bottom_right_diagonals = get_diagonals_top_left_to_bottom_right(matrix)
    reverse_top_left_to_bottom_right_diagonals = reverse_lists(top_left_to_bottom_right_diagonals)
    top_right_to_bottom_left_diagonals = get_diagonals_top_right_to_bottom_left(matrix)
    reverse_top_right_to_bottom_left_diagonals = reverse_lists(top_right_to_bottom_left_diagonals)

    lines = [rows,
             reversed_rows,
             columns,
             reversed_columns,
             top_left_to_bottom_right_diagonals,
             reverse_top_left_to_bottom_right_diagonals,
             top_right_to_bottom_left_diagonals,
             reverse_top_right_to_bottom_left_diagonals ]

    count = 0
    for line in lines:
        count += count_xmas((line))

    print(count)


if __name__ == '__main__':
    main()