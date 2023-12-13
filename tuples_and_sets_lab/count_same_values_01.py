numbers = [float(x) for x in input().split()]
number_of_occurrences = {}

for num in numbers:
    if num not in number_of_occurrences:
        number_of_occurrences[num] = 0
    number_of_occurrences[num] += 1

for item, value in number_of_occurrences.items():
    print(f"{item} - {value} times")
