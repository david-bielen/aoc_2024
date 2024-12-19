# /// script
# dependencies = []
# ///

from input_data import input_string

input_string = input_string.replace("S", ">")


grid = {
    (j, i): grid_char
    for i, row in enumerate(input_string.split("\n"))
    for j, grid_char in enumerate(row)
}


def print_grid(grid):
    rows = max(key[1] for key in grid.keys()) + 1
    cols = max(key[0] for key in grid.keys()) + 1
    for row in range(rows):
        print("".join(grid.get((col, row), " ") for col in range(cols)))
    print("\n")


def get_current_position(grid):
    return next((pos for pos, value in grid.items() if value in "><^v"), None)


def get_final_position(grid):
    return next((pos for pos, value in grid.items() if value == "E"), None)


final_position = get_final_position(grid)


def get_possible_neighbours(current_position, current_orientation, grid):
    opposite_positions = {
        ">": (-1, 0),
        "<": (1, 0),
        "^": (0, 1),
        "v": (0, -1),
    }
    cx, cy = current_position
    valid_directions = [
        (dx, dy)
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if (dx, dy) != opposite_positions[current_orientation]
    ]
    return [
        (cx + delta_x, cy + delta_y)
        for (delta_x, delta_y) in valid_directions
        if grid.get((cx + delta_x, cy + delta_y)) in ".E"
    ]


def calculate_number_of_rotations_to_next_position(
    current_position, current_orientation, next_position
):
    cx, cy = current_position
    dx, dy = next_position

    direction_checks = {
        ">": dx > cx,
        "<": dx < cx,
        "^": dy < cy,
        "v": dy > cy,
    }

    if direction_checks[current_orientation]:
        return 0
    if (
        current_orientation in [">", "<"]
        and dx != cx
        or current_orientation in ["^", "v"]
        and dy != cy
    ):
        return 2
    return 1


def move_element_to_next_position(current_position, next_position, grid):
    print(current_position, next_position)
    grid[current_position], grid[next_position] = (
        grid[next_position],
        grid[current_position],
    )
    return grid


def cost_of_move_to_next_position(
    current_position,
    current_orientation,
    next_position,
):
    return (
        1000
        * calculate_number_of_rotations_to_next_position(
            current_position, current_orientation, next_position
        )
    ) + 1


def get_next_orientation(current_position, next_position):
    cx, cy = current_position
    dx, dy = next_position
    if dx > cx:
        return ">"
    if dx < cx:
        return "<"
    if dy > cy:
        return "v"
    if dy < cy:
        return "^"
    raise ValueError("Disoriented, buddy?")


current_position = get_current_position(grid)
current_orientation = grid[current_position]


cost_dict = {(current_position, current_orientation): 0}

to_explore = [(current_position, current_orientation)]
while True:
    if not to_explore:
        break
    current_position, current_orientation = to_explore.pop(0)
    for next_position in get_possible_neighbours(
        current_position, current_orientation, grid
    ):
        next_orientation = get_next_orientation(current_position, next_position)
        cost_of_next_state = (
            cost_of_move_to_next_position(
                current_position, current_orientation, next_position
            )
            + cost_dict[(current_position, current_orientation)]
        )
        if (
            next_position,
            next_orientation,
        ) not in cost_dict or cost_of_next_state < cost_dict[
            (next_position, next_orientation)
        ]:
            cost_dict[(next_position, next_orientation)] = cost_of_next_state
            to_explore.append((next_position, next_orientation))
print(
    min(
        cost_dict.get((final_position, orientation), float("inf"))
        for orientation in [">", "<", "^", "v"]
    )
)
