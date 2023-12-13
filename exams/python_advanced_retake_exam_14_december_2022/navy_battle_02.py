def move(idx1, idx2, iterable, cruiser, mine):
    if iterable[idx1][idx2] == "C":
        battlefield[idx1][idx2] = "S"
        cruiser += 1
        return idx1, idx2, iterable, cruiser, mine

    elif iterable[idx1][idx2] == "*":
        battlefield[idx1][idx2] = "S"
        mine += 1
        return idx1, idx2, iterable, cruiser, mine

    else:
        iterable[idx1][idx2] = "S"
        return idx1, idx2, iterable, cruiser, mine


size = int(input())

destroyed_cruiser = 0
mine_blows = 0
battlefield = []
submarine_row, submarine_col = 0, 0
for row in range(size):
    line = list(input())
    battlefield.append(line)
    for col in range(len(line)):
        el = battlefield[row][col]

        if el == "S":
            submarine_row, submarine_col = row, col

mine_fail = False
while destroyed_cruiser < 3:
    direction = input()
    battlefield[submarine_row][submarine_col] = "-"

    if direction == "up":
        submarine_row, submarine_col, battlefield, destroyed_cruiser, mine_blows = \
            move(submarine_row - 1, submarine_col, battlefield, destroyed_cruiser, mine_blows)

    elif direction == "down":
        submarine_row, submarine_col, battlefield, destroyed_cruiser, mine_blows = \
            move(submarine_row + 1, submarine_col, battlefield, destroyed_cruiser, mine_blows)

    elif direction == "left":
        submarine_row, submarine_col, battlefield, destroyed_cruiser, mine_blows = \
            move(submarine_row, submarine_col - 1, battlefield, destroyed_cruiser, mine_blows)

    else:
        submarine_row, submarine_col, battlefield, destroyed_cruiser, mine_blows = \
            move(submarine_row, submarine_col + 1, battlefield, destroyed_cruiser, mine_blows)

    if mine_blows == 3:
        mine_fail = True
        break

if destroyed_cruiser == 3:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
if mine_fail:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
[print(''.join(row))for row in battlefield]
