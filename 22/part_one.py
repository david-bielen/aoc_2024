# /// script
# dependencies = []
# ///
from temp import input_string

data = list(map(int, input_string.strip().split()))


def calculate_secret(secret_number):
    for _ in range(2000):
        secret_number = ((secret_number * 64) ^ secret_number) % 16777216
        secret_number = ((secret_number >> 5) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
    return secret_number


print(sum(calculate_secret(x) for x in data))
