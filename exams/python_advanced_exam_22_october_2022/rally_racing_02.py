size = int(input())
car_race_num = input()
matrix = []
tunnel_pos = []
directions = {"up": [-1, 0],
              "down": [1, 0],
              "right": [0, 1],
              "left": [0, -1]
              }

car_row = 0
car_col = 0
distance_covered = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(len(data)):
        if data[col] == "T":
            tunnel_pos.append([row, col])

while True:
    direction = input()
    matrix[car_row][car_col] = "C"

    if direction == "End":
        print(f"Racing car {car_race_num} DNF.")
        break

    next_row, next_col = car_row + directions[direction][0], car_col + directions[direction][1]
    matrix[car_row][car_col] = "."

    if matrix[next_row][next_col] == ".":
        distance_covered += 10
        car_row = next_row
        car_col = next_col
        matrix[car_row][car_col] = "C"

    elif matrix[next_row][next_col] == "F":
        distance_covered += 10
        matrix[next_row][next_col] = "C"
        print(f"Racing car {car_race_num} finished the stage!")
        break

    else:
        distance_covered += 30
        matrix[next_row][next_col] = "."
        tunnel_pos.remove([next_row, next_col])
        car_row = tunnel_pos[0][0]
        car_col = tunnel_pos[0][1]
        matrix[car_row][car_col] = "C"
        tunnel_pos.clear()

print(f"Distance covered {distance_covered} km.")
[print("".join(x)) for x in matrix]
