from itertools import combinations
from math import gcd

from input_data import input_string

rows = input_string.splitlines()
matrix_dict = {(r, c): char for r, row in enumerate(rows) for c, char in enumerate(row)}
total_rows, total_columns = len(rows), len(rows[0])
unique_chars = {char for char in input_string if char not in {".", "\n"}}


def is_within_matrix(point):
    r, c = point
    return 0 <= r < total_rows and 0 <= c < total_columns


def find_line_points(a, b):
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    g = gcd(dx, dy)
    sx, sy = dx // g, dy // g
    s = set()
    for d in (1, -1):
        x, y = (x2, y2) if d == 1 else (x1, y1)
        while is_within_matrix((x, y)):
            s.add((x, y))
            x += d * sx
            y += d * sy
    return sorted(s)


print(
    len(
        {
            antinode
            for char in unique_chars
            for antenna_1, antenna_2 in combinations(
                [key for key, value in matrix_dict.items() if value == char], 2
            )
            for antinode in find_line_points(antenna_1, antenna_2)
        }
    )
)
