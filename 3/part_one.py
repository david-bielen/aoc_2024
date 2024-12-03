import re
from functools import reduce

from input_data import input_string

print(
    sum(
        [
            reduce(
                lambda x, y: x * y,
                map(int, i.replace("mul(", "").replace(")", "").split(",")),
            )
            for i in re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_string)
        ]
    )
)
