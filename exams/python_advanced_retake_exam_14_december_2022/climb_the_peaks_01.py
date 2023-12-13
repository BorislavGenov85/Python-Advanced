from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])
mountain_peaks = deque([
    ["Vihren", 80],
    ["Kutelo", 90],
    ["Banski Suhodol", 100],
    ["Polezhan", 60],
    ["Kamenitza", 70]
])
conquered_peaks = []
win = False

while food_portions and stamina:
    food = food_portions.pop()
    current_stamina = stamina.popleft()
    result = food + current_stamina

    peak_info = mountain_peaks.popleft()
    peak_name = peak_info[0]
    peak_difficult = int(peak_info[1])

    if result >= peak_difficult:
        conquered_peaks.append(peak_name)
    else:
        mountain_peaks.appendleft(peak_info)

    if not mountain_peaks:
        win = True
        break

if win:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    for name in conquered_peaks:
        print(f"{name}")
        
