from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]
total_number_of_toys = 0
total_used_energy = 0
counter = 0

while elves_energy and materials:
    made_toy = 0
    energy_spend = 0

    energy = elves_energy.popleft()
    material = materials.pop()

    if energy < 5:
        materials.append(material)
        continue

    if energy < material:
        elves_energy.append(energy * 2)
        materials.append(material)
        continue

    counter += 1
    if counter % 3 != 0:
        energy_spend += material
        made_toy += 1
        energy -= material
        elves_energy.append(energy + 1)

    if counter % 3 == 0:
        if energy >= material * 2:
            made_toy += 2
            energy_spend += material * 2
            energy = (energy - material * 2) + 1
            elves_energy.append(energy)
        else:
            elves_energy.append(energy * 2)
            materials.append(material)

    if counter % 5 == 0:
        made_toy = 0
        elves_energy[-1] -= 1

    total_number_of_toys += made_toy
    total_used_energy += energy_spend


print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")
if elves_energy:
    print(f"Elves left: {', '.join([str(x) for x in elves_energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
