class ValueCannotBeNegative:
    pass


for _ in range(5):
    try:
        num = float(input("Please enter number: "))
        if num < 0:
            raise ValueCannotBeNegative

    except ValueError:
        print("This is not a valid number. Continue to next one!")




