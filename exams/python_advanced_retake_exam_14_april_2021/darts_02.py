def is_inside(row, col):
    return 0 <= row < 6 and 0 <= col < 6


def throw(points, first_idx, second_idx, iterable):
    current_points = 0
    if is_inside(first_idx, second_idx):
        if iterable[first_idx][second_idx] == "B":
            current_points = points
            return current_points

        elif iterable[first_idx][second_idx] == "T":
            current_points += (int(iterable[0][second_idx]) + int(iterable[6][second_idx]) +
                               int(iterable[first_idx][0]) + int(iterable[first_idx][6])) * 3
            return current_points

        elif iterable[first_idx][second_idx] == "D":
            current_points += (int(iterable[0][second_idx]) + int(iterable[6][second_idx]) +
                               int(iterable[first_idx][0]) + int(iterable[first_idx][6])) * 2
            return current_points

        elif iterable[first_idx][second_idx].isdigit():
            current_points += int(iterable[first_idx][second_idx])
            return current_points
    else:
        return 0


size = 7
first_player, second_player = input().split(", ")
dartboard = [input().split() for _ in range(size)]
first_player_points = 501
second_player_points = 501
first_player_throw_count = 0
second_player_throw_count = 0

while True:
    first_player_row, first_player_col = input().strip("(").strip(")").split(", ")
    first_player_row = int(first_player_row)
    first_player_col = int(first_player_col)

    first_player_throw_count += 1
    first_player_throw_points = throw(first_player_points, first_player_row, first_player_col, dartboard)
    if first_player_points - first_player_throw_points <= 0:
        print(f"{first_player} won the game with {first_player_throw_count} throws!")
        break
    else:
        first_player_points -= first_player_throw_points

    second_player_row, second_player_col = input().strip("(").strip(")").split(", ")
    second_player_row = int(second_player_row)
    second_player_col = int(second_player_col)

    second_player_throw_count += 1
    second_player_throw_points = throw(second_player_points, second_player_row, second_player_col, dartboard)
    if second_player_points - second_player_throw_points <= 0:
        print(f"{second_player} won the game with {second_player_throw_count} throws!")
        break
    else:
        second_player_points -= second_player_throw_points
