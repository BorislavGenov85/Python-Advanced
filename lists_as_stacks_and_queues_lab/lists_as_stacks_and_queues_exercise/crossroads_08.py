from collections import deque

green_light_duration = int(input())
free_window = int(input())
cars = deque()
time_to_passed = green_light_duration

passed_safely = 0
flag = False
car = ""
ch_hit = ""
while True:
    line = input()
    if line == "END":
        break

    if line == "green":
        while time_to_passed > 0 and cars:
            car = cars.popleft()
            if len(car) <= time_to_passed:
                time_to_passed -= len(car)
                passed_safely += 1
            elif len(car) <= time_to_passed + free_window:
                time_to_passed = 0
                passed_safely += 1
            else:
                ch_hit = car[time_to_passed + free_window]
                flag = True
                break

        else:
            time_to_passed = green_light_duration

        if flag:
            break
    else:
        cars.append(line)

if flag:
    print("A crash happened!")
    print(f"{car} was hit at {ch_hit}.")
else:
    print("Everyone is safe.")
    print(f"{passed_safely} total cars passed the crossroads.")
