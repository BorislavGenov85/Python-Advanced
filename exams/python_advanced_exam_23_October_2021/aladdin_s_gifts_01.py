from collections import deque

materials = [int(x) for x in input().split()]
magick_levels = deque([int(x) for x in input().split()])

presents = {"Gemstone": [100, 199],
            "Porcelain Sculpture": [200, 299],
            "Gold": [300, 399],
            "Diamond Jewellery": [400, 499]
            }
crafted_presents = {"Gemstone": 0,
                    "Porcelain Sculpture": 0,
                    "Gold": 0,
                    "Diamond Jewellery": 0
                    }

while materials and magick_levels:
    material = materials[-1]
    magick = magick_levels[0]
    result = material + magick

    if result < 100:
        if result % 2 == 0:
            result = material * 2 + magick * 3

        elif result % 2 != 0:
            result = material * 2 + magick * 2

    if result > 499:
        result /= 2

    if 100 <= result <= 499:
        for item, value in presents.items():
            if presents[item][0] <= result <= presents[item][1]:
                crafted_presents[item] += 1
                break

    materials.pop()
    magick_levels.popleft()

if crafted_presents["Gemstone"] and crafted_presents["Porcelain Sculpture"] >= 1 \
        or crafted_presents["Gold"] and crafted_presents["Diamond Jewellery"] >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magick_levels:
    print(f"Magic left: {', '.join([str(x) for x in magick_levels])}")
crafted_presents = {k: v for k, v in sorted(crafted_presents.items(), key=lambda x: x[0]) if v != 0}
for present, count in crafted_presents.items():
    print(f"{present}: {count}")
