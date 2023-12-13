from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament = [int(x) for x in input().split()]
items = {
        30: "Patch",
        40: "Bandage",
        100: "MedKit"
         }
created_items = {
        "Patch": 0,
        "Bandage": 0,
        "MedKit": 0
}

while textiles and medicament:
    current_textile = textiles.popleft()
    current_medicament = medicament.pop()

    result = current_textile + current_medicament
    if result in items:
        created_items[items[result]] += 1

    elif result > 100:
        remaining = result - 100
        medicament[-1] += remaining
        created_items["MedKit"] += 1
    else:
        current_medicament += 10
        medicament.append(current_medicament)

sorted_created_items = {k: v for k, v in created_items.items() if v != 0}

if not textiles and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")
if sorted_created_items:
    sorted_created_items = sorted(sorted_created_items.items(), key=lambda x: (-x[1], x[0]))
    for item in sorted_created_items:
        print(f"{item[0]} - {item[1]}")
if medicament:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medicament)])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
