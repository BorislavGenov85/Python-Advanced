def sum_colon_points(matrix, idx):
    points = 0

    for current_row in range(SIZE):
        el = int(matrix[current_row][idx])
        points += el
    return points


SIZE = 6
matrix = [input().split() for _ in range(SIZE)]

total_points = 0

for _ in range(3):
    row, col = input().strip("(").strip(")").split(", ")
    row = int(row)
    col = int(col)

    if 0 <= row < SIZE and 0 <= col < SIZE:
        if matrix[row][col] == "B":
            matrix[row][col] = 0
            total_points += sum_colon_points(matrix, col)

if total_points < 100:
    print(f"Sorry! You need {100 - total_points:.0f} points more to win a prize.")

elif total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")

elif total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")

else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
