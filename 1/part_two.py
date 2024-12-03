from input_data import input_string

print(
    sum(
        a * [b for _, b in data].count(a)
        for data in [
            [list(map(int, x.split())) for x in input_string.strip().split("\n")]
        ]
        for a, _ in data
    )
)
