def fill_the_box(height, length, width, *cubs):
    capacity = height * length * width

    total_cub = 0
    for cub in cubs:
        if cub == "Finish":
            break
        total_cub += cub

    if capacity > total_cub:
        return f"There is free space in the box. You could put {capacity - total_cub} more cubes."
    else:
        return f"No more free space! You have {abs(capacity - total_cub)} more cubes."


print(fill_the_box(2, 8,
                   2, 2, 1, 7, 3, 1, 5,
                   "Finish"
                   ))
