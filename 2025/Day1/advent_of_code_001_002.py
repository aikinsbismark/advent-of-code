with open("input/2025-1") as file:
    rotations = [line.strip() for line in file]

dial_position = 50
zero_passes = 0

for rotation in rotations:
    direction, distance = rotation[0], int(rotation[1:])

    zero_passes += distance // 100

    remaining_distance = distance % 100

    if direction == "L":
        zero_passes += remaining_distance >= dial_position and dial_position > 0
        dial_position = (dial_position - remaining_distance) % 100
    else:
        zero_passes += (dial_position + remaining_distance) >= 100
        dial_position = (dial_position + remaining_distance) % 100

print(zero_passes)



