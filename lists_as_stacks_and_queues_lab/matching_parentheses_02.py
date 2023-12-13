# first solution

data = input()
position = []
match_symbols = ["(", ")"]

for i in range(len(data)):
    if data[i] == match_symbols[0]:
        position.append(i)
    elif data[i] == match_symbols[1]:
        first_idx = position.pop()
        print(data[first_idx:i + 1])

# second solution

# expression = input()
#
# open_parentheses = []
#
# for i in range(len(expression)):
#     ch = expression[i]
#     if ch == "(":
#         open_parentheses.append(i)
#     elif ch == ")":
#         print(expression[open_parentheses.pop():i + 1])
