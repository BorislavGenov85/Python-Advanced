data = input()
unique = {}

for ch in data:
    if ch not in unique:
        unique[ch] = 0
    unique[ch] += 1

sorted_unique = {key: unique[key] for key in sorted(unique)}

for key, value in sorted_unique.items():
    print(f"{key}: {value} time/s")
