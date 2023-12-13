def move(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


rows, cols = [int(x) for x in input().split()]
playground = []
player_row = 0
player_col = 0

for row in range(rows):
    current_row = input().split()
    playground.append(current_row)
    for col in range(len(current_row)):
        if current_row[col] == "B":
            player_row = row
            player_col = col
            playground[row][col] = "-"

possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}
move_count = 0
touched_opponents = 0

while True:
    command = input()

    if command == "Finish":
        break

    if not move(player_row + possible_moves[command][0], player_col + possible_moves[command][1], rows, cols):
        continue

    if playground[player_row + possible_moves[command][0]][player_col + possible_moves[command][1]] == "O":
        continue

    if playground[player_row + possible_moves[command][0]][player_col + possible_moves[command][1]] == "-":
        move_count += 1
        player_row = player_row + possible_moves[command][0]
        player_col = player_col + possible_moves[command][1]
    elif playground[player_row + possible_moves[command][0]][player_col + possible_moves[command][1]] == "P":
        move_count += 1
        touched_opponents += 1
        player_row = player_row + possible_moves[command][0]
        player_col = player_col + possible_moves[command][1]
        playground[player_row][player_col] = "-"

    if touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {move_count}")
