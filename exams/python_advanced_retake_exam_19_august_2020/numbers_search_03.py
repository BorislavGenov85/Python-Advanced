def numbers_searching(*args):
    lst = sorted(args)
    duplicate_numbers = []
    missing_numbers = 0

    for el in lst:
        if lst.count(el) > 1 and el not in duplicate_numbers:
            duplicate_numbers.append(el)

    for i in range(lst[0], lst[-1]):
        if i not in lst:
            missing_numbers = i
            break

    missing_numbers = [missing_numbers, duplicate_numbers]
    return missing_numbers


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
