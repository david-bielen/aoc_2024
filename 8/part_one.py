from itertools import combinations

from input_data import input_string

rows = input_string.splitlines()
matrix_dict = {(r, c): char for r, row in enumerate(rows) for c, char in enumerate(row)}
total_rows, total_columns = len(rows), len(rows[0])
unique_chars = {char for char in input_string if char not in {".", "\n"}}


def is_within_matrix(point):
    r, c = point
    return 0 <= r < total_rows and 0 <= c < total_columns


def calculate_antinode_locations(a1, a2):
    x1, y1, x2, y2 = *a1, *a2
    return [(2 * x1 - x2, 2 * y1 - y2), (2 * x2 - x1, 2 * y2 - y1)]


print(
    len(
        {
            antinode
            for char in unique_chars
            for a1, a2 in combinations(
                [pos for pos, val in matrix_dict.items() if val == char], 2
            )
            for antinode in calculate_antinode_locations(a1, a2)
            if is_within_matrix(antinode)
        }
    )
)
