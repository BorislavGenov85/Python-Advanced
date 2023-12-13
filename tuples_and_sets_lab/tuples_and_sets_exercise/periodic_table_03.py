num = int(input())
elements = set()
for _ in range(num):
    elements.update(input().split())

for el in elements:
    print(el)
