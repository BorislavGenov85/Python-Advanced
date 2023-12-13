from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

substring = deque(input().split())
collected_colors = []

while substring:
    first_substring = substring.popleft()
    second_substring = substring.pop() if substring else ""

    result = first_substring + second_substring
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = second_substring + first_substring
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    first_substring = first_substring[:-1]
    second_substring = second_substring[:-1]
    if first_substring:
        substring.insert(len(substring) // 2, first_substring)
    if second_substring:
        substring.insert(len(substring) // 2, second_substring)

result = []
required_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for color in collected_colors:
    if color in main_colors:
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in collected_colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)

print(result)
