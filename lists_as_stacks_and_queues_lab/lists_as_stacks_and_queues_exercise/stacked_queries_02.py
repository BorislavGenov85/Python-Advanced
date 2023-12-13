num = int(input())
stack = []
for _ in range(num):
    command = input().split()
    if command[0] == "1":
        number = int(command[1])
        stack.append(number)

    elif command[0] == "2" and stack:
        stack.pop()

    elif command[0] == "3" and stack:
        max_num = max(stack)
        print(max_num)

    elif command[0] == "4" and stack:
        min_num = min(stack)
        print(min_num)

stack = [str(x) for x in stack]
stack.reverse()
print(", ".join(stack))
