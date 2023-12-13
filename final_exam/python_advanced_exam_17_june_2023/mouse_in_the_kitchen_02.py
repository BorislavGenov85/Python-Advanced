def move(m_row, m_col, iterable, cheese, trap, path):
    if iterable[m_row][m_col] == "C":
        iterable[m_row][m_col] = "M"
        cheese += 1
        return m_row, m_col, iterable, cheese, trap, path

    elif iterable[m_row][m_col] == "@":
        if path == "up":
            return m_row + 1, m_col, iterable, cheese, trap, path
        elif path == "down":
            return m_row - 1, m_col, iterable, cheese, trap, path
        elif path == "right":
            return m_row, m_col - 1, iterable, cheese, trap, path
        else:
            return m_row, m_col + 1, iterable, cheese, trap, path

    elif iterable[m_row][m_col] == "*":
        iterable[m_row][m_col] = "M"
        return m_row, m_col, iterable, cheese, trap, path

    elif iterable[m_row][m_col] == "T":
        iterable[m_row][m_col] = "M"
        trap = True
        return m_row, m_col, iterable, cheese, trap, path


def is_inside_board(mouse_idx1, mouse_idx2, idx1, idx2):
    return 0 <= mouse_idx1 < idx1 and 0 <= mouse_idx2 < idx2


rows, cols = [int(el) for el in input().split(",")]
mouse_row, mouse_col = 0, 0
field = []
cheeses = []

for row in range(rows):
    line = list(input())
    field.append(line)
    for col in range(len(line)):
        el = line[col]

        if el == "M":
            mouse_row, mouse_col = row, col
        elif el == "C":
            cheeses.append([row, col])

eaten_cheese = 0
trapped = False
while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        break

    if direction == "up":
        if is_inside_board(mouse_row - 1, mouse_col, rows, cols):
            mouse_next_row, mouse_next_col, field, eaten_cheese, trapped, direction = \
                move(mouse_row - 1, mouse_col, field, eaten_cheese, trapped, direction)
            if mouse_row != mouse_next_row or mouse_col != mouse_next_col:
                field[mouse_row][mouse_col] = "*"
            mouse_row, mouse_col = mouse_next_row, mouse_next_col
        else:
            print("No more cheese for tonight!")
            break

    elif direction == "down":
        if is_inside_board(mouse_row + 1, mouse_col, rows, cols):
            mouse_next_row, mouse_next_col, field, eaten_cheese, trapped, direction = \
                move(mouse_row + 1, mouse_col, field, eaten_cheese, trapped, direction)
            if mouse_row != mouse_next_row or mouse_col != mouse_next_col:
                field[mouse_row][mouse_col] = "*"
            mouse_row, mouse_col = mouse_next_row, mouse_next_col
        else:
            print("No more cheese for tonight!")
            break

    elif direction == "right":
        if is_inside_board(mouse_row, mouse_col + 1, rows, cols):
            mouse_next_row, mouse_next_col, field, eaten_cheese, trapped, direction = \
                move(mouse_row, mouse_col + 1, field, eaten_cheese, trapped, direction)
            if mouse_row != mouse_next_row or mouse_col != mouse_next_col:
                field[mouse_row][mouse_col] = "*"
            mouse_row, mouse_col = mouse_next_row, mouse_next_col
        else:
            print("No more cheese for tonight!")
            break

    elif direction == "left":
        if is_inside_board(mouse_row, mouse_col - 1, rows, cols):
            mouse_next_row, mouse_next_col, field, eaten_cheese, trapped, direction = \
                move(mouse_row, mouse_col - 1, field, eaten_cheese, trapped, direction)
            if mouse_row != mouse_next_row or mouse_col != mouse_next_col:
                field[mouse_row][mouse_col] = "*"
            mouse_row, mouse_col = mouse_next_row, mouse_next_col
        else:
            print("No more cheese for tonight!")
            break

    if trapped:
        print("Mouse is trapped!")
        break

    if eaten_cheese == len(cheeses):
        print("Happy mouse! All the cheese is eaten, good night!")
        break

[print(''.join(row)) for row in field]
