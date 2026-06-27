with open("input/2025-1") as file:
    moves = [line.strip() for line in file]

position = 50
total_point = 100
total_zeros = 0

for shift in moves:
    direction = shift[0]
    value = int(shift[1:])

    if direction == 'L':
        position -= value
    else: 
        position += value

    position %= total_point

    if position == 0:
        total_zeros += 1

print(f"total zeros: {total_zeros}")