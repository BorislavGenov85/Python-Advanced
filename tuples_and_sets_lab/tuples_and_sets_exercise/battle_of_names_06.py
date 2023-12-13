num = int(input())
odd_set = set()
even_set = set()

for i in range(1, num + 1):
    name = input()
    name_current_value = 0
    for ch in name:
        name_current_value += ord(ch)

    name_total_value = int(name_current_value / i)

    if name_total_value % 2 != 0:
        odd_set.add(name_total_value)
    else:
        even_set.add(name_total_value)

if sum(odd_set) == sum(even_set):
    last = odd_set | even_set
    last = [str(x) for x in last]
    print(f"{', '.join(last)}")

elif sum(odd_set) > sum(even_set):
    last = odd_set - even_set
    last = [str(x) for x in last]
    print(f"{', '.join(last)}")

else:
    last = even_set ^ odd_set
    last = [str(x) for x in last]
    print(f"{', '.join(last)}")

# second

# number = int(input())
#
# even = set()
# odd = set()
#
# for i in range(1, number + 1):
#     data = input()
#     total = 0
#     for ch in data:
#         total += ord(ch)
#     result = total // i
#
#     if result % 2 == 0:
#         even.add(result)
#     else:
#         odd.add(result)
#
# if sum(even) == sum(odd):
#     result = even | odd
#     print(", ".join([str(x) for x in result]))
# elif sum(odd) > sum(even):
#     result = odd - even
#     print(", ".join([str(x) for x in result]))
# else:
#     result = even ^ odd
#     print(", ".join([str(x) for x in result]))