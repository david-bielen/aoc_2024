from input_data import input_string

width = 101
height = 103

robots = [
    (tuple(map(int, p[2:].split(","))), tuple(map(int, v[2:].split(","))))
    for p, v in (line.split() for line in input_string.splitlines())
]


def calculate_next_position(p, v, r):
    global width, height
    for _ in range(r):
        next_x = (p[0] + v[0]) % width
        next_y = (p[1] + v[1]) % height
        p = (next_x, next_y)
    return p


def get_kwadrant(position):
    global width, height
    x, y = position
    if x < width // 2 and y < height // 2:
        return 1
    if x > width // 2 and y < height // 2:
        return 2
    if x < width // 2 and y > height // 2:
        return 3
    if x > width // 2 and y > height // 2:
        return 4
    return "."


new_positions = [calculate_next_position(*robot, 100) for robot in robots]
kwadrants = [get_kwadrant(position) for position in new_positions]

print(kwadrants.count(1) * kwadrants.count(2) * kwadrants.count(3) * kwadrants.count(4))
