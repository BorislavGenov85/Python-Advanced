from collections import deque


def best_list_pureness(*args):
    lst = deque(args[0])
    num = args[1]
    best_rotation = 0
    best_result = 0
    for rotation in range(num + 1):

        current_res = 0
        for i in range(len(lst)):
            current_num = lst[i]
            current_res += current_num * i

        if current_res > best_result:
            best_result = current_res
            best_rotation = rotation

        number = lst.pop()
        lst.appendleft(number)

    return f"Best pureness {best_result} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
