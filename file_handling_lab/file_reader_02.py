data = open("numbers.txt", "r")
lines = data.read().split("\n")
lines = [int(el) for el in lines if el != ""]
result = sum(lines)
print(result)
