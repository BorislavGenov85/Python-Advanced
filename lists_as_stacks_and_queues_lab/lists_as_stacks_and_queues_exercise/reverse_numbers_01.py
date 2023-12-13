string = input().split()
reversed_str = []

while string:
    num = string.pop()
    reversed_str.append(num)

print(" ".join(reversed_str))
