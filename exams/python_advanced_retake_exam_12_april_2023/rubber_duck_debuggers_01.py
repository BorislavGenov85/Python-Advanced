from collections import deque

time = deque(int(x) for x in input().split())
tasks = [int(x) for x in input().split()]
time_needed = {
        60: "Darth Vader Ducky",
        120: "Thor Ducky",
        180: "Big Blue Rubber Ducky",
        240: "Small Yellow Rubber Ducky"
}
given_ducky = {
        "Darth Vader Ducky": 0,
        "Thor Ducky": 0,
        "Big Blue Rubber Ducky": 0,
        "Small Yellow Rubber Ducky": 0
}

while time and tasks:
    current_time = time.popleft()
    current_task = tasks.pop()
    result = current_time * current_task

    for key, value in time_needed.items():
        if result <= key:
            given_ducky[value] += 1
            break
    else:
        current_task -= 2
        tasks.append(current_task)
        time.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in given_ducky.items():
    print(f"{key}: {value}")
