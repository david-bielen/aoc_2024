from input_data import input_string


def convert_string_to_dict(s):
    return [
        sum(r[i] == "#" for r in s.split("\n")) for i in range(len(s.split("\n")[0]))
    ]


locks = [convert_string_to_dict(i) for i in input_string.split("\n\n") if i[0] == "#"]
keys = [convert_string_to_dict(i) for i in input_string.split("\n\n") if i[0] != "#"]
print(
    sum(
        all(key[i] + lock[i] <= 7 for i in range(len(key)))
        for key in keys
        for lock in locks
    )
)
