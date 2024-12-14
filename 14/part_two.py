# /// script
# dependencies = [
#   "numpy",
# ]
# ///

# we assume that the matrix with the highest compressibility
# is the one containing the pattern of a xmas tree.

import numpy as np
from input_data import input_string

width, height = 101, 103

robots = np.array(
    [
        (tuple(map(int, p[2:].split(","))), tuple(map(int, v[2:].split(","))))
        for p, v in (line.split() for line in input_string.splitlines())
    ]
)

positions = np.array([p for p, _ in robots])
velocities = np.array([v for _, v in robots])
dimensions = np.array([width, height])


def calculate_next_positions(positions, velocities, r):
    return (positions + r * velocities) % dimensions


def calc_entropy(grid):
    counts = np.bincount(grid.ravel())
    probs = counts[counts > 0] / counts.sum()
    return -np.sum(probs * np.log2(probs))


entropy = 666
elapsed_seconds = None

for r in range(0, 6600):
    updated_positions = calculate_next_positions(positions, velocities, r)
    grid = np.zeros((height, width), dtype=int)
    np.add.at(grid, (updated_positions[:, 1], updated_positions[:, 0]), 1)
    current_entropy = calc_entropy(grid)
    if current_entropy < entropy:
        entropy = current_entropy
        elapsed_seconds = r

print(elapsed_seconds)
