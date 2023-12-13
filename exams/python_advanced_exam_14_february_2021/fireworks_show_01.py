from collections import deque

effects = deque([int(x) for x in input().split(", ") if int(x) > 0])
powers = [int(x) for x in input().split(", ") if int(x) > 0]
palm = 0
willow = 0
crossette = 0
success = False

while effects and powers:
    effect = effects.popleft()
    if effect <= 0:
        continue
    power = powers[-1]
    result = effect + power

    if result % 3 == 0 and result % 5 == 0:
        crossette += 1
        powers.pop()

    elif result % 3 == 0:
        palm += 1
        powers.pop()

    elif result % 5 == 0:
        willow += 1
        powers.pop()

    else:
        effects.append(effect - 1)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        success = True
        break

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in effects])}")

if powers:
    print(f"Explosive Power left: {', '.join([str(x) for x in powers])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
