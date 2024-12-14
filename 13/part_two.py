from input_data import input_string

parsed_input = []
current_group = []


def parse_value(segment: str) -> int:
    return int(segment.split("+")[1]) if "+" in segment else int(segment.split("=")[1])


for line in input_string.split("\n") + [""]:
    if line.strip():
        parts = line.split(": ")[1].split(", ")
        current_group.append((parse_value(parts[0]), parse_value(parts[1])))
    elif current_group:
        parsed_input.append(current_group)
        current_group = []


updated_parsed_input = [
    inner_list[:2]
    + [(inner_list[2][0] + 10000000000000, inner_list[2][1] + 10000000000000)]
    for inner_list in parsed_input
]

cost = 0
for e in updated_parsed_input:
    a = ((e[1][1] * e[2][0]) - (e[1][0] * e[2][1])) / (
        (e[1][1] * e[0][0]) - e[0][1] * e[1][0]
    )
    b = (e[2][0] - (a * e[0][0])) / e[1][0]
    if a.is_integer() and b.is_integer():
        cost += a * 3 + b
print(int(cost))
