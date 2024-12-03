from input_data import input_string

print(
    sum(
        1
        for a in [
            [int(nr) for nr in line.split()]
            for line in input_string.strip().split("\n")
        ]
        if (deltas := [a[i + 1] - a[i] for i in range(len(a) - 1)])
        and (
            all(delta in (-3, -2, -1) for delta in deltas)
            or all(delta in (1, 2, 3) for delta in deltas)
        )
    )
)
