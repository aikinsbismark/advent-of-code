with open("./input/2025-02", "r") as file:
    content = file.read().strip().split(",")

def filter_invalid_ids(content):
    invalid_numbers = []

    for id_ranges in content:
        strip_range = id_ranges.split("-")
        start, end = int(strip_range[0]), int(strip_range[1])

        for number in range(start, end+1):
            number_str = str(number)

            n = len(number_str)
            is_match = False
            for chunk_len in range(1, n // 2 + 1):
                if n % chunk_len == 0:
                    if number_str[:chunk_len] * (n // chunk_len) == number_str:
                        is_match = True
                        break
            if is_match:
                invalid_numbers.append(number)
    return invalid_numbers, sum(invalid_numbers)
invalid_ids, total = filter_invalid_ids(content)
print(f"total: {total}")
            