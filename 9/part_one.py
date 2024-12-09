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


def compact_disk(disk: list) -> str:
    leftmost_free = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            leftmost_free = i
            break
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != ".":
            if leftmost_free < i:
                disk[leftmost_free], disk[i] = disk[i], "."
                for j in range(leftmost_free + 1, len(disk)):
                    if disk[j] == ".":
                        leftmost_free = j
                        break
    return disk


def calculate_checksum(disk: list) -> int:
    checksum = 0
    for position, char in enumerate(disk):
        if char == ".":
            break
        else:
            checksum += int(char) * position
    return checksum


print(calculate_checksum(compact_disk(parse_disk_map(input_string))))
