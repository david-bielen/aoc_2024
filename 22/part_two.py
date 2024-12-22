# /// script
# dependencies = []
# ///
from collections import defaultdict

from temp import input_string

data = list(map(int, input_string.strip().split()))


def compute_first_occurrences(init_value):
    result = {}
    diff_buffer = [0, 0, 0, 0]
    current_num = init_value
    old_last_digit = 0
    for i in range(2001):
        last_digit = current_num % 10
        diff = last_digit - old_last_digit
        old_last_digit = last_digit
        idx = i % 4
        diff_buffer[idx] = diff
        if i >= 3:
            pattern = (
                diff_buffer[idx],
                diff_buffer[(i - 1) % 4],
                diff_buffer[(i - 2) % 4],
                diff_buffer[(i - 3) % 4],
            )
            if pattern not in result:
                result[pattern] = last_digit
        if i < 2000:
            x = current_num
            x = ((x * 64) ^ x) % 16777216
            x = ((x >> 5) ^ x) % 16777216
            x = ((x * 2048) ^ x) % 16777216
            current_num = x

    return result


main_dict = defaultdict(int)
for value in data:
    first_occurrences = compute_first_occurrences(value)
    for pattern, last_digit in first_occurrences.items():
        main_dict[pattern] += last_digit
print(main_dict[max(main_dict, key=main_dict.get)])
