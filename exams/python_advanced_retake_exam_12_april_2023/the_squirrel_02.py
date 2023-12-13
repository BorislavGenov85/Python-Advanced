def is_valid_position(idx_1, idx_2, size):
    if 0 <= idx_1 < size and 0 <= idx_2 < size:
        return True
    return False


size = int(input())
directions = input().split(", ")
field = []
move = {"up": [-1, 0],
        "down": [1, 0],
        "right": [0, 1],
        "left": [0, -1]
        }

squirrel_row = 0
squirrel_col = 0
collected_hazelnuts = 0
out_of_field = False
is_trapped = False

for row in range(size):
    line = list(input())
    field.append(line)
    for i in range(len(line)):
        if line[i] == "s":
            squirrel_row = row
            squirrel_col = i
            field[squirrel_row][squirrel_col] = "*"

for direction in directions:

    if direction in move:
        if is_valid_position(squirrel_row + move[direction][0], squirrel_col + move[direction][1], size):
            next_row, next_col = squirrel_row + move[direction][0], squirrel_col + move[direction][1]
            squirrel_row, squirrel_col = next_row, next_col
        else:
            out_of_field = True
            break

    if field[squirrel_row][squirrel_col] == "h":
        collected_hazelnuts += 1
        field[squirrel_row][squirrel_col] = "*"

    elif field[squirrel_row][squirrel_col] == "t":
        is_trapped = True
        break

    if collected_hazelnuts == 3:
        break

if out_of_field:
    print("The squirrel is out of the field.")
if is_trapped:
    print("Unfortunately, the squirrel stepped on a trap...")
if collected_hazelnuts < 3 and not out_of_field and not is_trapped:
    print("There are more hazelnuts to collect.")
elif collected_hazelnuts == 3 and not out_of_field and not is_trapped:
    print("Good job! You have collected all hazelnuts!")
print(f"Hazelnuts collected: {collected_hazelnuts}")
