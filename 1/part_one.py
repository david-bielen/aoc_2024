from input_data import input_string

print(
    sum(
        abs(x - y)
        for x, y in zip(
            *map(
                sorted,
                zip(*[map(int, x.split()) for x in input_string.strip().split("\n")]),
            )
        )
    )
)
