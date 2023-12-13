from collections import deque

caffeine = [int(x) for x in input().split(", ")]
drinks = deque([int(x) for x in input().split(", ")])
max_caffeine = 300
person_caffeine = 0

while caffeine and drinks:
    current_caffeine = caffeine.pop()
    current_drink = drinks.popleft()
    result = current_caffeine * current_drink

    if person_caffeine + result <= max_caffeine:
        person_caffeine += result
    else:
        drinks.append(current_drink)
        if person_caffeine >= 30:
            person_caffeine -= 30
        else:
            person_caffeine = 0

if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {person_caffeine} mg caffeine.")
