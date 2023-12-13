from collections import deque

quantity = int(input())
people = deque()

while True:
    data = input()
    if data == "Start":
        break
    else:
        people.append(data)

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    if len(command) == 1:
        liters = int(command[0])
        person_name = people.popleft()
        if quantity >= liters:
            print(f"{person_name} got water")
            quantity -= liters
        else:
            print(f"{person_name} must wait")
    else:
        liters = int(command[1])
        quantity += liters

print(f"{quantity} liters left")

# second solution

# from collections import deque
#
# water = int(input())
#
# names = deque()
#
# while True:
#     data = input()
#
#     if data == "Start":
#         break
#     else:
#         names.append(data)
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     command = command.split()
#
#     if len(command) == 1:
#         litters = int(command[0])
#         person = names.popleft()
#
#         if water >= litters:
#             water -= litters
#             print(f"{person} got water")
#         else:
#             print(f"{person} must wait")
#
#     else:
#         litters = int(command[1])
#         water += litters
#
# print(f"{water} liters left")
