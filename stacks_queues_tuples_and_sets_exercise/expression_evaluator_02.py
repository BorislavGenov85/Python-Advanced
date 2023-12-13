from collections import deque

data = input().split()
numbers = deque()

for el in data:
    if el in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()

            result = 0
            if el == "+":
                result = first + second
            elif el == "-":
                result = first - second
            elif el == "*":
                result = first * second
            else:
                result = first // second
            numbers.appendleft(result)

    else:
        numbers.append(int(el))

print(*numbers)

# second

# from collections import deque
#
#
# def evaluate_numbers(iterable, ch):
#     while len(iterable) > 1:
#         first = iterable.popleft()
#         second = iterable.popleft()
#         result = 0
#
#         if ch == "*":
#             result = first * second
#         elif ch == "+":
#             result = first + second
#         elif ch == "-":
#             result = first - second
#         else:
#             result = first // second
#         iterable.appendleft(result)
#
#     return iterable
#
#
# data = input().split()
# numbers = deque()
#
# for el in data:
#     if el in "*+-/":
#         evaluate_numbers(numbers, el)
#
#     else:
#         numbers.append(int(el))
#
# print(*numbers)

