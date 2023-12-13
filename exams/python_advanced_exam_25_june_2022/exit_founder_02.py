first_player, second_player = input().split(", ")
board = [input().split() for row in range(6)]
first_player_rest = False
second_player_rest = False

while True:
    first_player_cords = input()

    row, col = int(first_player_cords[1]), int(first_player_cords[4])

    if not first_player_rest:
        if board[row][col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break

        elif board[row][col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break

        elif board[row][col] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_rest = True

    else:
        first_player_rest = False

    second_player_cords = input()

    row, col = int(second_player_cords[1]), int(second_player_cords[4])

    if not second_player_rest:
        if board[row][col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break

        elif board[row][col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break

        elif board[row][col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_rest = True

    else:
        second_player_rest = False
