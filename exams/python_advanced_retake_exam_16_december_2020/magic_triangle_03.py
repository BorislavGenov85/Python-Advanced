# def get_magic_triangle(num):
#
#     if num == 1:
#         return [[1]]
#     elif num == 2:
#         triangle = get_magic_triangle(num - 1)
#         prev_row = triangle[-1]
#         current_row = [1]
#         for i in range(1, len(prev_row)):
#             current_row.append(prev_row[i - 1] + prev_row[i])
#         current_row.append(1)
#         triangle.append(current_row)
#         return triangle
#
#     else:
#         get_magic_triangle(num - 1)
#
#
# get_magic_triangle(5)


def get_magic_triangle(num):
    triangle = [[1]]
    for i in range(1, num):
        prev_row = triangle[i - 1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle


