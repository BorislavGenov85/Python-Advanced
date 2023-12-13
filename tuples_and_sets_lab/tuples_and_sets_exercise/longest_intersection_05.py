# first solution

num = int(input())
segments = []


for _ in range(num):
    data = input().split("-")
    first_section = data[0].split(",")
    start, end = int(first_section[0]), int(first_section[1])
    second_section = data[1].split(",")
    second_start, second_end = int(second_section[0]), int(second_section[1])

    first_set = set()
    for i in range(start, end + 1):
        first_set.add(i)

    second_set = set()
    for j in range(second_start, second_end + 1):
        second_set.add(j)

    current_set = first_set & second_set

    if not segments:
        segments.append(current_set)
    else:
        if len(current_set) > len(segments[0]):
            segments.pop()
            segments.append(current_set)
segments = [*segments[0]]
segments = [str(x) for x in segments]
print(f"Longest intersection is [{', '.join(segments)}] with length {len(segments)}")


# second solution

# number = int(input())
#
# longest = ""
#
# for _ in range(number):
#     data = input().split("-")
#     first = data[0].split(",")
#     first_start = int(first[0])
#     first_end = int(first[1])
#     intersection_1 = [i for i in range(first_start, first_end + 1)]
#
#     second = data[1].split(",")
#     second_start = int(second[0])
#     second_end = int(second[1])
#     intersection_2 = [i for i in range(second_start, second_end + 1)]
#
#     result = set(intersection_1) & set(intersection_2)
#
#     if len(result) > len(longest):
#         longest = result
#
# print(f"Longest intersection is [{', '.join([str(x) for x in longest])}] with length {len(longest)}")
