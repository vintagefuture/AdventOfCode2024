def get_obstacles(file_path):
    obstacles_coordinates = []
    with open(file_path, 'r') as file:
        for line_y, line in (enumerate(file)):
            for i, j in enumerate(line):
                if j == '#':
                    obstacles_coordinates.append([i, line_y])
                elif j == '^':
                    guard_initial_position = [i, line_y]

    return obstacles_coordinates, guard_initial_position


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

def main():
    obstacles_coordinates, initial_position = get_obstacles("test_input.txt")
    direction = 'up'
    total_positions = 1
    while not found_obstacle(obstacles_coordinates, initial_position, direction):
        initial_position = go_forward(initial_position, direction)
        print(initial_position)
        total_positions += 1

    print(total_positions)



if __name__ == '__main__':
    main()
