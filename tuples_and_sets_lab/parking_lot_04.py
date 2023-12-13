num = int(input())
parking_lot = set()

for _ in range(num):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    for car_number in parking_lot:
        print(car_number)
else:
    print("Parking Lot is Empty")

# second
# number = int(input())
#
# car_lot = set()
#
# for _ in range(number):
#     data = input().split(", ")
#
#     if data[0] == "IN":
#         car_lot.add(data[1])
#     else:
#         car_lot.remove(data[1])
#
# if car_lot:
#     print(*car_lot, sep="\n")
# else:
#     print("Parking Lot is Empty")
