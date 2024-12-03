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
            for i in re.findall(
                r"mul\(\d{1,3},\d{1,3}\)",
                re.sub(
                    r"don't\(\).*",
                    "",
                    re.sub(r"don't\(\).*?do\(\)", "", input_string, flags=re.DOTALL),
                    flags=re.DOTALL,
                ),
            )
        ]
    )
)
