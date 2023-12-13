data = input()
parentheses = []
balanced = True

for ch in data:
    if ch in "{[(":
        parentheses.append(ch)

    elif not parentheses:
        balanced = False
        break

    else:
        last_clamp = parentheses.pop()
        if f"{last_clamp}{ch}" not in "()[]{}":
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")

# data = [x for x in input()]
# parentheses = []
# opening = ["{", "[", "("]
# closing = ["}", "]", ")"]
#
# for i in range(len(data)):
#     current_clamp = data[i]
#     if current_clamp in opening:
#         parentheses.append(current_clamp)
#     elif not parentheses:
#         print("NO")
#         exit(0)
#     else:
#         if current_clamp == "}" and parentheses[-1] == "{" or current_clamp == "]" and parentheses[-1] == "[" \
#                 or current_clamp == ")" and parentheses[-1] == "(":
#             parentheses.pop()
# if parentheses:
#     print("NO")
# else:
#     print("YES")
