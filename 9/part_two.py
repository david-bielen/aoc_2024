from input_data import input_string


def parse_disk_map(disk_map: str) -> str:
    result = []
    file_id = 0

    for i, length in enumerate(map(int, disk_map)):
        if i % 2 == 0:
            result.extend([str(file_id)] * length)
            file_id += 1
        else:
            result.extend(["."] * length)
    return result


def calculate_similars_right(disk: list, index: int) -> int:
    similars = 0
    for i in range(index + 1, len(disk)):
        if disk[i] == disk[index]:
            similars += 1
        else:
            break
    return similars + 1


def calculate_similars_left(disk: list, index: int) -> int:
    similars = 0
    for i in range(index - 1, -1, -1):
        if disk[i] == disk[index]:
            similars += 1
        else:
            break
    return similars + 1


def compact_disk(disk: list) -> str:
    leftmost_free = 0
    disregard = set(".")
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] not in disregard:
            leftmost_free = len(disk) + 1
            for k in range(len(disk)):
                if disk[k] == "." and calculate_similars_right(
                    disk, k
                ) >= calculate_similars_left(disk, i):
                    length_of_similars = calculate_similars_left(disk, i)
                    char = disk[i]
                    leftmost_free = k
                    break
            if leftmost_free < i:
                for length in range(length_of_similars):
                    disk[leftmost_free + length] = char
                    disk[i - length] = "."
        disregard.add(disk[i])
    return disk


def calculate_checksum(disk: list) -> int:
    checksum = 0
    for position, char in enumerate(disk):
        if char == ".":
            pass
        else:
            checksum += int(char) * position
    return checksum


print(calculate_checksum(compact_disk(parse_disk_map(input_string))))
