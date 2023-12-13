from collections import deque


def calculate_honey(insect, syrup, sign):
    result = 0
    if sign == "+":
        result += abs(insect + syrup)
    elif sign == "-":
        result += abs(insect - syrup)
    elif sign == "*":
        result += abs(insect * syrup)
    elif sign == "/" and current_nectar > 0:
        result += abs(insect / syrup)

    return result


working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())

total_honey = 0

while working_bees and nectar:
    bee = working_bees[0]
    current_nectar = nectar.pop()

    if bee > current_nectar:
        continue

    bee = working_bees.popleft()
    current_symbol = symbols.popleft()
    honey = calculate_honey(bee, current_nectar, current_symbol)
    total_honey += honey

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
