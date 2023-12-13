from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_time_to_str(seconds):
    seconds %= 24 * 60 * 60

    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


data = input().split(";")
time = convert_str_to_seconds(input())
robots = {}
robots_busy_to_time = {}
items = deque()

for item in data:
    name, process_time = item.split("-")
    robots[name] = int(process_time)
    robots_busy_to_time[name] = -1

while True:
    line = input()
    if line == "End":
        break
    items.append(line)

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in robots_busy_to_time.items():
        if time >= busy_until:
            robots_busy_to_time[name] = time + robots[name]
            print(f"{name} - {item} [{convert_time_to_str(time)}]")
            break

    else:
        items.append(item)
