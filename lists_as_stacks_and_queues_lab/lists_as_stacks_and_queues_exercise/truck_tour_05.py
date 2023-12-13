# first solution
from collections import deque

number = int(input())
pumps = deque()

for _ in range(number):
    pump_parts = [int(x) for x in input().split()]
    pumps.append(pump_parts)

for attend in range(number):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel

        if tank < distance:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attend)
        break

# second solution
# from collections import deque
#
# num = int(input())
# pumps = deque()
#
# for _ in range(num):
#     pumps.append([int(x) for x in input().split()])
#
# for attend in range(num):
#     tank = 0
#     failed = False
#     for fuel, distance in pumps:
#         tank += fuel
#
#         if tank < distance:
#             failed = True
#             break
#         else:
#             tank -= distance
#
#     if failed:
#         pumps.rotate(-1)
#     else:
#         print(attend)
#         break
