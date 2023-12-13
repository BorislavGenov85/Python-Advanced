rows, cols = [int(x) for x in input().split()]
snake = input()

idx = 0

for row in range(rows):
    sub_lst = []
    for col in range(cols):
        sub_lst.append(snake[idx % len(snake)])
        idx += 1
    if row % 2 == 0:
        print(*sub_lst, sep="")
    else:
        print(*reversed(sub_lst), sep="")

# second solution

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
# data = list(input())
#
# data_copy = deque(data)
#
# for row in range(rows):
#     while len(data_copy) < cols:
#         data_copy.extend(data)
#
#     if row % 2 == 0:
#         print(*[data_copy.popleft() for _ in range(cols)], sep="")
#     else:
#         print(*[data_copy.popleft() for _ in range(cols)][::-1], sep="")
