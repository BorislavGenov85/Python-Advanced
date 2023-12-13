from collections import deque

effects = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]

bombs_info = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}
datura_bombs = 0
cherry_bombs = 0
smoke_bombs = 0
fill = False

while effects and casings:
    effect = effects[0]
    casing = casings[-1]
    result = effect + casing

    if result not in bombs_info.values():
        casings[-1] -= 5
        continue
    else:
        if result == 40:
            datura_bombs += 1

        elif result == 60:
            cherry_bombs += 1

        elif result == 120:
            smoke_bombs += 1
    casings.pop()
    effects.popleft()

    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_bombs >= 3:
        fill = True
        break

if fill:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if not effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
if not casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_bombs}")
