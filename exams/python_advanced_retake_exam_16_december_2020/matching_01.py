from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue

    if female <= 0:
        females.popleft()
        continue

    if male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if male == female:
        matches += 1
        males.pop()
        females.popleft()

    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(x) for x in females])}")
