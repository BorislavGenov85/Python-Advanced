from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups = deque([int(x) for x in input().split(", ")])

milkshake_count = 0

while milkshake_count < 5 and chocolates and cups:
    chocolate = chocolates.pop()
    milk_cup = cups.popleft()
    # ?
    if chocolate <= 0 and milk_cup <= 0:
        continue

    if chocolate <= 0:
        cups.appendleft(milk_cup)
        continue

    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshake_count += 1

    else:
        chocolates.append(chocolate - 5)
        cups.append(milk_cup)

if milkshake_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join([str(x) for x in cups])}")
else:
    print("Milk: empty")
