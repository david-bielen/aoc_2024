from input_data import input_string


def parse_value(segment: str) -> int:
    return int(segment.split("+")[1]) if "+" in segment else int(segment.split("=")[1])


parsed_input = [
    [
        (parse_value(parts[0]), parse_value(parts[1]))
        for parts in [line.split(": ")[1].split(", ")]
    ]
    for line in input_string.split("\n")
    if line.strip()
]

cost = 0
for e in parsed_input:
    a = ((e[1][1] * e[2][0]) - (e[1][0] * e[2][1])) / (
        (e[1][1] * e[0][0]) - e[0][1] * e[1][0]
    )
    b = (e[2][0] - (a * e[0][0])) / e[1][0]
    if a.is_integer() and b.is_integer():
        cost += a * 3 + b
print(int(cost))
