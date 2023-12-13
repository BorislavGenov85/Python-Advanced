from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = [int(x) for x in input().split()]
wasted_litters_of_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity[0]
    current_bottle = bottles_capacity[-1]

    if current_cup > current_bottle:
        bottles_capacity.pop()
        cups_capacity[0] -= current_bottle

    else:
        wasted_litters_of_water += current_bottle - current_cup
        cups_capacity.popleft()
        bottles_capacity.pop()

if not cups_capacity:
    bottles_capacity = [str(x) for x in bottles_capacity]
    print(f"Bottles: {' '.join(bottles_capacity)}")
if not bottles_capacity:
    cups_capacity = [str(x) for x in cups_capacity]
    print(f"Cups: {' '.join(cups_capacity)}")
print(f"Wasted litters of water: {wasted_litters_of_water}")
