queue = []
data = input()
while data != "End":

    if data == "Paid":
        print("\n".join(queue))
        queue.clear()
    else:
        queue.append(data)

    data = input()
print(f"{len(queue)} people remaining.")

# second solution

# from collections import deque
#
# names = deque()
#
# while True:
#     data = input()
#
#     if data == "End":
#         break
#
#     if data == "Paid":
#         while names:
#             name = names.popleft()
#             print(name)
#
#     else:
#         names.append(data)
#
# print(f"{len(names)} people remaining.")
