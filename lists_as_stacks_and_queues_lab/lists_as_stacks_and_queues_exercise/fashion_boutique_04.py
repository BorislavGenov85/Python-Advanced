# first solution

stack = [int(x) for x in input().split()]
capacity_of_rack = int(input())
rack = 1
value = 0

while stack:
    current_value = stack.pop()
    if current_value + value == capacity_of_rack:
        value = 0
        if stack:
            rack += 1
    elif current_value + value > capacity_of_rack:
        rack += 1
        value = 0
        value += current_value
    else:
        value += current_value

print(rack)

# second solution

# clothes = [int(x) for x in input().split()]
# capacity = int(input())
#
# rack = 1
# cloth_sum = 0
#
# while clothes:
#     current_cloth = clothes.pop()
#
#     if cloth_sum + current_cloth <= capacity:
#         cloth_sum += current_cloth
#     else:
#         rack += 1
#         cloth_sum = current_cloth
#
# print(rack)
