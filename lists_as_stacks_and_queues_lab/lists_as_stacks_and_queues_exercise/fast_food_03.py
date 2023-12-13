# first solution
from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split()])
max_order = max(orders)

while True:
    if not orders:
        break
    current_order = orders[0]
    if quantity >= current_order:
        quantity -= current_order
        orders.popleft()

    else:
        break

print(max_order)
if orders:
    orders = [str(x) for x in orders]
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")

# second solution

# from collections import deque
#
# food_quantity = int(input())
# orders = deque(int(x) for x in input().split())
#
# print(max(orders))
#
# while orders:
#     current_order = orders[0]
#
#     if food_quantity - current_order >= 0:
#         orders.popleft()
#         food_quantity -= current_order
#     else:
#         break
#
# if not orders:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join([str(x) for x in orders])}")
