from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
gun_barrel_count = gun_barrel_size
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
fired_bullets = 0

while locks and bullets:
    current_lock = locks[0]
    current_bullet = bullets.pop()
    if current_lock < current_bullet:
        print("Ping!")
    else:
        locks.popleft()
        print("Bang!")

    gun_barrel_count -= 1
    fired_bullets += 1

    if gun_barrel_count == 0 and bullets:
        print("Reloading!")
        gun_barrel_count = gun_barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - (fired_bullets * bullet_price)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
