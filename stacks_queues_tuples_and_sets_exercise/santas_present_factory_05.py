from collections import deque

boxes = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
    }
crafted_presents = {}

while magic_levels and boxes:
    box = boxes.pop()
    magic = magic_levels.popleft()

    result = box * magic

    if result in presents:
        toy = presents[result]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1

    elif result < 0:
        boxes.append(box + magic)

    elif result > 0:
        boxes.append(box + 15)

    else:
        if box == 0 and magic == 0:
            continue

        if box == 0:
            magic_levels.appendleft(magic)
        else:
            boxes.append(box)

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
        ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    boxes.reverse()
    print(f"Materials left: {', '.join([str(x) for x in boxes])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

for name, count in sorted(crafted_presents.items()):
    print(f"{name}: {count}")
