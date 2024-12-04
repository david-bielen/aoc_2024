from input_data import input_string

matrix = [list(line) for line in input_string.strip().split("\n")]

MATRIX_SIZE = len(matrix)
PATTERNS = {
    ("X", "M", "A", "S"),
    ("S", "A", "M", "X"),
}
OFF_SET = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (1, -1), (2, -2), (3, -3)],
]


def get_pattern(x, y, offsets):
    return [
        matrix[x + dx][y + dy]
        if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0])
        else None
        for dx, dy in offsets
    ]


print(
    sum(
        1
        for x in range(len(matrix))
        for y in range(len(matrix))
        for off_set in OFF_SET
        if tuple(get_pattern(x, y, off_set)) in PATTERNS
    )
)
