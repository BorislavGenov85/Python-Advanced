def even_odd(*nums):
    command = ""
    new_nums = []
    for num in nums:
        if isinstance(num, int):
            new_nums.append(num)
        else:
            command = num

    if command == "even":
        new_nums = [x for x in new_nums if x % 2 == 0]
        return new_nums

    new_nums = [x for x in new_nums if x % 2 != 0]
    return new_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
