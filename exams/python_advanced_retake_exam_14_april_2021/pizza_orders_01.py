from collections import deque

pizzas = deque([int(x) for x in input().split(", ") if 0 < int(x) <= 10])
employees = [int(x) for x in input().split(", ")]
total_pizzas = 0

while pizzas and employees:
    pizza = pizzas[0]
    employer = employees[-1]

    if pizza <= employer:
        pizzas.popleft()
        employees.pop()
        total_pizzas += pizza
    else:
        pizzas[0] -= employer
        employees.pop()
        total_pizzas += employer

if not pizzas:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizzas])}")

