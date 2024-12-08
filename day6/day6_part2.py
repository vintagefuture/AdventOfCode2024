from itertools import cycle

def get_obstacles(file_path):
    obstacles_coordinates = []
    with open(file_path, 'r') as file:
        for line_y, line in (enumerate(file)):
            for i, j in enumerate(line):
                if j == '#':
                    obstacles_coordinates.append([i, line_y])
                elif j == '^':
                    initial_position = [i, line_y]

    return obstacles_coordinates, initial_position

def get_file_dimensions(file_path):
    with open(file_path) as f:
        text = f.readlines()
        total_rows = len(text) - 1
        total_columns = len(text[0]) - 2

    return [total_rows, total_columns]

def found_obstacle(obstacles_coordinates, initial_position, direction):
    next_coordinates = go_forward(initial_position, direction)
    if next_coordinates in obstacles_coordinates:
        return True

    return False

def go_forward(initial_position, direction):
    next_position = []
    up_position = [initial_position[0], initial_position[1] - 1]
    down_position = [initial_position[0], initial_position[1] + 1]
    right_position = [initial_position[0] + 1, initial_position[1]]
    left_position = [initial_position[0] - 1, initial_position[1]]
    if direction == 'up':
        next_position = up_position
    elif direction == 'down':
        next_position = down_position
    elif direction == 'left':
        next_position = left_position
    elif direction == 'right':
        next_position = right_position

    return next_position

def is_loop(obstacles_coordinates, initial_position, total_columns, total_rows):
    directions = cycle(['up', 'right', 'down', 'left'])
    current_position = initial_position
    direction = next(directions)
    while (current_position[0] <= total_columns) and (current_position[1] <= total_rows):
        next_position = go_forward(current_position, direction)
        print(next_position)
        if next_position not in obstacles_coordinates:
            current_position = next_position
            if next_position == initial_position and direction == 'up':
                return True
        else:
            direction = next(directions)

    return False

def main():
    obstacles_coordinates, initial_position = get_obstacles("test_input.txt")
    total_rows, total_columns = get_file_dimensions("test_input.txt")
    possible_loops = 0
    for i in range(total_columns + 1):
        print(i)
        for j in range(total_rows + 1):
            print(j)
            print(f'Placing additional obstacle in {[i, j]}')
            print(f'Old obstacles: {obstacles_coordinates}')
            new_obstacles_coordinates = obstacles_coordinates.copy()
            if [i, j] not in obstacles_coordinates:
                new_obstacles_coordinates.append([i,j])
            print(f'New obstacle_coordinates: {new_obstacles_coordinates}')
            loop = is_loop(new_obstacles_coordinates, initial_position, total_columns, total_rows)
            if loop:
                possible_loops += 1
        print(f"possible_loops: {possible_loops}")
    print("I never get here right?")


if __name__ == '__main__':
    main()
