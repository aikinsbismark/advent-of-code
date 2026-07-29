with open("./input/2025-02", "r") as file: 
    content = file.read().strip().split(",")

def filter_invalid_ids(content):
    invalid_numbers = []
    
    for id_ranges in content:
        strip_range = id_ranges.split("-")
        start, end = int(strip_range[0]), int(strip_range[1])

        for number in range(start, end+1):
            number_str = str(number)

            if len(number_str) % 2 != 0:
                continue

            first_half = number_str[:len(number_str)//2]
            second_half = number_str[len(number_str)//2:]

            if first_half == second_half:
                invalid_numbers.append(number)

    return invalid_numbers, sum(invalid_numbers)
invalid_ids, total = filter_invalid_ids(content)
   
print(f"total: {total}")