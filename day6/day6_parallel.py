import concurrent.futures
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
        total_rows = len(text)
        total_columns = len(text[0].strip())  # Adjust for trailing newlines if necessary

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

def is_loop(obstacles_coordinates, initial_position, total_rows, total_columns):
    total_positions = 0
    directions = cycle(['up', 'right', 'down', 'left'])
    current_position = initial_position
    direction = next(directions)
    encountered_obstacle = dict()
    visited = [initial_position]
    while (0 <= current_position[0] < total_columns) and (0 <= current_position[1] < total_rows):
        next_position = go_forward(current_position, direction)
        if next_position not in obstacles_coordinates:
            if next_position not in visited:
                total_positions += 1
            current_position = next_position
            visited.append(next_position)
        elif tuple(next_position) in encountered_obstacle and encountered_obstacle[tuple(next_position)] == direction:
            return True
        else:
            encountered_obstacle[tuple(next_position)] = direction
            direction = next(directions)

    return False

# Function to check if a loop exists for given (i, j)
def check_for_loop(obstacles_coordinates, original_obstacles, i, j, initial_position, total_rows, total_columns):
    obstacles_coordinates = original_obstacles.copy()  # Reset obstacles each time
    obstacles_coordinates.append([i, j])
    return is_loop(obstacles_coordinates, initial_position, total_rows, total_columns)


if __name__ == '__main__':
    obstacles_coordinates, initial_position = get_obstacles("input.txt")
    total_rows, total_columns = get_file_dimensions("input.txt")
    original_obstacles = obstacles_coordinates.copy()

    loops_found = 0

    # Using ProcessPoolExecutor for parallelism
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Generate tasks for each (i, j) pair
        futures = [executor.submit(check_for_loop, obstacles_coordinates, original_obstacles, i, j, initial_position, total_rows, total_columns)
                   for j in range(total_columns) for i in range(total_rows)]

        # Collect results
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                loops_found += 1

    print(f"Loops found: {loops_found}")
