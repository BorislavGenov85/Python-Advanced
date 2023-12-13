from collections import deque


def list_manipulator(*args):
    lst = deque(args[0])
    command = args[1]
    sub_command = args[2]

    if command == "add":
        parameters = list(args[3:])

        if sub_command == "beginning":
            for i in range(len(parameters) - 1, -1, -1):
                el = parameters[i]
                lst.appendleft(el)
            return list(lst)

        else:
            lst.extend(parameters)
            return list(lst)

    else:
        parameters = args[3:]
        if parameters:
            number = parameters[0]
            if sub_command == "beginning":
                for _ in range(number):
                    lst.popleft()
                return list(lst)

            else:
                for _ in range(number):
                    lst.pop()
                return list(lst)

        else:
            if sub_command == "beginning":
                lst.popleft()
                return list(lst)

            else:
                lst.pop()
                return list(lst)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
