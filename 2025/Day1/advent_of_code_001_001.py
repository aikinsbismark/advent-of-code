with open("input/2025-1") as file:
    rotations = [line.strip() for line in file]

dial_position = 50
total_zeros = 0

for rotation in rotations:
    direction, distance = rotation[0], int(rotation[1:])

    if direction == "L":
        dial_position -= distance       
    else: 
        dial_position += distance

    dial_position %= 100

    if dial_position == 0:
        total_zeros += 1

print(f"total zeros: {total_zeros}")