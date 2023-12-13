# first solution

from collections import deque

children_names = deque(input().split())
number = int(input())
counter = 1
while len(children_names) != 1:
    if counter == number:
        kid = children_names.popleft()
        print(f"Removed {kid}")
        counter = 0
    else:
        kid = children_names.popleft()
        children_names.append(kid)

    counter += 1

print(f"Last is {children_names[0]}")


# second solution

# from collections import deque
#
# children = deque(input().split())
# num = int(input())
#
# counter = 1
# while len(children) != 1:
#
#     if counter == num:
#         name = children.popleft()
#         counter = 1
#         print(f"Removed {name}")
#     else:
#         children.rotate(-1)
#         counter += 1
#
# print(f"Last is {children[0]}")
