number_of_guests = int(input())
vip_guests_code = set()
regular_guests_code = set()

for _ in range(number_of_guests):
    line = input()
    if line[0].isdigit():
        vip_guests_code.add(line)
    else:
        regular_guests_code.add(line)

data = input()
while data != "END":
    if data[0].isdigit():
        vip_guests_code.remove(data)
    else:
        regular_guests_code.remove(data)

    data = input()

vip_guests_code = sorted(vip_guests_code)
regular_guests_code = sorted(regular_guests_code)
guests_who_did_not_come = len(vip_guests_code) + len(regular_guests_code)
print(guests_who_did_not_come)
for guest in vip_guests_code:
    print(guest)
for guest in regular_guests_code:
    print(guest)
