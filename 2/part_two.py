from input_data import input_string

print(
    sum(
        1
        for b in [
            [int(nr) for nr in line.split()]
            for line in input_string.strip().split("\n")
        ]
        if any(
            (
                lambda deltas: all(delta in (-3, -2, -1) for delta in deltas)
                or all(delta in (1, 2, 3) for delta in deltas)
            )([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])
            for seq in [b] + [b[:i] + b[i + 1 :] for i in range(len(b))]
        )
    )
)

print(
    sum(
        any(
            all(d in (-3, -2, -1) for d in deltas)
            or all(d in (1, 2, 3) for d in deltas)
            for deltas in (
                [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
                for seq in [b] + [b[:i] + b[i + 1 :] for i in range(len(b))]
            )
        )
        for b in (
            [int(nr) for nr in line.split()]
            for line in input_string.strip().split("\n")
        )
    )
)
