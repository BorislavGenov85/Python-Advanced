from collections import deque

seats = input().split(", ")
first_lst = deque([int(x) for x in input().split(", ")])
second_lst = deque([int(x) for x in input().split(", ")])
taken_seat = []
matched_seats = 0
rotation = 0

while rotation < 10 and matched_seats < 3:
    rotation += 1
    first_num = first_lst.popleft()
    second_num = second_lst.pop()
    result = chr(first_num + second_num)

    if f"{first_num}{result}" in seats and f"{first_num}{result}" not in taken_seat:
        matched_seats += 1
        taken_seat.append(f"{first_num}{result}")
        continue
    if f"{second_num}{result}" in seats and f"{second_num}{result}" not in taken_seat:
        matched_seats += 1
        taken_seat.append(f"{second_num}{result}")
        continue

    first_lst.append(first_num)
    second_lst.appendleft(second_num)

print(f"Seat matches: {', '.join(taken_seat)}")
print(f"Rotations count: {rotation}")
